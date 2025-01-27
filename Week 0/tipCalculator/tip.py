def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    return float(d.replace("$", ""))


def percent_to_float(p):
    # TODO
    return float(p.replace("%", ""))/100


main()

# Easier method (or harder.....me sef no sabi oo)
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    if d.startswith("$"):
        return float(d[1:])
    else:
        return float(d)


def percent_to_float(p):
    # TODO
    if p.endswith("%"):
        n = float(p[0:-1])
        raw = n / 100
        return raw
    else:
        m = float(p)
        new = m / 100
        return float(new)


main()