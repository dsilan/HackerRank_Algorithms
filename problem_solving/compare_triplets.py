a=[17, 28, 30]
b=[99, 16, 8]

def compare(a,b):
    point=[0,0]
    for (i,j) in zip(a,b):
        if i > j:
            point[0] += 1
        elif i < j:
            point[1] += 1
        else:
            pass
    print(point)

compare (a,b)