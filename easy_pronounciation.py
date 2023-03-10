"""
You are given a string SS consisting of N lowercase Latin characters. 
Determine whether it is easy to pronounce or not based on the rule above — print YES. 
If it is easy to pronounce and NO otherwise.
word is hard to pronounce if it contains 44 or more consonants in a row; 
otherwise it is easy to pronounce. 

Write a program for the same
"""

# Code -->
case = int(input())
str = "aeiou"
for i in range(case):
    L = int(input())
    inp = input()
    count, temp = 0, 0
    for j in range(L):
        if (inp[j] not in str):
            count +=1
        else: count =0
        if (count >=4):
            temp = count
    if (temp>=4):
        print("No")
    else:
        print("Yes")