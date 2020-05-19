# Challenge name :- 21 days of Coding
# Day = 4

"""
prob description = Given an array of positive integers. Your task is to find the leaders in the array.
Note: An element of array is leader if it is greater than or equal to all the elements to its right side. Also, the rightmost element is always a leader.

    Input:
16 17 4 3 5 2
1 2 3 4 0
    Output:
17 5 2
4 0
"""


def leader(arr):
    for i in range(len(arr)):
        temp = 0
        for j in range(i + 1, len(arr)):
            if arr[i] >= arr[j]:
                temp = arr[i]
            else:
                temp = 0
                break
        if temp > 0:
            print(temp, end=" ")
    print(arr[-1])


leader([7, 4, 5, 7, 3])

# Code 2
"""
prob description = You a given a number N. You need to print the pattern for the given value of N.

        for N=2 the pattern will be 
        2 2 1 1
        2 1
        for N=3 the pattern will be 
        3 3 3 2 2 2 1 1 1
        3 3 2 2 1 1
        3 2 1
"""

def pattern(num):
    a = num
    while num >0:
        for i in range(a,0,-1):
            print(str(i)*num,end="")
        num = num-1
        print()

pattern(3)


