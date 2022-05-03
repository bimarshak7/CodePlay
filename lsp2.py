s = 'I adore it'
words = s.split()

max = max([len(x) for x in words])
t = s[0]
res=''
for word in words:
    d = max - len(word) 
    res+=(t*d+word)+' '
    
print(res)
