amountPaid = 0
amountDue = 50

while (amountPaid <= 50):
    print(f"Amount Due: {amountDue}")
    if amountDue >= 0:
        amountPaid = int(input("Insert Coin: "))

    if amountPaid == 5 or amountPaid == 10 or amountPaid == 25:
        amountDue = amountDue - amountPaid
        # print(amountDue)
    if amountDue <= 0:
        break

print(f"Change Owed: {abs(amountDue)}")