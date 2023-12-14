from get_data import getdata


def sortdata():
    
    our_df = getdata()
    ##pass in instructor name to get the data back
    instructor_name = input("Type name of instructor you want to investigate: ")
    sorted = our_df[our_df["Instructor Name"] == instructor_name]
    columns_to_remove=['sheet_name','season','year']
    updated_df = sorted.drop(columns=columns_to_remove)
    print(updated_df)

if __name__ == "__main__":
    sortdata()