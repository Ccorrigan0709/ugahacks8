from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account

SCOPES = SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)



# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1DjuAuinALN0Pu2WMS-3-KbxPuwi0jw64LPYc5uFlpKw'




# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
# If there are no (valid) credentials available, let the user log in.


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet1!A1:BX2603").execute()
values = result.get('values', []) 

data = [row for row in values] 
print("what is the brandof the car you would like to purchase?")
brand = input()
print("what is the model you want to purchase")
model = input()
print("what is the price of the vehicle?")
price = input()

mPrice = 0


for r in data:
    if (data[r][0] == brand) and (data[r][1] == model):
        for c in r:
            mPrice = data[r][2]
 

difference = price - mPrice
if (difference):
    print("the price of this car is greater than the market-value by approximately $",difference)


            










