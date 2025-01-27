# wrong
camelCase = input("camelCase: ")

for letter in camelCase:
    if letter.isupper():
        snakeCase = camelCase.replace(letter, "_"+letter.lower())

print(f"snake_case: {snakeCase}")


# Correct
# Another method
#CAMELCASE
camelCase = input("camelCase: ")

snake_case = ""

for letter in range(len(camelCase)):
    if camelCase[letter].isupper():
        snake_case = snake_case + "_" + camelCase[letter].lower()
        # print(snake_case)
    else:
        snake_case = snake_case +camelCase[letter]

print("snake_case: ", snake_case)
