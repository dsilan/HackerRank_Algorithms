import numpy as np
arr=np.array([[11, 2, 4],[4, 5, 6],[10, 8, -12]])

x=0
y=0
n = len(arr)
for i in range(0,n):
    x += arr[i][i]
    y += arr[i][n-i-1]
print(abs(x-y))