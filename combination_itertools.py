from itertools import combinations
st,n = input(),int(input())
n = int(n)
lst = []
ls = []
for i in st:
    ls.append(i)
ls.sort()
st = "".join(ls)
for i in ls:
    print(i)
lst = list(combinations(st,n))
for j in lst:
    s=""
    for k in range(n):
        s += j[k]
    print(s)