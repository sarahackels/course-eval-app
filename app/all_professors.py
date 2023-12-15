from app.get_data_online import get_data2

def unique_instructors():
    our_df = get_data2()
    profs = our_df["Instructor Name"].sort_values().unique().tolist()
    return profs


if __name__ == "__main__":
    unique_instructors()