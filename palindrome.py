# def is_palindrom(word):
#     word = word.lower()
#     return word == word[::-1]

# word = input("Enter your input: ")

# print(is_palindrom(word))

def is_palindrome(word):
    word = word.lower()

    n = len(word)

    for i in range(n //2):
        if word[i] != word[n - 1- i]:
            return False
        
    return True

word = input("Enter your input: ")

print(is_palindrome(word))
