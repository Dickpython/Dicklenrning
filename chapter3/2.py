# 定义一个名为Shape的类及其子类Square。 Square类具有一个init函数，该函数以长度作为参数。这两个类都有一个Area函数，该函数可以打印Shape的区域默认为0的形状的区域。
class Shape(object) :
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,lenth_1):
        Shape.__init__(self)
        self.length = lenth_1
    def area(self):
        return self.length * self.length

square_1 = Square(3)
print (square_1.area())
