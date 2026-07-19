# List Comprehensions = A concise way to create lists in Python
#                       Compact and easier to read than traditional loops
#                       [expression for value in iterable if condition] 

# basically you have to follow this formula for:
# [expression for value in iterable if condition] - for every value in something that's iterable 
#                                                   (meaning you can loop through it)
#                                                    check some condition,
#                                                    and then do the expression

# so first let me show you an example with using a traditional Loop, then you'll be able to see why-
# a list comprehension is useful, we're going to create a list and double the numbers 1-10
doubles = []
# using a traditional for loop:
for x in range(1, 11): 
    doubles.append(x * 2)
print(doubles)
# so for a traditional for loop,it's quite long
# we can use a list comprehension to make this code more compact and easier to read
# here is how it will look with list comprehension:

#first we need a name for this list:
double = [ x * 2 for x in range(1, 11)] # we will follow the formula | [expression for value in iterable if condition] |
print(double)                           # we will use the if condition in the exercise later 
# so as you can see unlike the traditional for loop, we only used two lines instead of 4, which 
# saves a lot of space and time writing the code
# it's more understandable, the expression is that the value will be multiplied by two, and the
# range will be like the amount of numbers the we want to be printed or accessed

# so that's basically it, it's a much more cleaner and faster way of making a list:
# let's go over some exercises:

# what about this time we want to quadruple each number in a list
quadruple = [ y * 4 for y in range (1, 16)]
print(quadruple)

# let's square each numbers
squares = [ z * z for z in range (1, 12)]
print(squares)

# ________________________________________________________________
# now let's work with strings
guys = ["aj", "cj", "vj", "emj"]
# im gonna take each string in the list and make them all uppercase
# we could assign this to a new list
# or we can just simply just reassign it, just to keep it simple, I'll reassign it
#guys = [guy.upper() for guy in guys]
#print(guys)

# we can also make this in two lines only, we can replace the name of the list "guys" with just the 
# elements inside of the list
# it still works, but i prefer having a list name with the elements in it
# whatever works for you

# we can also return or print specific index of character of each element
guys_chars = [guy[0] for guy in guys]
#guys_chars = [guy[1] for guy in guys]
print(guys_chars)

# okay now let's work with conditions if conditions
# lets create a list of numbers
numbers = [1, -2, 3, -4, 5, -6, 7]
# we'll create a list comprehension to create a new list where all the numbers are positive
pos_num = [num for num in numbers if num >= 0 ] # we do need a expression, but if we're not modifying
                                            # each value, we can just return the value of 'num' (value)
# so in this case, if the numbers are greater or equal to 0, we will just return the value
print(pos_num)

# let's do it with the negative numbers
neg_num = [num for num in numbers if num <= 0 ]
print(neg_num)

# okay, now let's check to see if there are even numbers
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums) # it it should give us the numbers that are even, you probably thought it would be different

# okay what about odd numbers:
odd_nums = [num for num in numbers if num % 2 == 1]
print(odd_nums)

# Here's the last exercise:
# we'll create a list of grades
# a list of grades that are considered passing, meaning they scored the passing score or above
grades = [85, 67, 42, 49, 21, 92, 69]
grade_num = [grade for grade in grades if grade >= 60] 
print(grade_num)
# what about the failed scores:
grades_num = [grade for grade in grades if grade < 60] 
print(grades_num)

# so basically that's it, that's a list comprehension, a concise way to create list in python, 
# this saves space and time writing the code and it's much more easier to understand it's clearer



# Now let's proceed with lambda functions:

# Lambda function = A small anonymous function for a one time use (throw away function)
#                   They take any number of arguments, but have only 1 expression
#                   Helps keep the namespace clean (we dont have to think of a unique name for tha functions) and is useful with higher order functions
#                   'sort()', 'map()', 'filter()', 'reduce()'
#                   lambda parameters: expression
# example : lambda x: x * 2

# heres an example of a lambda function that you may see within a map() method
#map(lambda x: x * 2, numbers)
# so I havent explained what is a map function yet so, a lambda function
# is a function you would commonly see within a map() function or a higher order function
# but we will talk about this in the next lesson, in this lesson we're going to focus
# more on the syntax of Lambda function

# we will follow this formula
# - lambda parameters: expression 

# so first lets create a variable
# we'll write a lambda function to double a number
double = lambda x: x * 2 # so what we just did was we're assignning a lambda function to a variable
                         # although you could assign a lambda function to a variable,
                         # but that's not the primary use of them
                         # you would likely see lambda function within higher order functions
# now in this variable of "double"
# it contains a function, meaning we can call it
# to demonstrate that, im going to print my double variable
# and since it contains a function within it we can call it
# we have to pass in one argument,
# let's say 2
print(double(24))
# when we print this, you already know whats gonna happen

# anyways, with lambda function, it can take as many number of arguments as u need, although only 1 expression
# so let's make another variable and have 2 arguments
# let's do an add function 
add = lambda x, y: x + y 
print(add(2,2))
            
# okay let's write a more complicated expression 
# okay let's try to find the greater of two numbers
max_val = lambda x, y: x if x > y else y
print(max_val(6,7))

