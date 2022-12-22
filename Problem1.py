#Program to find length of the string given by the user and add "ing" if length
#of the string is greater than 3 otherwise print the given word as it is

word = input("Enter a word -->")
length = len(word)
if length >3:
    print(word+"ing")
else:
    print(word)