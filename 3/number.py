def main():
    x = get_int("Whats x? ")
    print(f"x is {x}")

 
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()