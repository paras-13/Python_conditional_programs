# Write a program to check whether the given number is Armstrong number or not .
# (Note: If a 3 digit number is equal to the sum of the cubes of its each digit , then it is an Armstrong number )
num = int(input("Enter a three digit number:"))
sum = 0
tnum = num
while tnum != 0:
    rem = tnum%10
    sum+= rem**3
    tnum = tnum//10
if sum == num:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")