months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ")

        if "/" in date:
            # Handle date in the format MM/DD/YYYY
            date = date.split("/")
            month = int(date[0])
            day = int(date[1])
            year = int(date[2])

            # Check for valid month, day, and year
            if not (1 <= month <= 12) or not (1 <= day <= 31):
                continue

        elif "," in date:
            # Handle date in the format Month Day, Year
            try:
                month, day_and_year = date.split(" ", 1)
                day, year = day_and_year.split(", ")

                month = months.index(month) + 1
                day = int(day)
                year = int(year)

                # Check for valid month, day, and year
                if not (1 <= month <= 12) or not (1 <= day <= 31):
                    continue
            except ValueError:
                # In case of invalid format
                continue

        else:
            # If there's no comma or slash, invalid format
            print("Invalid format. Please use either MM/DD/YYYY or Month Day, Year format.")
            continue

        # Additional check for days of specific months
        if (month == 2 and day > 29) or (month in [4, 6, 9, 11] and day > 30):
            continue

        # Format the date
        month = f"{month:02}"
        day = f"{day:02}"

        print(f"{year}-{month}-{day}")
        break

    except (ValueError, IndexError):
        continue
