a=20

while True:
    for i in range(2,21):
        if a%i!=0:
            a+=1
            break
    if i==20:break
print(a)
