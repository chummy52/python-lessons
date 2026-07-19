# now let's move on to multiple inheritance


# Multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# Multilevel Inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

# so first let's talk about multiple inheritance
# so in this example, im gonna create two parent classes:
class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

# ---------------
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): # now if you study science, fish also hunt fishes, only those that are smaller than them and also they are prey to other predators
    pass
# ---- and these are gonna be the children classes

# now let's see if this does in fact work, we'll create objects for the animals

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# now let's check their methods
rabbit.flee()
# you will get a Attribute Error if you put a method that the children classes doesnt have because it doesnt inherit the attributes and methods from a parent class
rabbit.hunt()
hawk.hunt()
hawk.flee()
fish.flee()
fish.hunt()
# the fish inherits both of the attributes of the 2 parent classes, so they have the attributes and can use the methods of both parent classes

# children classes can inherit from more than one parent class which is what we did for fish class

# now moving on with multi-level inheritance, a parent can inherit from another parent
# let's add a class of Animal
class Animal:
    def __init__ (self, name): # let's define a constructor
        self.name = name

    def eat(self):
        print(f"  {self.name} is eating")
    def sleep(self):
        print(f"  {self.name} is sleeping")

    
# --------------------------------------------        

class Prey(Animal): # so prey are going to inherit from the animal class, so we need to add the Animal to each inheritance list
    def flee(self):
        print(f" {self.name} is fleeing")

class Predator(Animal): #so predator are going to inherit from the animal class, so we need to add the Animal to each inheritance list

    def hunt(self):
        print(f" {self.name} is hunting")

# ---------------
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): 
    pass

# so basically its like this, the rabbit, hawk, and fish class are the children, and they inherited
# the attributes and methods from their parent classes, Predator and Prey, and the Parent classes inherited
# the attributes and methods from their grandparent which is the Animal class
# so like Grandparent <- Parent <- Children

# now let's try to use the methods of the Animal class with the children classes that were inherited from the parent classes because the parent classes inherited
# as well the attributes and methods of the Animal class which is their grandparent

#let's put names on our animals
rabbit = Rabbit("Bugs")
hawk = Hawk("Eye")
fish = Fish("Nemo")
# ---------------------------
rabbit.flee() # no rabbit.hunt()
hawk.hunt() # no hawk.flee()
fish.flee() 
fish.hunt()
# ---------------------------
# methods that came from grandparent class
rabbit.eat()
rabbit.sleep()

hawk.eat()
hawk.sleep()

fish.eat()
fish.sleep()

# so that's how it is this is what Inheritance is and the Types of it thankss