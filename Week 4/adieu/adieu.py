import inflect

p = inflect.engine()

# METHODS:

# plural plural_noun plural_verb plural_adj singular_noun no num
# compare compare_nouns compare_nouns compare_adjs
# a an
# present_participle
# ordinal number_to_words
# join
# inflect classical gender
# defnoun defverb defadj defa defan


# UNCONDITIONALLY FORM THE PLURAL
# mylist = ["apple", "banana", "carrot"]
# mylist = p.join((mylist))
# print(mylist)
mylist = []
while True:
    try:
        name = input("Name: ")
    except EOFError:
        print()
        break
    else:
        mylist.append(name)

        
print(mylist)
mylist = p.join((mylist))
print("Adieu, adieu, to", mylist)

