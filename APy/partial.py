from functools import partial
def f(x,y,z):
    return x*11+y*22+z*33

p = partial(f,2,3)

x=p(4)
print(p.args)

