''' Scientific Computing with Pyton - Polygon Area Calculator'''

# shape_calculator_v0.py

# In this project you will use OOP to create a Rectangle class and a Square class. 
# The Square class should be a subclass of Rectangle and inherit methods and attributes.

class Rectangle:
    # When a Rectangle object is created, it should be initialized with width and height attr.
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        ret_str = ''
        if self.width > 50 or self.height > 50:
            ret_str = 'Too big for picture.'
        else:
            for ln in range(self.height):
                for col in range(self.width):
                    ret_str += '*'
                ret_str += '\n'
        return ret_str

    def get_amount_inside(self, shape):
        # wval = self.width // shape.width
        # print(wval)
        # vval = self.height // shape.height
        # print(vval)
        # return wval * vval
        return (self.width // shape.width) * ( self.height // shape.height)

    def __str__(self):
        ret_str = ('Rectangle(width=' + str(self.width) +
                    ', height=' + str(self.height) + ')')
        return ret_str


class Square(Rectangle):
    def __init__(self, side):
        #super().__init__(side, side)
        Rectangle.__init__(self, side, side)
        self.side = side

    def set_side(self, side):
        #Rectangle.set_width(self, side)
        super().set_width(side)
        Rectangle.set_height(self, side)

        self.side = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return 'Square(side=' + str(self.side) + ')'



rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
            



    
    
