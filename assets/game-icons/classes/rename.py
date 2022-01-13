import os

cwd = os.getcwd()
file_list = []

for file in os.listdir(cwd):
    file = file.replace(".png", "").replace(".jpg", "")
    if "-" in file:
        split_str = file.split('-')
        last_str = split_str[1].capitalize()
        file_list.append(split_str[0] + ": " + last_str)
    else:
        file_list.append(file + ": ")
file_list = [i + '\n' for i in file_list]
with open('credit-out.txt', 'w') as writer:
    writer.writelines(file_list)
