# what is encapsulation?
    # encapsulation is the process of hiding the details of a class.


class test:
    def __int__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return 'This is a test class'

class test1:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return 'This is a test1 class'

class final:
    def __init__(self,test,test1,test2):
        self.test = test
        self.test1 = test1
        self.test2 = test2

    def __str__(self):
        return '\n' + str(self.test) + '\n' + str(self.test1) + '\n' + str(self.test2)


t = test(1,2,3)
t1 = test1(4,5,6)
t2 = final(5,6,7)
f = final(t,t1,t2)