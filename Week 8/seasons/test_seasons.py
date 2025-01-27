# from seasons import get, get_minutes
# import pytest

# def test_Normal():
#     assert get_minutes([2023, 11, 1]) == 527040

# def test_NotList():
#     with pytest.raises(ValueError):
#         get_minutes("string")

# def 
import pytest
from datetime import datetime
from datetime import date

today_str = datetime.now().strftime("%Y-%m-%d")
print(today_str)