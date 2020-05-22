# Challenge name :- 21 days of Coding
# Day = 6

"""
prob description = Consider a long alley with a N number of doors on one side. All the doors are closed initially. You move to and fro in the alley changing the states of the doors as follows: you open a door that is already closed and you close a door that is already opened. You start at one end go on altering the state of the doors till you reach the other end and then you come back and start altering the states of the doors again.
In the first go, you alter the states of doors numbered 1, 2, 3, … , n.
In the second go, you alter the states of doors numbered 2, 4, 6…
In the third go, you alter the states of doors numbered 3, 6, 9 …
You continue this till the Nth go in which you alter the state of the door numbered N.
You have to find the number of open doors at the end of the procedure.

    Input:
    372
    2
    100
    825625
    63542

    Output:
    19
    1
    10
    908
    252
    Explanation:

"""

def count_open_doors(num):
    a = []
    # for initializing array with all doors closed represented with 0
    for i in range(num):
        a.append(0)

    for x in range(1, num):
        for j in range(1, num):
            if x * j < num:
                if a[x * j] == 0:
                    a[x * j] = 1
                else:
                    a[x * j] = 0
            else:
                break

    count = 0

    for x in range(len(a)):
        if a[x] == 1:
            count += 1

    print(count)

count_open_doors(825625)