import pandas as pd
from app.get_data_online import get_data2
from app.all_classes import unique_classes

def test_unique_classes():
    column_name = 'Course'
    df = get_data2()
    unique_values = df[column_name].unique()
    assert isinstance(unique_classes, list)
    assert len(unique_classes) == len(unique_values)
    assert not unique_classes.duplicated().any()
