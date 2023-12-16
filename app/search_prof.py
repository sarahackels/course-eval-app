from app.get_data_online import get_data2


def sortdata(name):
    
    ##get data
    our_df = get_data2()

    ##sort data by professor name
    sorted = our_df[our_df["Instructor Name"].str.contains(name) ]
   
    #remove redundant columns
    columns_to_remove=['sheet_name','season','year']
    updated_df = sorted.drop(columns=columns_to_remove)

    #print(updated_df)
    return updated_df

def getmean(data):

    ##length of list of classes is the number of courses
    coursenumber = len(data)

    ##other stats on this professor
    meaneval = data["Overall evaluation of instructor"].mean().round(3)
    lowesteval = data["Overall evaluation of instructor"].min()
    highesteval = data["Overall evaluation of instructor"].max()

    ##turn these other stats into a list
    stats = [coursenumber, meaneval, lowesteval, highesteval]
    #print(stats)
    #return the list
    return stats

if __name__ == "__main__":
    instructor_name = input("Type last name of instructor you want to investigate: ")
    data = sortdata(instructor_name)
    getmean(data)