n=6
x,t,k=' ',1,'#'
""""
for i in range(0,n):
    print(i)
    for y in range(n-1-i, 0, -1):
        print(x ,end='')

    for j in range (1,i+2):
        print("#", end='')
    print("\r")
"""
#çok daha iyi bir çözüm
while n>0:
    print((n-1)*x+t*k)
    n -= 1
    t += 1