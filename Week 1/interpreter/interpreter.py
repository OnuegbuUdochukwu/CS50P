def main():
    equation = input("").split(" ")
    if(equation[1] == "+"):
        print(add(equation))
    elif(equation[1] == "-"):
        print(sub(equation))
    elif equation[1] == "*":
        mul(equation)
    elif equation[1] == "/":
        div(equation)


def add(eq):
    return float(eq[0]) + float(eq[2])

def sub(eq):
    return float(eq[0]) - float(eq[2])

def mul(eq):
    return float(eq[0]) * float(eq[2])

def div(eq):
    return float(eq[0]) / float(eq[2])

main()



# Easier method
#Interpreter

equation = input("enter your equation: ").strip().lower()

x, y , z = equation.split(" ")

x = int(x)
z = int(z)

if y == "+":
    print(f"{(x+z):.1f}")
elif y == "-":
    print(f"{(x-z):.1f}")
elif y == "*":
    print(f"{(x*z):.1f}")
elif y == "/" and z == 0:
    print(f"second value cannot be zero")
elif y == "/":
    print(f"{(x/z):.1f}")
