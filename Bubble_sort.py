# Program to sort a list using bubble sort.

alist = [15,6,13,22,3,52,2]
print("original list is:",alist)
n = len(alist)
for i in range(n):
    for j in range(0,n-i-1):
        if alist[j] > alist[j+1]:
            alist[j],alist[j+1] = alist[j+1],alist[j]
print("list after sorting:",alist)