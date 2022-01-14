# with open("./hhgttg.txt", "r") as file:
    # tudo = file.read()
    # file.seek(0)

    # first_line = file.readline()
    # print(first_line)
    # print(first_line.rstrip())
    # file.seek(0)

    for line in file:
        print(line.rstrip())

# with open("./hhgttg.txt", "a") as file:
# with open("./hhgttg.txt", "w") as file:
with open("./hhgttg.txt", "x") as file:
    file.write("But it is the story of that terrible stupid catastrophe and  some of its consequences.\n")

