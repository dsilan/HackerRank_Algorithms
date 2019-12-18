total = 1
number_of_valleys=0
s = ['U','D','D','D','U','D','U','U']
#total += len([step for step in s if step == 'U'])
#total -= len([step for step in s if step == 'D'])
for step in s:
    if step == 'U':
        total += 1
    elif step == 'D':
        total -= 1 
    if total == 1 and step == 'U':
        number_of_valleys += 1

ar = [1, 2, 3]
print(number_of_valleys)

t = sum(int(i) for i in ar)
print(t)

import numpy
sm = numpy.sum(ar)
print(sm)


print("big num")
arr = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
suum = sum(int(it) for it in arr)
print(suum)