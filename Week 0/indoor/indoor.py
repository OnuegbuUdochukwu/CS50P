def main():
    saySomething = input()
    indoor(saySomething)

def indoor(sentence):
    print(sentence.lower())

main()


# Easier method
yell = input().lower()
print(yell)
