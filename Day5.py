# Challenge name :- 21 days of Coding
# Day = 5

"""
prob description = Monu lives in a society which is having high rise buildings. This is the time of sunrise and monu wants see the buildings receiving the sunlight. Help him in counting the number of buildings recieving the sunlight.
Given an array H representing heights of buildings. You have to count the buildings which will see the sunrise (Assume : Sun rise on the side of array starting point).

    Input:
    7 4 8 2 9
    Output:
    3
    Explanation:
    Building with height 7, 8 and 9 will recieve the sunlight during sunrise.
"""

def sunlight(arr):
    max = arr[0]
    building_count = 1
    new_arr=[arr[0]]

    for i in range(1,len(arr)):
        if(arr[i]>max):
            building_count +=1
            max = arr[i]
            new_arr.append(max)


    print(new_arr)
    return building_count

if __name__ == "__main__":
    print(sunlight([2,3,8,4,5,9]))