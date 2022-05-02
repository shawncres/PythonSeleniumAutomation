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


##test 2
##
##class A:
##    def __init__(self,x,y):
##        self.x = x
##        self.y = y
##
##
##    def operate(self):
##        return self.x * self.y
##
##
##class Ba(A):
##    def __init__(self,x,y,z):
##        super().__init__(x,y)
##        self.z = z
##
##    def newoperate(self):
##        return self.operate() + self.z
##
##
##j = Ba(3,4,5)
##
##print(j.newoperate())
##
##
##
##



## test 3
##
##class maintest:
##    def __init__(self):
##        self.x = 50
##
##
##
##class subtesta(maintest):
##    def __init__(self):
##        super().__init__()
##
##class subtestb(maintest):
##    def __init__(self):
##        super().__init__()
##        self.a = 100
##
##    def multiply(self):
##        return  self.x * self.a
##
##class subtestc(maintest):
##    def __init__(self,value):
##        super().__init__()
##        self.value = value
##
##    def listcomp(self):
##        newlist = [self.x * k for k in self.value]
##        print(newlist)
##
##
##    
##
##j = subtestc([1,5,10])
##
##
###print(j.multiply())
##
##j.listcomp()
##        
##
##j = subtestb()
##
##print(j.multiply())
##


class human:
    def __init__(self):
        self.height = 50
        self.weight = 100

    def greeting(self):
        print('Hi I\'m a human being')

    def stats(self):
        print(f'I am {self.height}cm tall and weight {self.weight}kg')

class child(human):
    def __init__(self):
        super().__init__()        
        print('I am a child')
        self.height = self.height /2
        self.weight = self.weight /2





john = child()


john.greeting()

john.stats()

        
        




