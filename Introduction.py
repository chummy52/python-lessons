# this is the full course so this will be longer than ever

# object = a "bundle" of related attributes (variables) and methods (functions)
#          Ex: "look around your surroundings and list what u see." mine's a phone, cup or a book
#                                                                           each of these objects can have different attributes to represent it
#                                                                           Ex: an attribute of the phone next to me could be a version number -> "version_num = 13"
#                                                                                                                                                i could set that to be 13 (what version is the phone?)
#                                                                                                                                         another attribute -> is_on = True ( is the phone powered on or not?)   
#                                                                                                                                   or even a price -> price = 567.69
#          Hmm what about the cup next to me, -> liquid = "coffee" (what liquid is within my cup?)
#                                             whats the temperature of the coffee? -> temp = 76.4
#           
#          Or even a book, -> title = "Tom and Jerry" (whats the title of the book?)
#                             pages = 252 (how many pages does the book have?)


# now objects have the capability to do things, they have 'methods', which are functions that belong to an object 
# people are confused between methods and functions, they're technically different, a method is a function that belongs within an object

# what are some actions these objects can perform?
# lets say with a phone, you can make a call, receive a call, turn on and off a phone
# ex:                             ex: with a cup:                ex: with a book:
    # def make_call():...             def fill_cup():...             def open_book():...

    # def receive_call():...   ->     def drink_cup():...   ->       def read_book():...

    # def turn_on():...               def empty_cup():...            def close_book():...

    # def turn_off():...
# those can all be functions


# an object is a "bundle" of related attributes and methods they can represent real world items,
# to create many objects
# you would need a "class":                                                                                  
# a class is a type of blueprint

# class = (blueprint) used to design the structure and layout of an object
# we need to design what out objects have, their attributes and what they can do (methods)

# we will create a class of car
# we will create some car objects
#class car:
    # to construct a car object, we need a special type of method called a "constructor" (keep that in mind)
    # it works similarly to a function
    # we will define a function of double underscores init (init means initialize) and follow it with a set of parentheses
    #def __init__(): # this is our constructor method, we really need this method in order to construct objects
                        # its a 'Dunder' method - meaning double underscore __init__
                        # this method behaves similar to a function
                        # we need to set up the parameters
#    def __init__(self, model, year, color, for_sale): # self means this object we're creating right now (this car)
                        # so what are some attributes a car should have (model - could be a string like a BMW; a year; a color; hmm let's add a boolean -> for_sale)
        # inorder to assign these attributes, we're going to access 'self' -> self."the name of the attribute" = the attribute we receive
#        self.model = model
        # (self, model, year, color, for_sale): these are parameters, when we receive let's say the name of the model,
        # we will assign it to an object, let's do this with the other parameters
#        self.year = year
#        self.color = color
#        self.for_sale = for_sale # A boolean
        # this is an example of a few attributes that a car might have

from car import Car # if you would look back here hehe
# now to construct a car object, we need a unique name for this car | car1 = "take the name of the 'class'" and add set of parentheses to invoke the constructor
car1 = Car("ferrari", 2020, "black", True) # we're going to do this almost exactlty like a function,
             # we have parameters set up, we need to send a matching number of arguments,
             # 'self' will be provided to us behind the scenes automatically, if not, just put it first within the set of parentheses
# let's see what happens if i attempt to print our car object
#print(car1) # what we will receive will be a memory addresss of this car object, where it's located
            # but i would like one of the attributes located at this memory address
            # instead of printing the object itself, we're going to access one of the attributes found within this variable(car1)

# we will follow the name of the 1 with a DOT ( . ) and this is known as the "attribute access operator"
print(car1.model) # i would like the model of the car1, so i would need to put the attribute from the object
# what about the other attributes:
print(car1.year)
print(car1.color)
print(car1.for_sale)

# now let's create a second car, we will reuse the class "car" for this

car2 = Car("Bugatti", 2025, "purple", False)
# instead of accessing car1's attributes, we're gonna access car2's attributes
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

# or even a 3rd car
car3 = Car("BMW", 2023, "grey", True)
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

# with classes, they can take up a lot of space, for better organization, you can place them within a new python file
# so we can cut our class and place it to the new file
# so from out main python file, we're going to import our car file, our car module, from the name of the module car import
#from car import car
# now this saves a lot of space from the previous one as long as the file exists like the file for the class
# i should put this before the variables and their attributes mentioned
# you could keep ur classes within ur main python file, or import them if you would like to organize things


# now after attributes, let's talk about methods
# methods are actions that our objects can perform
# let's go back to the car.py, and come back here after you read it
# after reading it, let's take a variable acccess the 'drive' method
car1.drive()
car2.drive()
car3.drive()
#what about the stop
car1.stop()
car2.stop()
car3.stop()
# (def drive(self) ; def stop(self)) - these methods are identical for each car object
# instead of printing the word car, let's inset the model of the car to the functions. come back here after reading what happened in the car.py file
# now after adding placeholder for the functions and adding the self. and the name of the attribute
# when we print the variables again, it will say the name of the car or the model of the car:
# self. is referring to the object we're currently working with, use the attribute access operator, followed by the name of the ttribute
# you can also add multiple placeholder in a function if you want
# let's add another function where we describe our car,
# after adding that, i will access the new function with the variables

car1.describe()
car2.describe()
car3.describe()


# so Yeah those are objects in python, This is the introduction to OOP so expect more lessons to come







