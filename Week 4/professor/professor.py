# import random


# def main():
#     level = (get_level()) 
#     number1, number2 = generate_integer(level)
#     print(number1, number2)


#     correct = 0
#     questionNo = 0
#     while questionNo < 10:

#         if level == 1:
#             number1 = random.randint(0, 9)
#             number2 = random.randint(0, 9)
#         elif level == 2:
#             number1 = random.randint(10, 99)
#             number2 = random.randint(10, 99)
#         else:
#             number1 = random.randint(100, 999)
#             number2 = random.randint(100, 999)
#     #     number1 = random.randint(1, 10)
#     #     number2 = random.randint(1, 10)
#         summation = number1 + number2

#         question = int(input(f"{number1} + {number2} = "))
#         testTime = 0

#         if question == summation:
#             correct += 1
#         else:
#             while (testTime < 2 and question != summation):
#                 print("EEE")
#                 question = int(input(f"{number1} + {number2} = "))
#                 testTime += 1
#                 # break
#             if (question != summation and testTime == 2):
#                 print((f"{number1} + {number2} ="), summation)

#         questionNo += 1

#     print("Correct: ", correct,  "/ 10")

# def get_level():
#     level = 0
#     while level not in [1, 2, 3]:
#         try:
#             level = int(input("Level: "))
#         except ValueError:
#             pass
#     return level

# def generate_integer(level):
#     if level not in [1, 2, 3]:
#         raise ValueError
#     return level


# if __name__ == "__main__":
#     main()

import random


def main():
    level = (get_level())
    # number1, number2 = generate_integer(level)
    # print(number1, number2)


    correct = 0
    questionNo = 0
    while questionNo < 10:
        if level == 1:
            number1 = random.randint(0, 9)
            number2 = random.randint(0, 9)
        elif level == 2:
            number1 = random.randint(10, 99)
            number2 = random.randint(10, 99)
        else:
            number1 = random.randint(100, 999)
            number2 = random.randint(100, 999)

        summation = number1 + number2

        question = int(input(f"{number1} + {number2} = "))
        testTime = 0

        if question == summation:
            correct += 1
        else:
            while (testTime < 2 and question != summation):
                print("EEE")
                question = int(input(f"{number1} + {number2} = "))
                testTime += 1
                # break
            if (question != summation and testTime == 2):
                print((f"{number1} + {number2} ="), summation)

        questionNo += 1

    print("Correct:", correct, "/ 10")

def get_level():
    level = 0
    while level not in [1, 2, 3]:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
    return level

def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError


    return level


if __name__ == "__main__":
    main()
