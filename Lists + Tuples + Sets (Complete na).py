# Collections - single "variable" used to store multiple values
# Lists - [] ordered and changeable. Duplicates OK
# Set - {} unordered and immutable(fixed), but Add/Remove OK. NO Duplicates
# Tuple - () ordered and unchangeable. Duplicates OK. FASTER

#let's say we have a variable here:
#prutas = "mansanas" 
#then i can print the variable
#print(prutas)

# i could turn the variable "prutas" into a collection by surrounding my values
# with either a set of square brackets for "Lists", curly brackets for "Set"
# or a set of parentheses for "Tuple"

# Lets begin with the Lists, if i would like to store multiple values inside
# of a variable, i would surround my values with a set of square brackets

prutas = ["apple", "pineapple", "papaya"]
#print(prutas) # this would return all of the values in the variable
#print(prutas[0]) # we can access certain elements inside of a collection, with index operator
                 # we will use square brackets
# and that should only print the specific element in the collection 
# if we access an element that is out of range, we will be greeted by an index error

# as you already know index operator have 3 indices, a beginning, an end, and a step
# this is the same when you are handling with strings previously

#print(prutas[0:2:]) # [start : end : step], so here i assigned a beginning and a end
#print(prutas[::2]) # and here i only assigned a step idex which skips certain elements
                   # its like counting but skipping numbers

# we can also use a for loop for this, this just iterates the collection 
#for x in prutas:  #  for every "you can name this anything" its just preference or for readability "in" "the collection"
#    print(x) 

# So other than that, what are the other methods that we can use with collections?
# to list the different methods, we can use the dir() function

#print(dir(prutas)) # just have to put the name of the collection and print it
# we have attributes at the early part of the list that we have not explained explained yet, \
# but at the end of the list, there are the methods that you are probably familiar if you have read the Python Lists + list Methods file first where we used all of it except the attributes

# if you want descriptions with the methods cause its time consuming to find the file everytime you want to know their descriptions
# just use this | help(the collection that you selected)) |

# let's say you need the length of how many elements are within a collection
# there is the length function | len() | 
#print(len(prutas))

#Using the "in" operator, we can find if a value is within a collection
#this will return a boolean statement only
#print ("apple" in prutas) # is the element "apple" in the "prutas" collection?
# this is used to find if a value is in a list, this applies to other collections

#like the previous lessons, we can also change elements or certain elements in a collection using index operator
#prutas[0] = "grape"
#print(prutas)




# So now moving on with sets:
# they are unorganized so like everytime you print a set,
# it will be randomized, it will not and cannot be alphabetically organized as well
# you can use some of the other methods that were used for Lists
# and also when you print the list of methods for sets, 
# it will be different and advanced so you can just also use the help() function
# for that and the description function dir()

# so sets use {}


#Moving on with the Tuples:
# they are also ordered but they are unchangable unlike Lists
# they can be duplicated as well unlike Sets, and it is faster than a list since its unchangeable
# it uses () just like when ur doing strings dba
# you can look at the previous lesson "2D Lists  - Grids and Tables"
# I showed a preview on how to used eacb collection

# Anyways any collection that were mentioned here are all fine, as long as it suits your program, that's all thank you 


#Exercise: 
seven = ("monday", "tuesday", "wednesday", "thurdsay", "friday", "saturday", "sunday")

#seven[0] = "tuesday" 
#print(seven) # as you can see, it will return as a error because as said earlier a tuple cannot be changed or unchangeable

numbers = {1,2,3,3,4,5,5,6,6,7,7,8,8,9,10}
print(numbers)





































































