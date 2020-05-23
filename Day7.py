# Challenge name :- 21 days of Coding
# Day = 7

"""
prob description = Given two binary strings that represent value of two integers, find the product of two strings. For example, if the first bit string is “1100” and second bit string is “1010”, output should be 120.

    Input:
    1100 01

    Output:
    12


"""

def binary_product(bin1,bin2):

    dec1 = bin_to_dec(bin1)
    dec2 = bin_to_dec(bin2)
    print(dec1,dec2)

    return dec1*dec2

def bin_to_dec(string):
    decimal = 0
    string = string[::-1]
    for i in range(len(string)):
        if int(string[i]) ==1:
            decimal = decimal + pow(2,i)
    return decimal



print(binary_product('1100','01'))