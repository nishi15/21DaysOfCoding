# Challenge name :- 21 days of Coding
# Day = 2

"""
prob description = Given a string S containing only lower case alphabets, the task is to sort it in lexigraphically-descending order.
    Input:
geeks for
    Output:
skgee rof
"""

def sortstring(string):
    """Function to sort the given string in descending order"""
    string_list = string.split()
    new_string = ''
    new_list = []

    for i in range(len(string_list)):
        new_list = sorted(string_list[i],reverse=True)
        for j in new_list :
            new_string += j
        new_string += " "


    print(new_string)

sortstring("i love programming")

