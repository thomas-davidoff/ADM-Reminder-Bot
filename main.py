from parser import next_appointments
from mako.template import Template
from google_connect import gmail_service
import json
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def create_html(appt, temp):
    person = appt['dancer']
    pt = appt['pt']
    time = appt['datetime']
    relative_time = appt['relative_time']

    render = temp.render(dancer=person, pt=pt.capitalize(), appt_time=time, relative_time=relative_time)
    return render


def create_message(recipient, email_html, appt_time):
    message = MIMEMultipart("alternative")
    message['To'] = recipient
    message['From'] = 'ptappointmentbot@gmail.com'
    message['Subject'] = f'PT Appointment Reminder for {appt_time}'

    mime_html = MIMEText(email_html, 'html')
    message.attach(mime_html)
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    email_message = {'raw': encoded_message}
    return email_message


def send_mail(service, message):
    send_message = service.users().messages().send(userId="me", body=message).execute()
    return send_message


if __name__ == '__main__':
    script_directory = os.path.dirname(os.path.abspath(__file__))
    email_file = os.path.join(script_directory, 'emails.json')
    template_file = os.path.join(script_directory, 'email_template.html')

    template = Template(filename=template_file)
    with open(email_file) as f:
        email_dict = json.load(f)
        email_dict = {k.lower(): v for k, v in email_dict.items()}

    # example_appt = [{
    #     'dancer': 'Thomas',
    #     'pt': 'ANN',
    #     'datetime': 'Thursday, Feb 9 at 4:50 PM',
    #     'relative_time': 'tomorrow'
    # }]
    #
    # next_appointments = example_appt

    for appointment in next_appointments:
        email_render = create_html(appointment, template)
        dancer = appointment['dancer'].lower().strip()
        if dancer in email_dict:
            print(f'Sending to {dancer} at {email_dict[dancer]}...')
            finished_email = create_message(email_dict[dancer], email_render, appointment['datetime'])
            send_mail(gmail_service, finished_email)
        else:
            print(f'Could not find {dancer} in email file.')
