def time(s):
    p = s[-2]
    if p=='A':
        if s[:2]=='12':
            t = '00'+s[2:-2]
        else:
            t = s[:-2]
    else:
        if s[:2]=='12':
            t = s[:-2]
        else:
            t = str(int(s[:2])+12)+s[2:-2]
    return t

s= time('12:01:00AM')

print(s)
