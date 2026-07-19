# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# Example: Suppose we need to count to 10
#for x in range(1,11): # the x here is a counter but any variable can be the counter
#    print(x) # when this runs, we will start at 1 until 10
#print("Happy New Year!")

# for x in reversed (range(1, 11)): # we used reversed to count the opposite way unlike before, so it would start at 10 and end at 1
# print(x)
# print("Happy New Year!")

# we can also add step in the counting, like in the string indexing
# for x in range(1, 11, 2): #the third number is the step where you tell the program to count by 2s, 3s, whatever you want
#    print(x)
# print("Happy New Year")

# So the range function isnt the only thing you can iterate over or (repeat a process or a set of instructions multiple times)


#Lets say we have a credit card number
# credit_card = "123-4567-890"

# for x in credit_card: # x will hold our current position, at first it'll be 1,2,3,1, dash, and so on and so forth
#    print(x)
# So you can iterate over a string with the for loop as well

# There are 2 useful keywords, these aren't exclusive to for loops
#  you can use these within while loops as well
# They are continue and break

#Example: supposed we are going to count to 20
# for x in range(1, 12):
# example - 13 is considered an unlucky number right?
# what if our counter reaches 13, I would like to sip the number 13
# well we can do that with the "continue" keyword
#    if x == 6:
#        continue # this is used to skip over a iteration, in this case, we will skip the 6th character of the iteration
# else:
#    print(x)

#    if x == 6:
#        break # this is used to stop the iteration at a specific number, in this case, the counting will stop at number 5
# else:
#    print(x) 



# Conclusion: For loops can execute a block of code a fixed number of times
#             You can iterate over a range, string, sequence, etc.

# There is a lot of overlap where you could use either a while loop or a for loop
# While loops tend to be better if you need to execute something possibly infinite amount of times
# such as when you're accepting user input


#Exercises

for x in range (1,11): # this counts 1-10
    print(x)

for x in range (2, 21, 2): # this counts in even numbers
    print(x)

for x in range (1,11): # this is a multiplication table for number 7, the number can be changed
    print(f" 7 x {x}  = {7 * x}")

total = 0 # this is a Sum of all the numbers from 1-100 using a for loop
for x in range (1, 101):
    total = total + x
print (f" the sum of 1-100 is = {total}")

# The x btw in between the for and in, it can be changed to whatever you want tbh
# but most of the programmers uses x as the name of the variable

