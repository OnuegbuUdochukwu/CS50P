def main():
    fraction = input("x / y: ")
    percent = convert(fraction)
    print(gauge(percent))


def convert(fraction):
    fraction = fraction.split('/')
    if not (fraction[0].isdigit() and fraction[1].isdigit()):
        raise ValueError

    num = int(fraction[0])
    den = int(fraction[1])

    if (num > den and den != 0):
        raise ValueError

    if den == 0:
        raise ZeroDivisionError
    
    return round(num/den * 100)

def gauge(percentage):
    if percentage <= 1:
        return(f"E")  
    elif percentage >= 99:
        return("F")
    else:
        return(f"{percentage}%") 


if __name__ == "__main__":
    main()


