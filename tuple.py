def count_vowels(string):

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_count = 0

    for char in string:
        if char in vowels:
            vowels_count +=1


    return vowels_count

input_string = input("Enter a string: ")
result = count_vowels(input_string)

print(f"The number of vowels in the string is: {result}")
