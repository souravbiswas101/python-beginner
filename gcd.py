def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

result = gcd(48, 18)
print("The Gcd of 48 and 18 is: ", result)