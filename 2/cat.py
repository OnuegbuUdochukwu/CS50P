def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Whats n? "))
        if n > 0:
            return n
        #     break
        # return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()