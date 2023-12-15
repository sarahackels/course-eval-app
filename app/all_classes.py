from app.get_data_online import get_data2

def unique_classes():
    our_df = get_data2()
    courses = our_df["Course"].sort_values().unique().tolist()
    return courses


if __name__ == "__main__":
    unique_classes()