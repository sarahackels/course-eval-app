import gspread
from google.oauth2 import service_account
import pandas as pd
import os
from dotenv import load_dotenv
import base64
import json

load_dotenv()

##get secrets
GOOGLE_CREDENTIALS_FILE = os.getenv("GOOGLE_CREDENTIALS")
DOCUMENT_ID = os.getenv("DOCUMENT_ID")

##turn the environment string into a json file so that the google credentials can read it
def string_to_json(encoded_credentials=GOOGLE_CREDENTIALS_FILE):
    if encoded_credentials:
        decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')
        credentials_json = json.loads(decoded_credentials)
        return credentials_json
    else:
        print("Environment variable for Google Credentials not found.")

##make sure gspread works
def authenticate_gspread(credentials):
    try:
        creds = service_account.Credentials.from_service_account_info(
            credentials,
            scopes=['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        )
        gc = gspread.authorize(creds)
        return gc
    except Exception as e:
        print(f"Authentication Error: {e}")
        return None

## get the data and make sure that it is authenticated
def get_spreadsheet_data(gc, spreadsheet_key, worksheet_name):
    try:
        spreadsheet = gc.open_by_key(spreadsheet_key)
        worksheet = spreadsheet.worksheet(worksheet_name)
        records = worksheet.get_all_records()
        return records
    except Exception as e:
        print(f"Error accessing Google Sheet: {e}")
        return None

##actually bring all the data in and make it into a pandas df
def get_data2(key=DOCUMENT_ID, credentials=string_to_json()):
    spreadsheet_key = key
    worksheet_name = 'course_evals_combined_20231204'

    # Authenticate with Google Sheets
    gc = authenticate_gspread(credentials)

    if gc is not None:
        # Get data from the specified worksheet
        data_records = get_spreadsheet_data(gc, spreadsheet_key, worksheet_name)

        if data_records is not None:
            # Convert the data to a Pandas DataFrame
            df = pd.DataFrame(data_records)

            #print(df)
            return df
        else:
            print("Error getting data from the worksheet.")
    else:
        print("Error authenticating with Google Sheets.")

if __name__ == "__main__":
    get_data2()
