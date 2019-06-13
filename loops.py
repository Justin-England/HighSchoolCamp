"""
title: loops
author: Justin
date: 2019-06-13 09:39
"""

def is_letter(character):
    return character[0].lower() in "qwertyuioplkjhgfdsazxcvbnm"

def short_hand(short):
    short = short.lower().replace("and", "&").replace("too", "2").replace("you", "U").replace("for", "4")
    short = short.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
    return short

phrase = input("Put a long sentence in, get a short sentence out! ")
phrase_shortened = short_hand(phrase)
print(f"\nPresto! Text this instead! \n\n \"{phrase_shortened}\"\n")

phrase_forward = phrase.lower().replace(" ", "").replace("'", "").replace(",", "").replace(":", "").replace(";", "").replace(".", "")
phrase_backward = (phrase_forward[::-1])

def palindrome(phrase_forward, phrase_backward):
    if(phrase_forward == phrase_backward):
        return print("It's a palindrome!")
    else:
        return print("Nope! Not a palindrome!")

palindrome_yn = input("Would you like to check if this statement is a palindrome? y / n ")

if(palindrome_yn == "y"):
    print("\nOk great! I'll check that for you! \n")
    palindrome(phrase_forward, phrase_backward)
elif(palindrome_yn == "n"):
    print("\nWell, if you say so. \n")
else:
    print("\nI don't understand what that means. Please imput a \"y\" or \"n.\" ")

while palindrome_yn not in ["y" or "n"]:
    palindrome_yn = input("\nWould you like to check if this statement is a palindrome? y / n ")

if(palindrome_yn == "y"):
    print("\nOk great! I'll check that for you! \n")
    palindrome(phrase_forward, phrase_backward)
elif(palindrome_yn == "n"):
    print("\nWell, if you say so. ")
else:
    print("\nI don't understand what that means. Please imput a \"y\" or \"n.\" ")