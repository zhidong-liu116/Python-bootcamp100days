# Write your code above 👆
with open("file1.txt") as f:
    #lst1 = [int(x) for x in f.read().split()]
    lst1 = []
    for i in f:
        lst1.append(int(i))

with open("file2.txt") as f:
    lst2 = [int(x) for x in f.read().split()]

result = [nums for nums in lst1 if nums in lst2]

print(result)
