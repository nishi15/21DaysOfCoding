# Challenge name :- 21 days of Coding
# Day = 1

"""
prob description = Given a string S, write a program to title case every first letter of words in string.

    Input:
I love programming
    Output:
I Love Programming
"""

def case_conversion(string):

    string_list = string.split()
    new_string= ""

    for i in range(len(string_list)):
        new_string += string_list[i].capitalize()+" "

    return new_string

result = case_conversion("I love programming")
print(result)
