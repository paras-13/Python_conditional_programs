# Factorial of a number
a=1
def factorial(num):
    global a
    if num!=0:
        a=a*num
        factorial(num-1)
    return a
num = int(input())
print(factorial(num))