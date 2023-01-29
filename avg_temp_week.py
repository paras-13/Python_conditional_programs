# Program to calculate average temperature of a week
week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
sum = 0
print("Welcome: Proceed to calculate average temperature for this week")
D = {}
for day in week:
    inp = float(input(f"Temperature recorded on {day}"))
    D[day] = inp

for temp in D:
    sum += D[temp]

avg = sum/7
print(f"Average temmperature recorded this week is {avg}")
