house = input("Whats your name? ")
 
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Grinfindor")
    case "Draco":
        print("Slytherin")
    case _: