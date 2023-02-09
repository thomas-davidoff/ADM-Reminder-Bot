from googleapiclient.errors import HttpError
from google_connect import sheets_service
import os


def fetch_sheet_data(service, sheet_id, sheet_range):
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id,
                                range=sheet_range, majorDimension='COLUMNS').execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
        return

    return values


SHEET_RANGE = os.environ['SHEET_RANGE']
SHEET_ID = os.environ['SHEET_ID']


try:
    sheet_data = fetch_sheet_data(sheets_service, SHEET_ID, SHEET_RANGE)
except HttpError as error:
    print(f'An error occured (sheets): {error}')
