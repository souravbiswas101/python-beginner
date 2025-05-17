# def showinfo(name, city="hyderabad"):
#     print("Name: ", name)
#     print("City: ", city)
#     return 

# showinfo(name='Ansh', city='Delhi')
# showinfo(name='Shrey')

# def printInfo(name, age):
#     print("Name: ", name)
#     print("Age:", age)
#     return 

# printInfo("Naveen", 29)
# printInfo( age=30 ,name='miki')

# def add(x, y):
#     z = x+y
#     print("x={} y={} x+y={}". format(x, y,z))


# a = 10
# b = 20
# add(a, b)

# def add(*args):
#     s = 0
#     for x in args:
#         s = s+x

#     return s

# result = add(10, 20, 30, 40)
# print(result)

# result2 = add(1, 2, 3)
# print(result2)
# def sum_list(numbers):
#     total = 0
#     for num in numbers:
#         total +=num
#     return total

# my_list = [1, 2, 3, 4, 5]
# result = sum_list(my_list)

# print(f"The sum of the numbers in the list is: {result}")

# def print_max_of_three(a, b, c):
#     max_num = a
#     if b>max_num:
#         max_num = b
#     if c>max_num:
#         max_num = c
#     print(f"The maximum of {a}, {b}, and {c} is: {max_num}")


# print_max_of_three(10,30, 20)


def check_range(number):
    if 1<=number<=100:
        print("Yes")
    else:
        print("No")

check_range(50)

