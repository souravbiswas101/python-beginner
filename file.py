l = ["a", "b", "c"]
with open("test.txt", "w+") as file:
    file.writelines(l)
    print(file.read())