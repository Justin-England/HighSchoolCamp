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
print(f"Presto! Text this instead! \n {phrase_shortened}")

phrase_forward = phrase.lower().replace(" ", "").replace("'", "").replace(",", "").replace(":", "").replace(";", "").replace(".", "")
phrase_backward = (phrase_forward[::-1])

def palindrome(palindrome_check):
    palindrome_check = if(phrase_forward == phrase_backward):
                            print("It's a palindrome!")
                       else:
                            print("Nope! Not a palindrome!")
    return palindrome_check

palindrome_yn = input("Would you like to check if this statement is a palindrome? y / n ")

if(palindrome_yn == "y"):
    print("Ok great! I'll check that for you! ")
    palindrome(phrase)
else:
    print("I don't understand what that means. ")

if(palindrome_yn == "n"):
    print("Well, if you say so. ")
else:
    print("I don't understand what that means. ")