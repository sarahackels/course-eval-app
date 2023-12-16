
from app.search_class import sortdata2


def test_sortdata2():
    samplename="OPIM244"
    sampledata = sortdata2(samplename)
    assert len(sampledata) < 1000
    assert sampledata['Course'].nunique() == 1
    assert sampledata['Course'].iloc[0] == samplename
