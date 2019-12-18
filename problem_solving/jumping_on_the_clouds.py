s=[0, 0, 1, 0, 0, 1, 0]
a=[0, 0, 0, 0, 1, 0]
ns = 7
na = 6
c=0
jump = 0
while c < na-1:
    if(c+2 < ns and a[c+2]==0):
        c += 2
    else:
        c += 1
    jump += 1
print(jump)