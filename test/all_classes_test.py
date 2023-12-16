from app.get_data_online import get_data2
from app.all_classes import unique_classes

def test_unique_classes():
    column_name = 'Course'
    df = get_data2()
    classlist=unique_classes()
    unique_values = df[column_name].unique()
    assert isinstance(classlist, list)
    assert len(classlist) == len(unique_values)
   
