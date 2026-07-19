# Nested Loops - a loop within another loop (outer, inner)
#                outer loop:    
#                    inner loop: should be indented after the outer loop

# You can encounter a nested loops:
# While loop inside of a while loop
# For loop inside of a for loop
# A for loop inside of a while loop
# A while loop inside of a for loop
# etc.

#Here's a demonstration: lets begin by displaying the numbers from 1-9 but we'll use a loop
for x in range(1,10):
    print(x) # so heres a feature, so with a print statement,
#            we end each print statement with a new line character
#            if i need all these numbers on the same line,
#            at the end of my print statement, I can add print(x, end = "")
#            normally with a print statement, each ends with the new line character print(x, end = "\n")
#            but we can set that to be something else, so when we run this print statement (x, end = "")

    print(x, end = "") # all of the numbers will be on the same line
                        # or you can add a different symbol like Dash (x, end = "-")
                        # or Space (x, end = " ")

# so we have used a loop to count the numbers 1-9
# What if i would like to repeat this three times?

# well, i could create another loop | for x in range(1, 4):, or you can just say 3 | for x in range (3):

for x in range(3): # now what ever loop that is within this loop, it will repeat 3 times

    for y in range (1, 10):   # so now we have this inner loop, 
#                             it will follow the outer loop or the loop before this loop was placed
#                             in this case, the counting would be repeated 3 times
#                             also there should be different variables for each loop to avoid confusions and counter actions
#                             there should be no same variable name   
        print(y, end = "")
# now you see, it repeated its counting 3 times, and that's around 27 iterations 3x9
# to exit this for loop, we need to count the numbers one through nine 
# once we do so, that is one iteration of the outer loop
# but our outer loop is saying it still needs three total iterations


# now if you like this on separate lines. let's make this look a little different
#let's add each iteration of the outer onto a new line
# so within the outer loop but not within the inner loop
# Im going to create a blank print statement
    print() # this would just print a new line

    # so with the inner loop, we count the number 1-9, afer we exit the for loop.
    # we will print a new line, and then repeat the inner loop all over again
    # until out outer loop is satisfied

# So that's basically a nested loop, its jsut a loop inside of another looping structure


# So let's create a project, we're going to print a rectangle, made up of some symbol that we set
# we'll have the user type in how many rows and columns this rectangle will have
# we will re-use the code on the second part, not the first one,



rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the desired symbol / character/s to use: ")

for x in range (rows): # think of the outer as the one in charge of the rows, so let's change the in range 3 to in range "rows"
    for y in range (columns): # the inner loops will be in charge of the columns, so in range "columns" 
        print (symbol, end=" ") # here will be the symbol the user chooses
    print()

    # so now, instead of the numbers, it will print the symbol that the user input, for the inner loop 
    # but you can customize this, other than symbols, it can be anything, a number or even alphabetical letters 



# So basically that's it, a nested loop is a loop inside of another loop
# the type of loop doesnt really matter as well as what's within each loop 
# its just a situation where you have a loop inside of another loop





#Loop Control Statements = change a loops execution from its normal sequence

#break = used to terminate the loop entirely
#continue = skips to the next iteration of the loop
#pass = does nothing, acts as a placeholder

#here is an example for "break" using while loop 
while True:
    name = input("Enter you name: ")
    if name != "": # the "!" states for 'does not', so in this case it would mean if name 'does not' equal to "" or if there is a character input then the program will break
        break # this can be also used to break iterations


# Next here is an example for continue, let's say we have a phone number

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-": # so here it tells if there is still a dash or a specific character in a tring  
        continue # it will continue to count
    print(i, end = "") # so if we just go with print(i), it will print every single character, one line each, but if we put an end = "" it will count the numbers in one line


# Next is pass, it does nothing, it acts as a placeholder
# lets say i would like to print the number 1 through 20 using a for loop

for i in range(1,21):
    if i == 13: # lets say i want to skip a number
        pass # i would use this to skip the number in the if statement
    else: # the rest will be printed besides the number i chose not to be printed
        print(i)

#Exercise for nested loops
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the desired symbol / character/s to use: ")

for x in range (rows):
    for y in range (columns):
        print(symbol, end= " ")
    print()

# Exercise for break 
for x in range (1,11):
    if x == 3:
        pass
    else:
        print(x)

# Exercise for continue

number_ameera = "0935-674-6643"

for i in number_ameera:
    if i == "":
        continue
    print(i, end= "")


#So yeah that's it for the nested loops + break and continue and pass