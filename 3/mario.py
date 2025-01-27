def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n): 
        print("#" * (i + 1 ))
        # print(" " * (n-i-1), "#" * (i+1))

main()