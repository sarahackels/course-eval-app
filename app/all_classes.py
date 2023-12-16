from app.get_data_online import get_data2

def unique_classes():
    ##get data from main function
    our_df = get_data2()

    ##collect set of all courses that are unique and make them a list
    courses = our_df["Course"].sort_values().unique().tolist()
    return courses


if __name__ == "__main__":
    unique_classes()