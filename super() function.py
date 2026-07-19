# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

# the Parent class is the Super Class | class Super
# The Child class is the Sub Class | class Sub(Super)

# here's an example: we'll create a few shape objects
# we ned to set up the classes though
# for each of these classes inorder to instantiate objects we'll need to a constructor
#-----------------
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
#----------------
# let's create a method that describes the shape
    def describe(self):
        print(f" It is {self.color} and {'filled' if self.is_filled else 'not filled'}") 
        # so each of the class children will have this describe method since it came from the parent class which is the superclass
#-----------------
# we also have method overwriting, what if we create a similar method to describe within circle, square, and triangle
# but we will do this in the children classes because each class have different attributes
#------------------
class Circle(Shape):
    def __init__(self, color, is_filled, radius): # what attributes should a circle should have | color, is it filled our not False if not True if yes, and a radius
        #self.color = color
        #self.is_filled = is_filled
        super().__init__(color, is_filled)
        self.radius = radius
    
    def describe(self):
        super().describe()
        print(f" this Circle is {self.color}, it is {'filled' if self.is_filled else 'not filled'} and it has a radius of {3.14 * self.radius * self.radius}cm^2")
        # this is called method overwiting, although same ang function na nandon sa parent, pero pag ni access mo na yung method for a shape, yung function na nasa loob ng children class although same name as the function from the parent, will be followed
        # if you would like to extend the functionality of a method from a parent, you can use the super() function
    #----------------------
    # not only i want to use the describe method of the child, i would also like to use the describe method of the parent
    # so within a method of a children class, we will use the super() function, to access the describe method of the parent class and not only the children class
    #-----------------------
        #super().describe() # what we're doing is extending the functionality of the describe method
    #-----------------------
class Square(Shape):
    def __init__(self, color, is_filled, width): 
        #self.color = color
        #self.is_filled = is_filled
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f" this Square is {self.color}, it is {'filled' if self.is_filled else 'not filled'} and it has an area of {self.width * self.width}cm^2")
        

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height): 
        #self.color = color
        #self.is_filled = is_filled
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f" this Triangle is {self.color}, it is {'filled' if self.is_filled else 'not filled'}, and with an area of {self.width * self.height / 2}cm^2")
        
# there are a lot of similar attributes between the shapes, lets make a parent class first
# after defining the methods from the parent class, since the children class inherited the attributes and methods from the parent class
# we don't need to re-write the methods that already existed and inherited from the parent class
# so now within the constructor of the children classes, we have to call the constructor for the parent class, also known as the superclass
# and thats where the super() function comes super(). and call the constructor of the parent
# we'll let super() function handle the attributes that all of these types of shapes have in common and then only put the attributes that shapes dont have in common 

# now let's create objects for these shapes
# we can add keyword values for clarity and that we won't have to mind the positional arguments
circle = Circle(color ="red", is_filled = True, radius = 29.9)
square = Square(color = "blue", is_filled = False, width = 15.4)
triangle = Triangle(color = "yellow", is_filled = True, width = 25, height = 30)

# let's try to print them
print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

print(square.color)
print(square.is_filled)
print(f"{square.width}cm")

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")

circle.describe()
square.describe()
triangle.describe()

# as you can see it works, super() function is much more convenient, 
# it kinda saves up space as well, and it helps us to not always repeat our codes as much as possible
# okay guys so that's super() function, it is associated with the superclass or the Parent class