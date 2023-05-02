import pytest

@pytest.mark.slow
def test_my_fast():
    sdu = "zhanar"
    assert "zhan" in sdu

@pytest.mark.slow
def test_my():
    number = 100
    assert 99+1 == number