from app.get_data_online import get_data2
from app.search_prof import sortdata, getmean


def test_sortdata():
    samplename="Marc Howard"
    sampledata = sortdata(samplename)
    assert len(sampledata) < 1000
    assert sampledata['Instructor Name'].nunique() == 1
    assert sampledata['Instructor Name'].iloc[0] == samplename

def test_getmean():
    samplename="Marc Howard"
    data = sortdata(samplename)
    teststats=getmean(data)
    assert len(teststats) == 4
    assert sum(teststats) > 0