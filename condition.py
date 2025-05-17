my_input = int(input("Enter your number: "))

if (my_input % 3 == 0) and (my_input % 5==0):
    print("FizzBuzz")

elif my_input % 5== 0:
    print("Buzz")

elif my_input % 3 == 0:
    print("Fizz")
else:
    print("Not a FizzBuzz Number")