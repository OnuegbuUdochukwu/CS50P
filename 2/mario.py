def main():
    print_square(4)


def print_square(size):

    # For each row in the square
    for i in range(size):
        print_row(size)


def print_row(size):
    # For each brick in a row
    for j in range(size):

        # Print each brick
        print("#", end = "")

    print()

    

main()