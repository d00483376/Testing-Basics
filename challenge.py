# Challenge:
# Write a function that checks if a given string is a palindrome.
# A palindrome is a word, phrase, or number that reads the same
# backward as forward. Ignore spaces, punctuation, and capitalization.


def is_palindrome(text):
    cleaned = ""
    for char in text:
        if char.isalnum():
            cleaned += char.lower()
    return cleaned == cleaned[::-1]
