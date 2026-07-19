# module - a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up large program reusable separate files

#help("modules") # this is for the list of all the modules found within the standard python library
                # you would need to pass in the word "modules"

# if you put the name of the modules in the help function, it would give you all of the functions 
# and variables of that certain module
#help("math")

# to include a module, we would need to type import
#import math # this would give us access to the variables and functions of this module
# we could also use some alias for the module like a nickname if you have a long module name and want to shorten it but still works the same
#import math as m
#print(math.pi)
#print(m.pi)

# another way to import is to use 'from' the name of the module, and then something specific
#from math import pi # in this case, you wont need the module name anymore
# but it's advised to not use the from import cause it might cause some name conflicts espcially when making large programs with multiple lines of codes
#print(pi)

# now to create a module, we would need to create a new python file and think of a module name nad create functions and variables there

import example # now we have access to everthing in the module that we just created
print(example.square(6))

result = example.pi
print(result)

print(example.cube(5))

print(example.circumference(4))

print(example.area(5))

# so yeah that's how you use a module and how to make a module on your own 