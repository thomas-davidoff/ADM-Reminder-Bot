import pandas as pd
import numpy as np
from sheets_importer import sheet_data

from datetime import timedelta, datetime
from pytz import timezone


def create_df(raw_data):
    # Make each array same length
    for array in raw_data[1:]:
        main_col_length = len(raw_data[0])
        length_difference = main_col_length - len(array)
        for row in range(length_difference):
            array.append(' ')

    data_dict = {'time': raw_data[0]}
    for column_number in range(len(raw_data) - 1):
        col_title = f'slot {column_number + 1}'
        data_dict[col_title] = raw_data[column_number + 1]

    df = pd.DataFrame(data_dict)
    df = df.replace('', np.nan)
    df = df.dropna(how='all')

    return df


def clean_df(df):
    weekday = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    index_col = df.time

    # Create Series of days from time column of raw df and reindex to forward fill values
    days = index_col[index_col.str.startswith(weekday, na=False)]
    days = days.reindex(index=range(len(df)), method='ffill')

    # Create Series of time slots from time column of raw df by checking whether first char is numeric
    times = index_col[index_col.fillna(' ').str[0].str.isnumeric()]

    # Create new column combining date and time
    df['datetime'] = pd.to_datetime(days + '; ' + times)

    # Identify which rows are PT rows by filtering out valid datetime entries
    pts = df[df['datetime'].isnull()].iloc[:, 1:-1]
    pts = pts.reindex(index=range(len(df)), method='ffill')

    # Combine PT name with dancer name keeping slot columns
    for i in [i + 1 for i in range(len(df.iloc[:, 1:-1].columns))]:
        col_name = f'slot {i}'
        df[col_name] = df[col_name] + ' | ' + pts[col_name]

    # Drop redundant time column, drop all empty rows
    df = df.drop('time', axis=1).dropna(subset=['datetime']).set_index('datetime').dropna(how='all')

    return df


all_appointments = clean_df(create_df(sheet_data))

eastern_tz = timezone('US/Eastern')
now = datetime.now(eastern_tz)
today = now.strftime('%Y-%m-%d')
tomorrow = (now + timedelta(days=1)).strftime('%Y-%m-%d')

df = pd.concat([all_appointments.loc[today], all_appointments.loc[tomorrow]])
df = pd.concat([df[col] for col in df.columns]).dropna()



next_appointments = []
for i in range(len(df)):
    appointment_info = {}
    values = df[i]
    appointment_info['dancer'], appointment_info['pt'] = values.split(' | ')
    appointment_time = df.index[i]
    appointment_info['datetime'] = appointment_time.strftime('%A, %b %-d at %-I:%M %p')
    appointment_info['relative_time'] = ['tomorrow','today'][appointment_time.strftime('%Y-%m-%d') == today]
    next_appointments.append(appointment_info)
