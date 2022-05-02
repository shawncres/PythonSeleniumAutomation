##class Test:
##    def __init__(self):        
##        self.x = 22
##        self.y = 33
##        self.z = 44
##
##    def mult(self,value):
##        j= value * self.x
##        print(j)
##
##    def listmult(self,numbs):
##
##        newlist = [ k*k for k in numbs]
##        print(newlist)
##
##
##class SubTest(Test):
##    def __init__(self):
##        super().__init__()
##
##    def add(self,value):
##        j= value + self.x
##        print(j)
##
##    def listconst(self,numbs):
##
##        newlist = [ k*self.x for k in numbs]
##        print(newlist)
##
##
##a = SubTest()
##
##
##
##a.mult(5)
##
##
##a.listconst([100,200,400])




class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def operate(self):
        return self.x * self.y


class Ba(A):
    def __init__(self,x,y):
        super().__init__(x,y)




j = Ba(3,4)

print(j.operate())














