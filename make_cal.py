input_operator = input("Enter the input operator: ")
num1 =int(input("Enter the number:"))
num2 = int(input("Enter the number: "))

if input_operator == '+':
    sum = num1 + num2
    print(sum)
elif input_operator =='-':
    sub = num1 - num2
    print(sub)
elif input_operator == '/':
    div = num1 / num2
    print(div)
elif input_operator == '%':
    mod = num1 % num2
    print(mod)
elif input_operator =='*':
    mul = num1 * num2
    print(mul)
elif input_operator == '**':
    exp = num1**num2
    print(exp)
elif input_operator == "//":
    ceil = num1 // num2
    print(ceil)
else:
    print("Does not exit")