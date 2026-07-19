# list - ised to store multiple items in a single variable
#ex:
#food = ["chicken", "pizza", "meat", "ameera"] # we can put multiple items in this variable by turning it into list
                 # in order to do so, we're going to sorround all of thevalues that we like to add
                 # within a set of square brackets
# so now, what happens when you print this "list"?
#print(food) # this would display all of the items that is in the variable, within the square brackets

# each item that are in a list are referred to as "elements"
# if we need to access a certain element in a list
# we have to list the "index"

# so again, in the print statement, we will put square brackets within the parentheses
# of the list, and also it should be put after the name of the list

#print(food[3]) # we would need to list the numbered index of the element
              # that we're trying to access, so computers always start counting with 0
              # so if we want to access the element named "pizza", we would need to start with 1 

# if you put a numbered index that is out of range in the list,
# it will be an error, because the list can only have a limited range,
# depending on how many elements you put
# an "index out of range" error


# One important concept with lists is that you can always
# update and change the elements found within a list
# later on in the program after you declare one

# let's say you want to immediately change an element within a list
#food = ["chicken", "pizza", "meat", "ameera"]

#food[2] = "hotdog" # let's say i want to replace "meat" with hotdog
                   #kay mahilig man ako sa hotdogs hehe
#print(food) # now once i print this again, the previous element in the position number 2
            # which was "meat", was changed to "hotdog"

# or if i want to print just the newly assigned element
#print(food[2]) # as i said earlier, it changed the previous element with the new one in its position number


# now if you want to display all of the elements found within a list, 
# you can easily do that with a standard for loop
#for x in food:
    #print(x) # as you can see, it displayed the elements in each line individually
             # although you might think a return statement would work better
             # since that would print them in a single line as a string,
             # it wont work because it is designed only for functions



# Now in this section, I will demonstate a few useful functions of lists
# and to access these functions, type the name of your list, dot(.),
# and there's gonna be a bunch to choose from 

# Here are the list methods or functions:
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	    Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	    Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list


# let's try using append here
food = ["chicken", "pizza", "meat", "ameera"]

#food.append("burger")

#food.clear()

#pagkain = food.copy() # so when you have another list and you want to copy a list, their elements, for a new list, just do this
#print(pagkain) # you would have to make a variable first inorder to copy a list

#a = food.count("ameera") # this counts how many times a element appeared in a list
#print(a)

#y = ["Ameera", "Baby"] # this adds the elements on a different list to the end of the current list
#food.extend(y) # make a new variable to make another list and then add the elements from the new list to the current list, and it will be added at the end of the current list u wanna siwtch it to

#a = food.index("ameera") # this returns the position number of an element inside of a list
#print(a) # you would have to make a new variable to do this inorder to "request" for the position of an element

#food.insert(0, "lumpia") # this adds an element in a specific positition, 
                       #or position number, so as long as this is active, 
                       #it won't be "chicken" the one in the number 0 position, it would be the inserted element in that position number
# this is different from .append, because this method adds an element in a speciic position

#food.pop(0) # this removes an element in a list, in the specified position number
# quite self explanatory dyt?

#food.remove("pizza") # this removes the first occurence of an element
#in the list, let's say you have 3 "pizza" in the list,
#the first occured "pizza" will only be removed,'
#and the later 2 "pizza" will not be removed

#food.reverse() # this reverses the order of a list
# this one is also self-explanatory

#food.sort() # this sorts out the elements in a list, alphabetically
for x in food:
    print(x)


# And that's it for the List and the List Methods/Functions

# An Exercise:
# Make a list of 5 subjects, that you'll study. 
# Add 2 more. Remove one. Sort alphabetically
# Print each item with a for loop
# Then reverse the list and print again

subjects = ["math", "science", "physics", "PE", "Chemistry"]

y = ["Literature", "Robotics"]
subjects.extend(y)
for x in subjects:
    print(x)

subjects.remove("Chemistry")
for x in subjects:
    print(x)

subjects.sort()
for x in subjects:
    print(x)

subjects.reverse()
for x in subjects:
    print(x)