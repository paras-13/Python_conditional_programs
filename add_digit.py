# Program to add digits of an integer given by the user
num = input("Enter any integer")
sum = 0
for i in num:
    sum = sum + int(i)
print(f"Sum of all the digits of the number {num} is {sum}")