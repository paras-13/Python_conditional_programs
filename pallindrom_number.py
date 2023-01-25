# Write a program to check whether the given number is palindrome or not.
num = int(input("ENTER NUMBER:"))
wnum = num
rev = 0
while( wnum > 0):
    dig = wnum % 10
    rev = rev*10 + dig
    wnum = wnum // 10
if(num == rev):
    print("Number", num,"is a palindrome")
else:
    print("Number", num ," is not a palindrome")