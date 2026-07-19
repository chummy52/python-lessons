# 2D Lists - these are pretty flexible, so 2D lists is just a list made up of lists
#            it's really useful if you ever need a grid or matrix of data
#            it's like a Excel spreadsheet

#let's make 4 lists
#fruit =   ["apple", "banana", "pineapple", "orange", "grape"]
#meat =    ["chicken", "beef", "fish"]
#drink =   ["coke", "water", "smoothie", "alcohol"]
#dessert = ["cake", "halo-halo", "candy"]

# so as you can see above, each of these lists are considered as a one-dimensional list

# now to create a 2D list, you would begin by creating a one dimensional list
# let's create a list of "groceries"

#groceries = [fruit, meat, drink, dessert] # we would need to add the lists as elements for this list

# to access or change one of the elements, you would type the name of the list, then use the index operator
#fruit[0] = "rambutan"
#print(fruit)

#with a 2d list, its a little different, if I were to print my 2d list of groceries
#print(groceries)
# we would layout the entire 2D list, flat
# we have individual lists separated with a comma, all enclosed within a set of square brackets


#let me go back and line up the 1D lists symmertically
# now it kinda represents a grid or matrix, with rows and coloumns 
# each individual list resembles a row, each element resembles a column

# If i were to print "groceries" at index 0
#print(groceries[0]) # In place of returning one element found within one of the lists
                    # that would return an entire list of an entire row 
# so "groceries" at index 0 is my fruit list, index 1 is my meat list, index 2 is my drink list, and index 3 is my dessert list


# for one of the elements found within one of the rows, you would need 2 indices(index)
# let's say i want to print the "chicken" only in the meat list
#print(groceries[1][0]) # the first square bracket is the row, 
                       # the second is the column
                       # parang coordinates lang x and y ykwim

# to access an element from a 2d list, you would need 2 indices(index) in place of one
# because using just 1, would return the entire row 

# now when you declare a 2D list, you dont need necessarily give each inner list a name
# we could do something like this:

#groceries = [["apple", "banana", "pineapple", "orange", "grape"],
#             ["chicken", "beef", "fish"],
#             ["coke", "water", "smoothie", "alcohol"],
#             ["cake", "halo-halo", "candy"]]

# here, this would work too, just separate each inner list with a comma
# then enclose everything with a set of square brackets

# if you ever need to iterate over the elements of a 2d list , you can use nested loops
# if i were to use a single for loop for like a collection 


#for collection in groceries:
    #print(collection) # using a single for loop, would iterate over the rows 

# but to also iterate over the elements found within each of the rows
# we would need to use a nested loop 

#for collection in groceries: # for every collection in groceries
    #for food in collection: # for every food in collection
        #print(food) # using nested loops, we can iterate all of the elements
                    # found within our 2D list(groceries)

# but i want to make this more organized kagaya sa una yung parang grid structure
#for collection in groceries:
#    for food in collection:
#        print(food, end=", ") # Im going to replace the new line character
                             # at the end of a print statment
#    print() # then when we exit the nested loop,
            # I will print a new line using just a empty print statement

# With 2d collections, or lists, you're not limited to just lists,
# you could create a list of tuples

# so the inner rows will be surrounded with a set of parentheses 

#groceries = [("apple", "banana", "pineapple", "orange", "grape"),
#             ("chicken", "beef", "fish"),
#             ("coke", "water", "smoothie", "alcohol"),
#             ("cake", "halo-halo", "candy")]

#for collection in groceries:
#    for food in collection:
#        print(food, end=", ")
#    print()

#This is also valid too



# or you can make 2D tuple,  it's a tuple made up of tuples, gawin mo lang parentheses  yung nasa labas
#groceries = (("apple", "banana", "pineapple", "orange", "grape"),
#             ("chicken", "beef", "fish"),
#             ("coke", "water", "smoothie", "alcohol"),
#             ("cake", "halo-halo", "candy"))

#for collection in groceries:
#    for food in collection:
#       print(food, end=", ")
#    print()


# you could make a tuple made out of sets, sets are enclose with a set of curly brackets
#groceries = ({"apple", "banana", "pineapple", "orange", "grape"},
#             {"chicken", "beef", "fish"},
#             {"coke", "water", "smoothie", "alcohol"},
#             {"cake", "halo-halo", "candy"})

#for collection in groceries:
#    for food in collection:
#        print(food, end=", ")
#    print()

# you can use kahit ano, basta yung will fit best sa program mo




#Exercise: let's create a 2D keypad that you would normally see in a phone
# we have 3 data types, a list, a set or a tuple
# the elements in a set, unordered so we can't use that
# if we have the option, a tuple is faster than a list 
# a tuple is ordered and unchangable, so we should use it if we can 
# and that's perfectly fine, let's create a 2d tuple this time

#num_pad = ((1, 2, 3),
#           (4, 5, 6),
#           (7, 8, 9),
#           ("#", 0, "*"))

# this will be the outer loop 
#for row in num_pad:
#    print(row)  # now we printing every row in our numpad, 
#                  but i want to remove the parentheses


# let's create a nested loop
#for row in num_pad:
#    for num in row:
#        print(num, end=" ")
#    print()
# now you have  a numberpad, you can see it's a grid made up of rows and columns 


#That's a 2D list, well a 2D collection, it's a collection that's made up of collections
# then with our numpad, we made a 2d Tuple

# if you need a grid or matrix of data, a 2d collection would work perfectly


#Exercise 2: tic tac toe

tictac = [
          ["_","_","_"],
          ["_","_","_"],
          ["_","_","_"]
]
    
tictac[1][1] = "X"
tictac[0][2] = "O"

for row in tictac:
    for symbol in row:
        print(symbol, end="")
    print()



