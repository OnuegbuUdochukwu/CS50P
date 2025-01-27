import re

greeting = input("Greeting: ").strip().split(" ")

if greeting[0].lower() == "hello":
    print("$0")
elif greeting[0].lower().startswith("h"):
    print("$20")
else: 
    print("$100")


# Another method
greeting = input("Greeting: ").lower().strip()

if greeting.__contains__("hello"):
    print("$0")

elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")

# Another method

greeting = input("Greeting: ").lower().strip()
 
if matches := re.search(r"^hello$", greeting):
    print("$0")
elif matches := re.search(r"^h.+", greeting):
    print("$20")
else:
    print("$100")
