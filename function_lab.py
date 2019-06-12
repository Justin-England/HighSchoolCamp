"""
title: function_lab
author: Justin
date: 2019-06-12 11:23
"""

import random
import math

print("Hey I'd like to know how old you are.")

print(" ")

born = int(input(f"So what year were you born in? "))

print(" ")

current = int(input(f"By the way, what year is it again? "))

def age(c, b):
    return c - b

print(" ")

output = age(current, born)

if(output <= 0):
    print(f"Hmm... That doesn't make any sense. You can't be {output} years old, that's impossible!")
else:
    print(f"I see so that makes you... {output} years old, right?")



