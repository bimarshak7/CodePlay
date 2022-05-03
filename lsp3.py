def encode(s):
    c=0
    prev=s[0]
    out = ''
    for a in s:
        if(prev==a):
            c+=1
        else:
            out+=str(c+2)+prev
            c=1
            prev=a
    out+=str(c+2)+prev
    print(out)
    return out
def decode(s):
    out = ''
    for i in range(0,len(s)-1,2):
        out+=s[i+1]*(int(s[i])-2)
    print(out)

s = input("Enter string to encode: ")
en = encode(s)
decode(en)
