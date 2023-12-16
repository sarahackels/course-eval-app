import pandas as pd
from app.get_data_online import get_data2
from app.search_prof import sortdata, getmean

@pytest.fixture
def sample_data():
    data = {
        "Instructor Name": ["Smith", "Jones", "Johnson", "Smith", "Brown", "Jones"],
        "Overall evaluation of instructor": [4.5, 3.8, 4.2, 4.0, 4.7, 3.5],
    }
    return pd.DataFrame(data)

def test_sortdata_and_getmean(sample_data, monkeypatch, capsys):
    monkeypatch.setattr("app.get_data_online.get_data2", lambda: sample_data)
    instructor_name = "Smith"
    monkeypatch.setattr('builtins.input', lambda _: instructor_name)
    sorted_data = sortdata(instructor_name)
    captured = capsys.readouterr()
    expected_output = "  Instructor Name  Overall evaluation of instructor\n0           Smith                                4.5\n3           Smith                                4.0\n"
    assert captured.out == expected_output

    stats = getmean(sorted_data)
    expected_stats = [2, 4.25, 4.0, 4.5]
    assert stats == expected_stats
