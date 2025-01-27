def main():
    ...
    mealTime = input("Enter the time: ")
    check = convert(mealTime)

    if (7 <= check <= 8):
        print("Breakfast")
    elif (12 <= check <= 13):
        print("Lunch")
    elif (18 <= check <= 19):
        print("Dinner")


def convert(time):
    ...
    time = time.split(":")
    hour = float(time[0])

    minute = float(time[1]) / 60
    return hour + minute



if __name__ == "__main__":
    main()



# Another method
def main():
    mealTime = input("What time is it? ")

    # Reassign Meal time
    mealTime = float(convert(mealTime))

    if 7 <= mealTime <= 8:
        print("Breakfast time")
    elif 12 <= mealTime <= 13:
        print("Lunch time")
    elif 18 <= mealTime <= 19:
        print("Dinner time")


def convert(time):
    time = time.replace(":", ".")
    hours, minutes = map(float, time.split("."))
    # time = float(time)
    # left, right = time.split(".")
    hours = int(hours)
    minutes = int(minutes)

    courseTime = hours + (round((minutes / 60), 2))
    return float(courseTime)


if __name__ == "__main__":
    main()
