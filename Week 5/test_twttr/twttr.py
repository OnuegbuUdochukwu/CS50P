def main():
    word = input("Input: ")
    n_word = shorten(word)
    print("Output:", n_word)

def shorten(word):
    new = ""
    vowel = ["a", "e", "i", "o", "u"]
    for letter in word:
        if letter.lower() in vowel:
            letter.replace(letter, "")
        else:
            new += letter
    
    return new



if __name__ == "__main__":
    main()