arr = [3,2,1,3]
tallest=max(arr)
print(len([x for x in arr if x == tallest]))

#daha iyi bir çözüm :D
print(arr.count(max(arr)))