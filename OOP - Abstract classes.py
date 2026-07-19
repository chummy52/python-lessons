# Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed.(They're supposed to be parents to children classes)
#                 They can contain abstract methods, which are declared but have no implementation
#                 Abstract classes benefits:
#                 1. Prevents instantiation of the class itself (we can't create an object from a class that's abstract)
#                                                               (abstract classes are like incomplete, we dont wanna create an object that's incomplete)
#                 2. Requires children to use inherited abstract methods
#                    (any children that inherit from an abstract class, if there's any abstract methods, we have to implement them)

# so let me give you a demonstration:
# we're going to create a class, A Vehicle
# to work with abstract classes, we need to import 'abc' meaning "Abstract Base Classes" and then 'ABC' meaning "Abstract Base Class", and 'abstractmethod'
from abc import ABC, abstractmethod 

class Vehicle(ABC): # so my Vehicle class, it's gonna be a abstract class, we will inherit from ABC
                    # I dont want myself or any other developers to be able to create a vehicle object
                    # I will make Vehicle an abstract class
                    # also I can add some abstract methods 
    @abstractmethod # these methods will be inherited by its children
                    # to declare an abstractmethod, we need to use a decorator (@)
                    # so what should all vehicles be able to do
    def go(self):   # with abstract methods, we declare them but we dont define them
        pass        # we'll define them within each of the children classes that inherit from Vehicle
    
    @ abstractmethod
    def stop(self):
        pass
# okay now we're done with the abstract class
# just to demonstrate that we can't instantiate an object from this class
# let's attempt to do so and see what happens:

#vehicle = Vehicle() # it will be a TypeError: Can't instantiate abstract class Vehicle with abstract methods go, stop
# this is good, our vehicle class is incomplete, we don't want to accidentally make a vehicle object

# now we will create children class, to inherit the abstract class

class Car(Vehicle): # class Car must implement all abstract methods
    # let's see what happens if we ignore it and try to create a car
#    pass
#car = Car() # it will say TypeError: Can't instantiate abstract class Car with abstract methods go, stop
# we would need to define those methods from the abstract class to the children class that inherited it from them

    def go(self):   
        print("you drive the car")    

    def stop(self):
        print("you stop the car")

car = Car()
car.go()
car.stop()

# now when you try to use the methods that the children class inherited from the parent class which is a abstract class
# it will work now because you defined the methods from the abstract class,
# now lets add a few more children for the vehicle class

class Motor(Vehicle):

    def go(self):   
        print("you ride the motorcycle")    

    def stop(self):
        print("you stop the motorcycle")

motor = Motor()
motor.go()
motor.stop()

class Boat(Vehicle):
    def go(self):   
        print("you sail the boat")    

    def stop(self):
        print("you anchor the boat")

boat = Boat()
boat.go()
boat.stop()

# when including abstract methods within a parent, it acts as a set of checks and balances 
# all vehicles should be able to go and stop
# if i forget to define one of these methods, well, we'll receive a TypeError, if it didnt warn me, I wouldnt notice the Error

# okay so that's abstract classes, its a class that can't be instantiated on its own,
# we can't create any objects from this class, we don't want to because it is incomplete
# they're meant to be subclassed, they can contain abstract methods which are declared but we dont finish defining them
# we define them within the children classes, as you can see from the example