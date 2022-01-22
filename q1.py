n = int(input())
l = input().rstrip().split()
l = [int(x) for x in l]
s=l.copy()
s.sort()
pos = int(input())
el = l[pos-1]
print(el)
ind = s.index(el)
print(ind+1)

