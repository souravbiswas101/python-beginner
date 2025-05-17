def count_unique_chars(string):
    char_count ={}

    for char in string.lower():
        if char.isalnum():
            char_count[char] = char_count.get(char, 0) +1

    result = ','.join([f"{char} = {count}" for char , count in char_count.items()])

    return result

input_string = input("Enter a string: ")
output = count_unique_chars(input_string)
print(output)