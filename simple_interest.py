# Program to calculate simple interest
""" Program to calculate simple interest using a function interest() that can receive
 principal amount , time and rate and returns calculated simple interest. Do specify
 default values for rate and time as 10% and 2 years respectively """

def interest(principal, time = 2 , rate = 0.10):
    return principal*rate*time
#__main__
Prin = float(input("Enter principal amount:"))              # At default values
print("Simple interest with default ROI and time value is:")
Si1 = interest(Prin)

Roi = float(input("Enter rate of interest (ROI):"))            # At variable values
time = int(input("Enter time in years:"))
print ("Simple interest with your provided ROI and time value is:")
Si2 = interest( Prin, time, Roi/100)
print("Rs.",Si2)