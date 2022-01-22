# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = input()
y = map(int,input().split())
y = Counter(y)
N = int(input())
c=[]
for i in range(N):
    x = list(map(int,input().split()))
    c.append(x)

t=0
for i in c:
    print(i)
    if(y[i[0]]):
        t+=i[1]
        y[i[0]]-=1
print(t)