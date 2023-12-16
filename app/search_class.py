from app.get_data_online import get_data2


def sortdata2(name):
    
    ##get data
    our_df = get_data2()

    ##sort data based on wether it has the name of the chosen course
    sorted = our_df[our_df["Course"].str.contains(name)]
   
    #remove redundant columns
    columns_to_remove=['sheet_name','season','year']
    updated_df = sorted.drop(columns=columns_to_remove)
    #print(updated_df)

    return updated_df


if __name__ == "__main__":
    class_name = input("Type name of the course you want to investigate: ")
    data = sortdata2(class_name)