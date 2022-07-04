# is multiple inheritence is possible in python?
#     # yes

# give me the example of multiple inheritance in python


class test:
    def a(self):
        print('test')


class test1:
    def a(self):
        print('test1')

class test2(test,test1):
    def a(self):
        test.a(self)
        test1.a(self)

obj = test2()
obj.a()