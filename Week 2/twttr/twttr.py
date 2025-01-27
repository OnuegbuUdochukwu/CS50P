first = input("Input: ")
vowels = ["a", "e", "i", "o", "u"]
output = ""

for letter in first:
    if letter in vowels:
        continue
    output += letter
print(output)



# Another method
word = input("Input: ")

for letter in word:
    vowels = ["a", "e", "i", "o", "u"]
    if not letter.lower() in vowels:
        print(letter, end="")
    