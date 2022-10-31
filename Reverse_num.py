# Program To reverse a two digit or three digit number

num=int(input("Enter a two or three digit number"))          # User provides a number
sum=0
if len(str(num))==2:
    for i in range(2):
        rem=num%10
        sum=sum*10+rem                                       # For two digit number
        num=num//10
    print(sum)
elif len(str(num))==3:
    for i in range(3):
        a = [100, 10, 1]
        rem=num%10                                           # For three digit number
        sum=sum+rem*a[i]
        num=num//10
    print(sum)
else:
    print('Only allows two or three digit numbers')