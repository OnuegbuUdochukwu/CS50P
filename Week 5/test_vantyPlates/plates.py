def main():
    plate = (input("Plate: ").upper())
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

    # print(plate)


def is_valid(s):
    ...
    # “All vanity plates must start with at least two letters.”
    if s[0:2].isalpha() == False:
        return False

    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if not 2<= len(s)<=6:
        return False


    # “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    i = 0
    while i < len(s):
        if s[i].isdigit() == True:
            if s[i+1].isalpha() == True:
                return False
            # elif s[i+2].isalpha() == True:
            #     return False
            else:
                break
        i += 1
        if s.isalnum() == True:
            if s[-1].isdigit() == True:
                if s[-2].isalpha() == True:
                    return False

    # if s.isalpha() == False:
    #     if s[-1:-3].isdigit() == False:
    #         return False



    # The first number used cannot be a ‘0’.”
    j = 0
    while j < len(s):
        if s[j].isalpha() == False:
            if s[j] == "0":
                return False
            else:
                break
        j += 1

    if s.isalnum() == False:
        return False


    return True
    
if __name__ == "__main__":
    main()