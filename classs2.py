class Rectangle:
    def __init__(self, length, width):
        self.set_length(length)
        self.set_width(width)

    # def area(self):
    #     return self.length*self.width

    def get_length(self):
        return self._length
    
    def set_length(self, length):
        if length>0:
            self._length = length
        else:
            print("Length must be positive!")
    def get_width(self):
        return self._width
    
    def set_width(self, width):
        if width>0:
            self._width = width
        else:
            print("width must be positive!")
    
    def area(self):
        return self.get_length() * self.get_width()
    
rect = Rectangle(5, 3)

rect.set_length(-2)
rect.set_width(-4)

print("Area of the rectangle: ", rect.area())