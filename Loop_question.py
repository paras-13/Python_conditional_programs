# Using a for loop and .append() method append each item with a Dr. prefix to the lst.

list1=["Phil", "Oz", "Seuss", "Dre"]
for i in range(len(list1)):   
    list1[i] = "Dr."+list1[i]                             #Lists are mutable
print(list1)


