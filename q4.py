k = int(input())
v = [str(x) for x in range(k+1)]
# print(v)
c=0
f=0
for i in range(1000,10000):
	s = list(str(i))
	for x in s:
		if x not in v or s.count(x)!=2:
			f=1
			break
	if f==1:continue
	f+=1
	if i%11==0:
		print(s)
		c+=1

print(f)