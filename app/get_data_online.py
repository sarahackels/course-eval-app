import gspread
from google.oauth2 import service_account
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DEFAULT_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "google-credentials.json")
GOOGLE_CREDENTIALS_FILEPATH = os.getenv("GOOGLE_CREDENTIALS_FILEPATH", default=DEFAULT_FILEPATH)
DOCUMENT_ID = os.getenv("DOCUMENT_ID")

def authenticate_gspread(credentials_path=GOOGLE_CREDENTIALS_FILEPATH):
    try:
        creds = service_account.Credentials.from_service_account_file(
            credentials_path, 
            scopes=['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        )
        gc = gspread.authorize(creds)
        return gc
    except Exception as e:
        print(f"Authentication Error: {e}")
        return None

def get_spreadsheet_data(gc, spreadsheet_key, worksheet_name):
    try:
        spreadsheet = gc.open_by_key(spreadsheet_key)
        worksheet = spreadsheet.worksheet(worksheet_name)
        records = worksheet.get_all_records()
        return records
    except Exception as e:
        print(f"Error accessing Google Sheet: {e}")
        return None

def get_data2(key=DOCUMENT_ID):
    
    spreadsheet_key = key
    
    worksheet_name = 'course_evals_combined_20231204'

    # Authenticate with Google Sheets
    gc = authenticate_gspread()

    if gc is not None:
        # Get data from the specified worksheet
        data_records = get_spreadsheet_data(gc, spreadsheet_key, worksheet_name)

        if data_records is not None:
            # Convert the data to a Pandas DataFrame
            df = pd.DataFrame(data_records)

            # Print the DataFrame
            print(df)
            return df
        else:
            print("Error getting data from the worksheet.")
    else:
        print("Error authenticating with Google Sheets.")

if __name__ == "__main__":
    get_data2()
