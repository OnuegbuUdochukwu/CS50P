import random

level = 0
while level <= 0:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass

unchanged = random.seed(level)
number = random.randint(1, 100)
print(number)

guess = 0
while guess != number:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too Large!")
        else:
            print("Just right!")
            break