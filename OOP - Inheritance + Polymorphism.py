# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

# by having a class inherit attributes and methods from another class
# this helps with code reusability and extensibility
# in this example: we're going to create an animal class
# the dog, cat, and mouse class, will inherit attributes and methods from the animal class:

# we will create a class of animal
class Animal:
    # then i will define the constructor
    def __init__(self, name): # let's pass in a name, although its not required but it might be good for this example
        self.name = name
        self.is_alive = True
    #all animals can eat
    def eat(self):
        print(f"{self.name} is eating")
    
    # all animals can sleep
    def sleep(self):
        print(f"{self.name} is sleeping")
    
# that's all that we need for the Animal Class ( this will be the main class)
# let's now move on to the Dog class
# now inorder for this class to inherit the attributes and methods of the Animal class we need
# to add an "inheritance list" with the set of parentheses
class Dog(Animal): # and then list the name of the class you want this class to inherit
   def speak(self):
       print("woof")
   # for the time being as a placeholder, ill add a pass

class Cat(Animal):
    def speak(self):
        print("meow")

class Mouse(Animal):
    def speak(self):
        print("squeek")

# okay so now we'll create objects for each animal
dog = Dog("Max")
cat = Cat("Sebastian")
mouse = Mouse("Mickey")

# okay let's first start printing the dog's name and if it's alive
print(dog.name)
print(dog.is_alive)
# let's have our dog object use the eat() method
dog.eat()
dog.sleep()
dog.speak()
# okay, let's do the same for the other animals
print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
mouse.speak()

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
mouse.speak()

# even though the "children" classes are empty, we're still inheriting the attributes and methods of the Parent Class
# this is convenient because you dont need to copy and paste, these attributes and methods for every single class
# it still works if u copy and paste that but its a lot of code to write tbh and it takes a lot of space
# but if you want a certain class to do a specific action and dont want the other classes to do the same, then you can add a method to the children class

# and lastly class Child(Parent), i only made it like that so u would understand better
# but it is also know as class Sub[Child] (Super)[Parent]