import math
import random
n=9
print("array:")
#arr = [random.randint(0, 20) for k in range(0, n)]
arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
#print(arr)
counts = 0
i=0
while n > 0:
    if arr[i] > 0:
        countOfNumber = arr.count(arr[i])
        if (countOfNumber % 2) == 0: 
            counts += countOfNumber / 2
        else:
            counts += (countOfNumber - 1) / 2
        value = arr[i]
        for j, r in enumerate(arr):
            if r == value:
                arr[j] = -1
    i += 1
    n -= 1


#print(int(counts))



n = 9
l = [10, 20, 20, 10, 10, 30, 50, 10, 20]
s = set(l)
p = 0
for i in s:
    p += len([x for x in l if x == i])//2
print(p)
