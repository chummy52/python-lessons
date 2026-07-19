# Polymorphism = Greek word that means to "have many forms or faces"
#                Poly = Many
#                Morphe = Form

#                Two Ways to Achieve Polymorphism 
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck Typing" = Object must have necessary attributes/methods

# Polymorphism is a programming concept, in programming, an object can take one of many forms

# let's focus first on Inheritance because we'll discuss "Duck Typing" in the next lesson
# so first let's create a class of Shape

from abc import ABC, abstractmethod
class Shape:
    #lets say with our shape class, we will define an area method
    @abstractmethod
    def area(self): # im gonna turn this into an abstract method
        pass        # Circle, Square, and Triangle are all considered as Shapes, they inherit from this class
                    # we need to define an area for each since they're all considered as Shapes, every shape has an area

class Circle(Shape): # what attributes does this shape have?
    def __init__(self, radius):
        self.radius = radius
    
    def area(self): 
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, sides):
        self.sides = sides

    def area(self): 
        return self.sides ** 2
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self): 
        return self.base * self.height * 0.5
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        #self.radius = radius # since radius method is in the parent class, u just have to use a super function instead of writing it
        super().__init__(radius)
    # now within my list of shapes, i will add a pizza object
    # but when i run it it doesnt have an area method so it will come out as an error 
    # it will say that the Pizza object has no attribute 'area'
    # our pizza is considered as a pizza but it is not considered a shape so it doesnt inherit the methods from the parent class like what the other children classes have - shapes
    # well a pizza is considered a circle so what if we make it inherit the circle class
    # then it will be considered as a shape now HAHAHAHAHAHAA cause a pizza is considered a circle and a circle is considered a shape , since Pizza was considered as a circle, it will be considered as a shape as well
    # so now This class has 3 forms HAHAHAHAHAHA

#circle = Circle() # A circle is a circle, the circle is also considered as a shape, but out circle is not a square nor a triangle, it is a circle and it is also considered as shape
#square = Square() # a square is a square, the square is also considered as a shape, but our square is not a circle nor a triangle, it is a square and it is also a shape
#triangle = Triangle() # A triangle is a triangle, the triangle is also considered as a shape, but our triangle is not a square nor a circle, it is a triangle but it is also a shape

# so we have 2 possible forms for each shape

# so let's say we would like to create a list of shapes, what do they all have in common?
# well, they're all shapes, a descriptive name for this list would be:
shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pineapple", 49)]# i will instantiate these objects
# our circle is a circle and a shape
# our square is a sqaure  and a shape
# our triangle is a triangle and a shape
# each of the objects in the list has two forms
# let's fill in the classes of the children and let's go back here afterwards......

# I'm going to write a loop to iterate through our shapes. this is from the list
for shape in shapes:
    #print(shape.area())
    print(f"{shape.area()}cm^2")
# if you would like, you can format the output

# okay what if we made a class that is completely unrelated to shapes
# now that's done

# so that's the concept of Polymorphism HAHAHAHAHA 
