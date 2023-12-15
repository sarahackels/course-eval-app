from app.get_data_online import get_data2


def sortdata(name):
    
    our_df = get_data2()
    sorted = our_df[our_df["Instructor Name"].str.contains(name) ]
   
    #remove redundant columns
    columns_to_remove=['sheet_name','season','year']
    updated_df = sorted.drop(columns=columns_to_remove)

    #print(updated_df)
    return updated_df

def getmean(data):

    coursenumber = len(data)
    meaneval = data["Overall evaluation of instructor"].mean().round(3)
    lowesteval = data["Overall evaluation of instructor"].min()
    highesteval = data["Overall evaluation of instructor"].max()

    stats = [coursenumber, meaneval, lowesteval, highesteval]
    #print(stats)
    return stats

if __name__ == "__main__":
    instructor_name = input("Type last name of instructor you want to investigate: ")
    data = sortdata(instructor_name)
    getmean(data)