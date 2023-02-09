import os.path
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def connect(credentials_file, tokens_file):
    """
    Checks for Google API credentials from access token.json file in working directory,
    and refreshes credentials using refresh token if the token is not valid or expired. Saves new access
    token to local file for future use

    return: Google API credentials
    """

    credentials = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(tokens_file):
        print('Credentials are valid.')
        credentials = Credentials.from_authorized_user_file(tokens_file, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        print('Credentials are non-existent or not valid.')
        if credentials and credentials.expired and credentials.refresh_token:
            print('Credentials are expired. Refreshing from refresh token.')
            credentials.refresh(Request())
        else:
            print('Building new token file from credentials file.')
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_file, SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        print('Writing new credentials to token.json')
        with open(tokens_file, 'w') as token:
            token.write(credentials.to_json())

    return credentials


script_directory = os.path.dirname(os.path.abspath(__file__))
creds_file = os.path.join(script_directory, 'credentials.json')
token_file = os.path.join(script_directory, 'token.json')

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/gmail.compose'
]

creds = connect(credentials_file=creds_file, tokens_file=token_file)

try:
    sheets_service = build('sheets', 'v4', credentials=creds)
    gmail_service = build('gmail', 'v1', credentials=creds)
except HttpError as error:
    print(f'An error occured (sheets): {error}')
