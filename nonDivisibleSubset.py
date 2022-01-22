def nonDivisibleSubset(k, s):
    # Write your code here
    r = [0]*k
    for a in s:
        r[a%k]+=1 #update remainder counter
    c = 1 if r[0]>0 else 0
    for i in range(1,k//2+1):
        if (i != k-i):
            c += max(r[i],r[k-i])
        else:
            c += 1
    print(r)
    return c
l1 = [1,7,2,4]  
l2 = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
a=nonDivisibleSubset(7,l2)
print(a)
