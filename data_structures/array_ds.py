arr = [1, 4, 3, 2]
arr.reverse()
print(arr)

#without using reverse function
for i in range(len(arr)-1,-1,-1):
    print(arr[i], end=' ')