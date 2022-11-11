# Program to display all prime numbers within a range
# Take the user input for start and end of range.
start= int(input("Enter a number from where you want start the range"))
end = int(input("Enter a number at where you want to end the range"))
for i in range(start,end+1):
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i,end = ",")