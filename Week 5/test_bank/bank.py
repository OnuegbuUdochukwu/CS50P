def main():
    greeting = input("Greeting: ").strip().split(" ")
    print(value(greeting))


def value(greeting):
    if greeting[0].lower() == "hello":
        money = 0
    elif greeting[0].lower().startswith("h"):
        money = 20
    else: 
        money = 100
    return money


if __name__ == "__main__":
    main()