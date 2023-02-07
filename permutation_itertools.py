from itertools import permutations
str1,l = input(),int(input())#map(str,input().split(" "))
ls = []
for i in str1:
    ls.append(i)
ls.sort()
str1 = "".join(ls)

lst = list(permutations(str1,int(l)))
for i in lst:
    for j in i:
        print(j,end="")
    print()