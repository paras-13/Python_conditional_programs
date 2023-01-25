# Program that receives two numbers in a function and returns the results of all arithmetic operations( +,-,*,/,%) on these numbers
def arCalc( x , y ) :
    return x+y , x-y , x*y , x/y , x%y
#__main__
num1 = int(input( "enter number 1 :" ))
num2 = int(input("enter number 2:" ))
add, sub, mult, div, mod = arCalc(num1,num2)
print("sum of given numbers:" , add )
print("subtraction of given numbers:", sub )
print("product of given numbers:", mult )
print("division of given numbers:", div )
print("modulo of given numbers:", mod )