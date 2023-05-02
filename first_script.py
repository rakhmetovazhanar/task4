import pytest

@pytest.mark.slow
def test_my_fast():
    sdu = "zhanar"
    assert "zhan" in sdu

@pytest.mark.slow
def test_my():
    number = 100
    assert 99+1 == number
    
 @pytest.mark.slow
def test_my_zh():
    number2 = 1000
    assert 999+1 == number2   
    
