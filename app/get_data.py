## going to turn this into a google api but for 
##right now its goign to pull the data from my computer

import pandas as pd

def import_csv_to_dataframe(file_path):
    try:
        # Use pandas to read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        return df

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Unable to parse the file '{file_path}'. Please check the file format.")
        return None

def getdata():
    # Replace 'path/to/your/file.csv' with the actual path to your CSV file
    csv_file_path = '/Users/sarahackels/Downloads/Year 4/OPAN/course-eval-app/Evaluation_Data.csv'

    # Import CSV file into a Pandas DataFrame
    df = import_csv_to_dataframe(csv_file_path)

    # Now you can work with the DataFrame 'df' as needed
    return df

if __name__ == "__main__":
    getdata()
