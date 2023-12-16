from app.get_data_online import get_data2

def unique_instructors():
    ##get data from main function
    our_df = get_data2()

    ##collect set of all instructor names that are unique and make them a list
    profs = our_df["Instructor Name"].sort_values().unique().tolist()
    #print(len(profs))
    return profs


if __name__ == "__main__":
    unique_instructors()