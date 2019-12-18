arr = [3,2,1,3]
tallest=max(arr)
print(len([x for x in arr if x == tallest]))

#better solution
print(arr.count(max(arr)))