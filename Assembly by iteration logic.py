import random


pn = ['12','15','43', '45']
sn = {}
gn = []

##def generate(self):
##    for 
##    r =random.randrange(10, 99, 1)
##    x =random.randrange(10, 99, 1)
##    sn.append(r:x)
##    


for i in pn:
    r =random.randrange(10, 99, 1)
    x = i+str(r)
    gn.append(x)
    sn[i]=x
    


for i in gn:
    if gn[0] != i:
        print(gn[0],i)


parent=gn[0]


print(sn)
print(parent)
print(sn['12'])

##
##print(pn[x])
##print(sn)
