import pytest
from seasons import get, get_minutes, main
from datetime import datetime

def test_get_valid_date():
    """Test get() with a valid date format."""
    # Use pytest's monkeypatch to simulate user input
    date_input = "2000-01-01"
    expected_output = ["2000", "01", "01"]

    # with pytest.raises(SystemExit):
    assert get() == expected_output

def test_get_invalid_date():
    """Test get() with an invalid date format."""
    # Simulate invalid date input
    with pytest.raises(SystemExit):
        get("01-01-2000")  # Wrong format

def test_get_minutes():
    """Test get_minutes with a known date difference in minutes."""
    # Create a fixed past date
    past_date = ["2000", "01", "01"]
    today = datetime.today()
    delta = datetime(today.year, today.month, today.day) - datetime(2000, 1, 1)
    expected_minutes = delta.total_seconds() / 60

    # Check if the output is close to expected value
    assert pytest.approx(get_minutes(past_date)) == expected_minutes

def test_main_output(capsys):
    """Test main() output for a known date."""
    # Simulate input and capture output
    test_date = "2000-01-01"
    expected_output = "Nine million five hundred thousand minutes\n"
    
    # with pytest.MonkeyPatch(test_date):
    #     main()
    #     captured = capsys.readouterr()
    assert captured.out == expected_output
