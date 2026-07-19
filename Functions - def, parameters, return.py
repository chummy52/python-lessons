# function = a block of reusable code
#            place () after the function name to invoke it

#heres a example, i need to say happy birthday 3 times
def happy_birthday_zoo():# inorder to define a function i need to type "def" 
#                          and a unique function namenow any code that belongs to the function should be indented underneath    
    print("Happy birthday to you")
    print("You belong to the zoo")
    print("With the monkey and the donkey")
    print("And the gorilla is you")

happy_birthday_zoo()
happy_birthday_zoo()
happy_birthday_zoo()

# this is much more efficient right? now if i need to say happy birthday 3 times, i would just place the function 3 times individually in seperate lines
#inorder to invoke this funtion, i would type the name of the function with the parentheses after
# i like to think of the parentheses as a pair of telephones talking to each other
# you call a function to invoke it, "hoy happy_birthday_zoo function, execute ur code bruh"
# with functions, you are able to send data directly to a function, using what are know as arguments
# you can send values or variables directly to a function

# example, place any data within the set of parentheses:
# happy_birthday_zoo("Cj")

# any data you send a function are known as arguments 
# but you need a matching set of parameters that are in order
# so what exactly is the data we're sending? well in the example, it's a name
# I will add one parameterr to my happy_birthday_zoo function

# example:

def happy_birthday_zoo(name, age):# i will name this data name, 
#                              a parameter is kinda of like a temporary variable
#                              that is used within a function   
    print(f"Happy birthday to {name}") # im gonna replace the you here with the parameter
    print("You belong to the zoo")
    print("With the monkey and the donkey")
    print("And the gorilla is you")
    print(f"You are {age} years old")

happy_birthday_zoo("Cj", 18) # when you invoke a function, you can send more than one argument, let's send an age this time
happy_birthday_zoo("nigga", 67)
happy_birthday_zoo("Tite", 18)

# if we have two arguments, we would also need two parameters for the function
# so before it was only | def happy_birthday_zoo(name) | now it would be (name, age) or whatever variable name you want
# also the position of the parameters matter, because if it was (age, name) then mabaliktad sila HAHAHAHAHA




# Lets try another example - i want to create a function to display an invoice
def display_invoice(username,amount,due_date): # there will be 3 parameters, a username, an amount, and a due_date
    print(f" Hello {username}")
    print(f" You have a debt amounting to ${amount:.2f}")
    print(f" You need to pay before: {due_date}")

display_invoice("Cj", 6749.24, "08/26/26")
display_invoice("Adrian", 7749.76, "09/15/26")
display_invoice("Rojen", 6996.96, "11/5/26")









# Now lets talk about the return statement
# return = statement used to end a function
#          and send a result back to the caller 

#Here's an example:

# lets make a function that add three numbers together
def add(x, y, z):
    a = x + y + z
    return a 

def subtract(x, y, z):
    a = x - y - z
    return a

def multiply(x, y, z):
    a = x * y * z
    return a

def divide(x, y, z):
    a = x / y / z
    return a

#lets invoke out all the functions, pass in 3 numbers, and print the results
print (add (1, 2, 3)) # this becomes 6
print (subtract (1, 2, 3)) # this becomes -4
print (multiply (1, 2, 3)) # this becomes 6
print (divide (1, 2, 3)) # this becomes 0.16666666 basta 
# so after we finish these functions, these functions becomes whatever is returned


#Now lets do something a little more complex
# we will create a function to create a full name

def gawa_pangalan(first, middle, last): # we will need 3 parameters first name, middle initial, and last name
    first = first.capitalize() # lets capitalize the first letter of the first name
    middle = middle.capitalize() # same here
    last = last.capitalize() # same here
    return first + " " + middle + " " + last # let's add spaces between the names

# so the function above this, just capitalize the first letter of each name

buong_name = gawa_pangalan("carl", "arabani", "taguba") # here lets make a variable outside of the function
print(buong_name)

# so we sent out function some arguments, and we have the parameters set up, 
# we took those values, and made them uppercase, 
# concatenated these strings together and then "returned" them as a single string
# using the return statement, you can return some data back to the place in which you call a function

# that's what functions are, they are reusable code


# Exercise 1
def greet(name):
    return name
hello_name = greet("cj")
print (hello_name)


# Excercise 2
def add(a, b):
    return (a + b)
result = add(6, 4)
print(result)

#Exercise 3 
def is_even(number):
    return number % 2 == 0

numero = int(input(" Please put the number here: "))
if is_even(numero):
    print(f" The number is even ")
else:
    print(f" The number is odd ")
