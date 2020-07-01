# Challenge name :- 21 days of Coding
# Day = 8

"""
prob description = Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

  INPUT:-
 "1,2,3,4,5"
 "0,1,2,1,5"

  OUTPUT:-
  True
  False

"""
# Way 1
def distinguish_numbers(str):
    numbers = str.split(",")
    check = []
    for i in range(len(numbers)):
        if numbers[i] in check:
            return False
        else:
            check.append(numbers[i])
    return True

# Way 2
def distinct_numbers(str):
    numbers = str.split(",")

    if len(numbers) == len(set(numbers)):
        return True
    else:
        return False

result = distinguish_numbers("0,1,2,1,5")
print(result)

result2=distinct_numbers("0,1,2,3,4,5")
print(result2)

