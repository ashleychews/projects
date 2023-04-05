from project import getinput, convert, symbols
import pytest
from unittest.mock import patch

def main():
    test_getinput()
    test_convert()
    test_symbols()

def test_getinput():
    inputs = ['10', 'USD', 'EUR', '17/12/2021']
    with patch('builtins.input', side_effect=inputs):
        assert getinput() == (10.0, 'USD', 'EUR', '17/12/2021')

def test_convert():
    assert convert(10, "USD", "EUR", "17/12/2021") == 8.829647838325615

    assert convert(100, "GBP", "AUD", "17/12/2021") == 185.72002268620122

    with pytest.raises(ValueError): #test invalid code
        convert(10, "USD", "XXX", "17/12/2021")

    with pytest.raises(ValueError): #test invalid date
        convert(10, "USD", "SGD", "17/12/2020")

def test_symbols():
    assert symbols("USD") == "$"
    assert symbols("EUR") == "€"
    assert symbols("GBP") == "£"
    assert symbols("JPY") == "¥"

if __name__ == '__main__':
    main()
