def main():
    sentence = input()
    print(faces(sentence))

def faces(clause):
    return clause.replace(":)", "🙂").replace(":(", "🙁")

main()

# Easier version
icon = input().replace(":)","🙂").replace(":(","🙁")
print(icon)

