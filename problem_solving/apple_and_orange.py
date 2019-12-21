s, t, a, b, m, n, apples, oranges = 7, 11, 5, 15, 3, 2, [-2,2,-1], [5,-6]
countOfApples = len([x for x in apples if x+a in range(s,t+1)])
print(countOfApples)
countOfOranges = len([y for y in oranges if y+b in range(s,t+1)])
print(countOfOranges)