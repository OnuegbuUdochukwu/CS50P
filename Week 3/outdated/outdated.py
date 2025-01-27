months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        if "/" in date:
            date = date.split("/")
            month = int(date[0])
            day = int(date[1])
            year = int(date[2])
            if month > 12 or day > 31:
                continue

        elif "," in date:
            month, day_and_year = date.split(" ", 1)
            day, year = day_and_year.split(", ")
            month = months.index(month) + 1
            month = int(month)
            day = int(day)
            year = int(year)
            if month > 12 or day > 31:
                continue
        else:
            continue
        
            
        month = f"{month:02}"
        day = f"{day:02}"
        
        print(f"{year}-{month}-{day}")
        break
    
    except (ValueError, IndexError):
        pass

# print(f"{year}-{month:02}-{day:02}")

# months = [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]

# while True:
#     try:
#         date = input("Date: ").strip()
        
#         # Check if input is in MM/DD/YYYY format
#         if "/" in date:
#             month_str, day_str, year_str = date.split("/")
#             month = int(month_str)
#             day = int(day_str)
#             year = int(year_str)
#         # Check if input is in Month DD, YYYY format
#         elif "," in date:
#             month_str, day_year_str = date.split(" ", 1)
#             day_str, year_str = day_year_str.split(", ")
#             month = months.index(month_str) + 1
#             day = int(day_str)
#             year = int(year_str)
#         else:
#             raise ValueError("Invalid date format.")

#         # Format month and day as two digits
#         month = f"{month:02}"
#         day = f"{day:02}"
        
#         print(f"{year}-{month}-{day}")
#         break

#     except (ValueError, IndexError):
#         print("Invalid date, please try again.")
