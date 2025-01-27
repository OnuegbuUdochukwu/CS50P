def main():
    while True:
        try:
            percentage = check()
            break
        except(ValueError, ZeroDivisionError):
            pass
    
    printResult(percentage)
    

def getDigits():
    fraction = input("Fraction: ")
    fraction = fraction.split('/')
    numerator = int(fraction[0])
    denominator = int(fraction[1])
    percent = round(numerator/denominator * 100)
    return percent
    

def check():
    p = getDigits()
    while p > 100:
       p = getDigits()
    return p



def printResult(percentage):
    if percentage <= 1:
        print(f"E")  
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%") 

main()


# Old Me

import sys
# def main():
#     first, last = errorCheck().split("/")
#     # print(first, last)

#     percent = get_percentage(first, last)
#     # print(percent)

#     if percent < 1:
#         print("E")
#     elif percent > 99:
#         print("F")
#     else:
#         print(f"{percent}%")

# def errorCheck():
#     try:
#         value =  input("Fraction: ")
#     except(ValueError, ZeroDivisionError):
#         print("cannot work")
#     else:
#         return value

# def get_percentage(f,l):
#    f = int(f)
#    l = int(l)
#    return (f/l) *100



# main()

def main():
    fuel  = input("Fraction: ")
    if fuel.find("-") == 1:
        fuel  = input("Fraction: ")
    first, last = fuel.split("/")
    value = check(first, last)

    # print(value)

    # percentage = percent(first,last)
    first,last = int(first), int(last)

    fuel_guage = (first/last)*100

    if fuel_guage<=1:
        print("E")
    elif 1<fuel_guage<99:
        print(f"{fuel_guage:.0f}%")
    elif fuel_guage>=99:
        print("F")
def check(f,l):
    try:
        f,l = int(f),int(l)
    except (ValueError):
        main()
        sys.exit()
    else:
        if f>l:
            main()
        elif l == 0:
            main()
        else:
            return f,l


# def percent(x,y):
#     x,y = int(x),int(y)
#     if x>y:
#         main()
#     elif y == 0:
#         # if (x/y*100) <1:
#         #     print("E")
#         # elif (x/y*100) > 99:
#         #     print("F")
#         # else:
#         #     print(x/y*100)
#         main()
#     else:
#         return x,y


main()