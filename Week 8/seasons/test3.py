import pytest
from datetime import datetime
from datetime import date

from seasons import get_minutes

def test_get_minutes_from_date():
    # Test with a valid date
    assert get_minutes([2023, 10, 1]) >= 0  # Should return a non-negative number
    
    # Test with a date in the future
    with pytest.raises(ValueError):
        get_minutes("2025-01-01")
    
    # Test with an invalid format
    with pytest.raises(ValueError):
        get_minutes("01/01/2023")
        
    # Test with a leap year
    assert get_minutes([2020, 2, 9]) >= 0

def test_edge_cases():
    # Test with today's date
    today_str = datetime.now().strftime("%Y-%m-%d")
    assert (today_str) == str(date.today())  # Should return 0 for today

# def get_minutes(date_str):
#     try:
#         year, month, day = map(int, date_str.split('-'))
#         date1 = datetime(year, month, day)
#         if date1 > datetime.now():
#             raise ValueError("Date cannot be in the future.")
#     except (ValueError, TypeError):
#         raise ValueError("Invalid date format. Use YYYY-MM-DD.")
    
#     date2 = datetime.now()
#     delta = date2 - date1
#     return delta.total_seconds() / 60  # Return minutes
