w1 = input()
w2 = input()
l1 = len(w1)
l2 = len(w2)
d = abs(l1-l2)
if l1>l2:w2=w2+"0"*d
if l2>l1:w1=w1+"0"*d
print("diff",d)

c=0
print("LNES",len(w1),len(w2))
for i in range(len(w2)):
	if w1[i]!=w2[i]:
		c+=1
		print(w1[i],w2[i])
print(c)