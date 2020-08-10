# Convert text document into name list:

first = open("names.txt", "r")
names = first.read()
name_list = names.split('","')

name_list[0] = "MARY"
name_list[-1] = "ALONSO"

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#sort alphabetically
sorted_list = sorted(name_list)

total = 0
for i in sorted_list:
    alpha_value = 0
    order_value = sorted_list.index(i) + 1
    for j in i:
        for letter in alphabet:
            if letter == j.lower():
                alpha_value += alphabet.index(letter) + 1
    total += alpha_value * order_value
print(total)




