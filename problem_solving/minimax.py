"""
import sys
arr = [1, 2, 3, 4, 5]
maximum, minimum, total = 0, sys.float_info.max, 0
for j in range(0, 5):
    for i in range(0,5):
        if i != j:
            total += arr[i]
    if total > maximum:
        maximum = total
    if total < minimum:
        minimum = total
    total = 0
print (minimum,maximum)
"""
#çok daha iyi bi çözüm
arr = [2, 1, 3, 4, 5]
s=sum(arr)
print(s-min(arr),s-max(arr))