d = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}  # dictionary of menu items and their prices

total = 0
while True:
    try:
        item = input("Item: ").title()
    except KeyError:
        pass
    except EOFError:
        break
    else:
        if item in d:
            total += d[item]
            print(f"${total:.2f}")


# Old Me
# total_cost = 0.0
# try:
#     while True:
#         item = input("Enter an item, or press Control-D to finish: ")
#         item = item.title()
#         if item in felipes:
#             price = felipes[item]
#             total_cost += price
#             print(f"${total_cost:.2f}")
#         elif item == "":
#             break
#         # else:
#         #     print("Sorry, that item is not on the menu.")
# except EOFError:
#     pass