# how about the minimum value of two numbers
min_val = lambda x, y: x if x < y else y
print(min_val(8, 16))

# okay how about three arguments
# we'll find the greater of three numbers 
# we're gonna be using math functions (max(); min())
max_value = lambda x, y, z: max(x, y, z)
print(max_value(2,3,6))

# okay how about the lowest number of three numbers
min_value = lambda x, y, z: min(x, y, z)
print(min_value(2,3,6))

# okay how about names, let's say a full name
# we'll create a lambda function to concatenate a string
full_name = lambda first, last: first + " " + last
print(full_name("mike", "oxlong")) # unlike numbers, strings need quotations marks 
# the output will be a one long string because we're using string concatenation

# Using a lambda function, we can check to see if a number is even 
# i will create a variable
is_even = lambda x: x % 2 == 0 # modulus symbol will return a boolean statement of 0 or 1
                          # this checks if there is a remainder of a division
                          # you can remove the | == 0 | if you want
                          # cause 0 means True and 1 means False
                          # if you add the == 0 it will return either "True" or "False"
print(is_even(6))

# Let's do an age verification check
age = lambda x: print("you are an adult") if x >= 18 else print("you are a child")
print(age(16))

# we can do it with a boolean statement
age_check = lambda age: True if age >= 18 else False
print(age_check(17))


# so those are examples of lambda functions 
# they are like def "function name"(): but they are one time use and they are small and anonymous function, they can take any number of arguments, but only have 1 expression
# this helps keep the namespace clean because we dont have to constatntly think of different function names especially within a larger program and is useful with higher order functions




# And now, let's talk about lambda functions with the higher order functions
# sort(), map(), filter(), and reduce()

# higher order function = a function that either;
#                         1. accepts a function as an argument
#                                   or
#                         2. returns a function
#                         (In python, functions are also treated as objects)

# ill give u an example first for the number 1, 

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

# let's say i have two functions, both of the functions will accept a string as an argument
# in loud it will return the text in uppercase, and in quiet, it will return the text in lowercase
# im going to create a third function

def hello(func): # and this will be my higher order function, it will accept a function as an argument
    text = func("Hello")
    print(text)

# and now i will use the higher order function to use either one of the functions before the higher
# order function

hello(loud) # like i said earlier that a higher order function, it will consider another function as an argument
# here's the rundown of what just happened:
# we're calling the hello function and we're passing in the function "loud" as an argument
# we're naming "loud" as 'func' while we're within the higher order function 
# so it will be like -> text = (loud) and we're sending a string of text that says "Hello"
# we're returning that text all uppercase, assignning it to a variable called text
# and printing that text to the countil window hello() the parentheses is the council window
# let's try the quiet
hello(quiet)

# so that's an example of number 1, a higher order function is  a function thataccepts a function as an argument
# the hello function is an example of higher order function because we're accepting either loud or
# quiet as arguments:

# now moving on to the number 2:
# let's say we  have a pair of nested functions 

def divisor(x): # a divisor is a number that is used to divide another number when using division ( 10 / 2 = 5 )
    def dividend(y): # this is the number that will be divided it is called divident
        return y / x # we're dividng the divident to the divisor
    # now within the outer function but not the inner function, im going to return our divident function
    return dividend # so a higher order function is a function that also returns a function
                    # the divisor is the higher order function because we're returning dividend
    # now if i would like to access this nested dividend function, i first need to call the outside
    # divisor function and pass in a number as an argument to serve as the divisor
    #the function will return the dividend function which we can then assign to a variable

# so the variable, hmm, i'll name it as divide
divide = divisor(2) # so here im setting what should i divide the dividend with, let's say 2
#  for the dividend, i will print the divide variable, i will pass in a number as the dividend
print(divide(20))
# let me explain what just happened here, so our program begins with the divisor(2) and we're passing in '2'
# x will be 2 and it will  stay that way until we finish the program or until we re assign x
# so x = 2, skipping the nested function, because we did not call it yet
# we're returning dividend, and assigning it to a variable, and we can call a variable if it has the memory address of a function
# which what we are doing on the last line, (divide(20)), now we're calling dividend and passing in 20
# so y = 20 and x still = 2, we're returning 20 / 2 and printing it to the council window

# so in conclusion, higher order function is a function that either:
# 1. accepts a function as a argument
# or
# 2. returns a function

# the format for the number 2 is a little bit strange, and we're not quite used to it yet,
# but with the next lessons, we will use higher order functions more often, now that we have introduced higher order function

#Exercise:
squares = [x ** 2 for x in range (1, 21)]
print(squares)

even_squares = [x for x in squares if x % 2 == 0]
print(even_squares)

# lambda that doubles a number
doubles_a_number = lambda x: x * 2
print(doubles_a_number(5))
print(doubles_a_number(10))
print(doubles_a_number(30))

grades_of_students = [51, 75, 85, 91, 92, 86, 12, 43]
passing_grades = [grade for grade in grades_of_students if grade >= 60]
print(passing_grades)
# let's do the failing ones
failing_grades = [fail_grade for fail_grade in grades_of_students if fail_grade < 60]
print(failing_grades)

# okay that's all thank you