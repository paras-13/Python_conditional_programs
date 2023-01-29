n_odd=int(input("Enter the number of odd numbers you want"))
lst = []
for i in range(1,n_odd*2,2):
    lst.append(i)
print(lst)