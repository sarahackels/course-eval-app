import pandas as pd
from app.get_data_online import get_data2
from app.search_class import sortdata2

@pytest.fixture
def sample_data():
    data = {
        "Course": ["Math", "History", "Physics", "Math", "Chemistry", "History"],
        "Instructor Name": ["Smith", "Jones", "Johnson", "Smith", "Brown", "Jones"],
    }
    return pd.DataFrame(data)

def test_sortdata2(sample_data, monkeypatch, capsys):
    monkeypatch.setattr("app.get_data_online.get_data2", lambda: sample_data)
    course_name = "Math"
    monkeypatch.setattr('builtins.input', lambda _: course_name)
    sortdata2(course_name)
    captured = capsys.readouterr()
    expected_output = "  Course Instructor Name\n0   Math            Smith\n3   Math            Smith\n"
    assert captured.out == expected_output
