# from datetime import datetime

# def time_in_minutes(date_object):
#     """Return the total time in minutes from a given date object."""
#     total_minutes = date_object.hour * 60 + date_object.minute
#     return total_minutes

# # Example usage:
# now = datetime.now()
# minutes = time_in_minutes(now)
# print(f"Current time in minutes: {minutes}")



# from datetime import datetime

# def difference_in_minutes(date1, date2):
#     """Return the difference in minutes between two date objects."""
#     delta = date2 - date1  # Calculate the difference
#     return delta.total_seconds() / 60  # Convert seconds to minutes

# # Example usage:
# date1 = datetime(2023, 10, 30, 12, 0)  # October 30, 2023, 12:00 PM
# date2 = datetime(2023, 10, 31, 12, 30)  # October 31, 2023, 12:30 PM

# minutes_difference = difference_in_minutes(date1, date2)
# print(f"Difference in minutes: {minutes_difference}")


from datetime import datetime
from datetime import date
# import datetime

def difference_in_days(date1, date2):
    """Return the difference in days between two date objects."""
    delta = date2 - date1  # Calculate the difference
    return delta.total_seconds() / 60  # Return the difference in days

# Example usage:
date1 = datetime(2023, 10, 1)  # October 1, 2023
date2 = datetime(2023, 10, 31)  # October 31, 2023

days_difference = difference_in_days(date1, date2)
print(f"Difference in days: {days_difference}")

print(type(date.today()))
day= str(date.today()).split("-")
print(day)