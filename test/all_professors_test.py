
from app.get_data_online import get_data2
from app.all_professors import unique_instructors

def test_unique_professors():
    column_name = 'Instructor Name'
    df = get_data2()
    profslist=unique_instructors()
    unique_values = df[column_name].unique()
    assert isinstance(profslist, list)
    assert len(profslist) == len(unique_values)
    