# Program that readsa number in feet and convert tometres

val = float(input("Enter your measurement in feet"))
# 1 feet = 0.305 metres
metre = val*0.305
print(f"{val} feet is {metre} metres")