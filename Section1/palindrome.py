def is_palindrome(word):
    word = word.lower()  
    reversed_word = word[::-1]  

    if word == reversed_word:
        print(f"Yes, the word '{word}' is a palindrome.")
    else:
        print(f"No, the word '{word}' is not a palindrome.")


user_input = input("Enter a word to check if it's a palindrome: ")
is_palindrome(user_input)
