from app.get_data import getdata
import pandas as pd

def test_get_data():
    data = getdata()
    assert isinstance(data, pd.DataFrame)
    expected_columns = ['Instructor Name','Term','Course','Section','Course Title','Hours spent studying per week','Effectiveness of readings & research','Exams, etc., represent course content','How much did you learn in course','Classroom presentations stimulating','Instructor available outside class','Overall evaluation of instructor','sheet_name','season','year']
    assert data.columns.tolist() == expected_columns
    assert data.shape[0] > 100