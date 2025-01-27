i = 0
my_list = []
my_dict = {}
while True:
    try:
        item = input()
    except EOFError:
        break
    else:
        my_list.append(item)
        my_dict[item] = my_list.count(item)
        i += 1

# my_list = list(my_dict.keys())
# new = sorted(my_list)

# # print(new)

# for j in range(len(new)):
#     print(new[j].upper())

# print(my_list)
# print(my_dict)
print(sorted(my_dict))
for i in sorted(my_dict):
    print(my_dict[i], i.upper())  # print the key and value in sorted order