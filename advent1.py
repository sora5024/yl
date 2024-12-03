f = open('example.txt' , 'r')

lines = f.readlines()

list1 = []

list2 = []

res = 0

for line in lines:
    a ,b = line.strip().split()
    list1.append(int(a))
    list2.append(int(b))

list1.sort()
list2.sort()

for i in range(0 , len(list1)):
    res += abs(list1[i] - list2[i])

print(res)

