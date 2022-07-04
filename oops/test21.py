 # what is abstraction in python?

    # abstraction is a way to hide the implementation details of a program


class test:
    def __init__(self,a,b,c,d):
        self.__a = a  # private variable is a variable that is not accessible from outside the class
        self.b = b    # _a is a variable that is accessible from outside the clas   
        self.c = c
        self.d = d    # __a is a private variable that is not accessible from outside the class

    def test_custom(self,v):
        return v - self.__a 

    def __str__(self):
        return 'This is a test class'


o = test(1,2,3,4)

print(o.test_custom(10))

#print(o._a)

#print(o.__a)

print(o._test__a) 

# this is a private variable that is not accessible from outside the class
# we can use the following method to access the private variable
#print(o._test__a)


# inheritance in python

# what is inheritance in python?

    # inheritance is a way to create a new class from an existing class

    # inheritence is used to access the variables and methods of the parent class



class test1(test):
    def __init__(self,j,*args):
        super(test1,self).__init__(*args)
        self.j = j 

# here we are creating a new class from the existing class test

# what is the use of super() in python?

    # super() is used to access the variables and methods of the parent class

# test1 is a child class of test.


# super(test1,self) acts as a reference to the parent class test

m = test1(1,2,3,4,5)
print(m.b)
print(m.j)
print(m._test__a)

print(m.test_custom(55))

