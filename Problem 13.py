number_file = open("number.txt", "r")
content = number_file.read()
content_list = content.split("\n")
total = 0
for i in content_list:
    total += int(i)

print(total)
