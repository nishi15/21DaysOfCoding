# Challenge name :- 21 days of Coding
# Day = 3

"""
prob description = Given an unsorted array arr[] of size N, rotate it by D elements (clockwise).
    Input:
2
1 2 3 4 5
3
2 4 6 8 10 12 14 16 18 20
    Output:
3 4 5 1 2
8 10 12 14 16 18 20 2 4 6
"""

def rotate(arr,rotating_element):
    arr2=arr[rotating_element:]+arr[:rotating_element]
    for i in arr2:
        print(i,end=" ")
    print()

rotate([40,13,27,87,95,40,96,71,35,79,68,2,98,3,18,93,53,57,2,81,87,42,66,90,45,20,41,30,32,18,98,72,82,76,10,28,68,57,98,54,87,66,7,84,20,25,29,72,33,30,4,20,71,69,9,16,41,50,97,24,19,46,47,52,22,56,80,89,65,29,42,51,94,1,35,65,25],69)


