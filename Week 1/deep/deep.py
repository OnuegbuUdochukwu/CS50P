answer = input("Whats the answer? ").lower()

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")


# Easier method
# Deep Thought

question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

match question:
    case "42" | "forty-two"| "forty two":
        print("Yes")
    case _:
        print("No")

