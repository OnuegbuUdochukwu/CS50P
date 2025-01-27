def main():
    sentence = input()
    print(playback(sentence))

def playback(result):
    result = result.replace(" ", "...")
    return result

main()


#Easier method
sentence = input().replace(" ", "...")
print(sentence)