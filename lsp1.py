def ch(x,y):
    while(y<=x):
        if x==y:
            return 1
        y*=y
    return 0
print(ch(256,8))
