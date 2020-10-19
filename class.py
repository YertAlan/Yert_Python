'''

class C1:
    def __init__(self,who):
        self.name=who



I1 = C1('Bob')
I2 = C1('Yert')

print(I1.name)
print(I2.name)
'''

class FirstClass:
    def setdata(self,value):
        self.data = value
    def display(self):
        print(self.data)

x=FirstClass()
y=FirstClass()


x.setdata('Yert.Alan')
y.setdata(3.14)



x.display()
y.display()

class SecondClass(FirstClass):
    def display(self):
        print('Value = "%s" ' % self.data)


z = SecondClass()
z.setdata(42)
z.display()



class ThirdClass(SecondClass):
    def __init__(self,value):
        self.data = value
    def __add__(self,other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirdClass:%s]' % self.data
    def mul(self,other):
        self.data *= other


a = ThirdClass('abc')
a.display()
print(a)



b = a + 'xyz'

b.display()
print(b)


a.mul(3)
print(a)
