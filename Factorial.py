#Factorial of a number
number = int(input("Enter a number for which you want to find the factorial -->"))
fact = 1
for i in range(1,number+1):
    fact*=i
print(fact)

print()
print("------------------------------------------------")
print("Using Recurrsion")
print("---------------------------------------------")
print()
# Factorial of a number using recurssion
a=1
def factorial(num):
    global a
    if num!=0:
        a=a*num
        factorial(num-1)
    return a
num = int(input("Enter a number for which you want to find the factorial -->"))
print(factorial(num))