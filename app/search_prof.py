from get_data_online import get_data2


def sortdata():
    
    our_df = get_data2()
    ##pass in instructor name to get the data back
    instructor_name = input("Type last name of instructor you want to investigate: ")
    sorted = our_df[our_df["Instructor Name"].str.contains(instructor_name) ]
    columns_to_remove=['sheet_name','season','year']
    updated_df = sorted.drop(columns=columns_to_remove)
    print(updated_df)
    print(len(updated_df), "COURSES")
    #doesnt work becuase csv is giving us numbers as strings
    print(updated_df["Overall evaluation of instructor"].mean().round(3), "AVG RATING")

if __name__ == "__main__":
    sortdata()