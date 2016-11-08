class Test(object):

    common = "Human Being"

    def __init__(self,name):
        self.name = name


    def __str__(self):
        return self.name


    def rename(self,renamed):
        self.name = renamed


a = Test('ovi')
b = Test('omi')


print a.common, b.common

print a.name, b.name

a.rename('bangla')

b.rename('bangladesh')


print a.name, b.name


Test.rename(a, "bangladesh")

print a.name, b.name


multiplier = 3

class D:

    multiplier = 2

    @classmethod
    def f(cls, x):
        return cls.multiplier * 2

    
    @staticmethod
    def s(x):
        return multiplier * 2


d = D()

print "calling with classname"
print D.f
print D.s

print "calling with classobject" 

print d.f
print d.s


print d.f(20)
print d.s(20)


print "----------------->"

print D.f(20)
print D.s(20)


class Rectangle(object):

    def __init__(self, h, w):

        self.height = h
        self.weight = w

    def area(self):
        return self.height * self.weight

    def perimeter(self):
        return 2 * (self.height + self.weight)


class Square(Rectangle):

    def __init__(self, s):
        super(Square, self).__init__(s,s)
        self.length = s

    @staticmethod
    def extra():
        return "This method has no purpose" 


print Square(2).area()

print Square(2).extra()


print issubclass(Square, Rectangle)

print isinstance(Square(2),object)
