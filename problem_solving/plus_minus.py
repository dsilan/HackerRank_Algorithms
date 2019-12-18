arr = [0,1,-1,-1,1]
r_positive = 0
r_negative = 0
n=len(arr)
for i in arr:
    if i>0:
        r_positive += 1
    elif i<0:
        r_negative += 1
    else:
        pass
print("{:f},{:f},{:f}".format((r_positive/n), (r_negative/n), (n-(r_negative + r_positive))/n))