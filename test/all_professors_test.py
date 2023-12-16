import pandas as pd
from app.get_data_online import get_data2
from app.all_professors import unique_instructors

def test_unique_professors():
    column_name = 'Instructor Name'
    df = get_data2()
    unique_values = df[column_name].unique()
    assert isinstance(unique_instructors, list)
    assert len(unique_instructors) == len(unique_values)
    assert not unique_instructors.duplicated().any()