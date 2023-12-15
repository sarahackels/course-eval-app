import gspread
from google.oauth2 import service_account
import pandas as pd



def authenticate_gspread(credentials_path):
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

def get_data2():

    credentials_path = '/Users/coleguzzetta/Documents/GitHub/course-eval-app/client_secrets.json'
    
    spreadsheet_key = '1LeZzY7Btb2TH_oWWbQl-EQEvIt9n4HKrfDCm3qE16BI'
    
    worksheet_name = 'course_evals_combined_20231204'

    # Authenticate with Google Sheets
    gc = authenticate_gspread(credentials_path)

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
