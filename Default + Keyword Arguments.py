# keyword arguments = an argument preceded(indicates that one thing occured or was place placed earlier than another) by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. Positional | 2. Default | 3. KEYWORD | 4. Arbitrary

# supposed  I have a function to display a message or a greeting
#def hi(greeting, title, first, last):
#    print(f"{greeting} {title} {first} {last}")

# to invoke the "hi" function, i would need to pass in four arguments
#hi("Hello", "Mr.", "Carl", "Taguba")
#print(hi)
# so what we used here is positional arguments, and the position of these arguments does matter
# so what we can do is put keyword arguments after the positional arguments, so even if you scramble the arguments,
# as long as it has the keywords it will be in the position it needs to be

def hi(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

#hi("Hello", title="Mr.", first="Carl", last="Taguba")
hi("Hello", last="Taguba", title="Mr.", first="Carl") # it will still be the same outcome
print(hi)
# but make sure, the positional argument should be the first, 
# not the keyword arguments, because it will be a syntax error

# Another example - im gonna print numbers 1-10 using a for loop
for x in range (1,11):
    print(x, end=" ") #remember how to put the numbers in one line? it's using "end=" which is a keyword,
#                      if you've seen the previous lessons before this

# another one is separate that's found within the print statement
print("1", "2", "3", "4", "5", sep=" ") # i can use a keyword named "sep"/separate,
# i would separate each of the strings with a character
# whatever that is placed in the separate keyword


#Exercise - we gonna create a function to generate a phone number,
#           but we need to pass in a country code, area code, 
#           the first 3 digits, the last 4 digits

def gen_number(country_code, first_3, middle_3, last_4):
    return f"{country_code}-{first_3}-{middle_3}-{last_4}"

phone_num = gen_number(country_code = +63, first_3 = 935, middle_3 = 674, last_4 = 6643)
# supposedly it should be 0### in the first_3, it should be 4 numbers but the number 0 makes it invalid
print(phone_num)
# this is how they make numbers in the philippines

# okay that's it for the keyword arguments









# Now for the default arguments
# Default arguments = A default value for certain parameters
#                     default is used when that argument is omitted (when you invoke a function)
#                     make you function more flexible, reduces #/number of arguments
#                     1. Positional | 2. DEFAULT | 3. Keyword | 4. Arbitrary

# let's define a function to calculate net price
def net_pricing(orig_list_price, discount=0, sales_tax=0.03): # these are what you call default values, if you don't put new arguments in the print statement, then these default values is what the program will follow in calculating the net price
    return orig_list_price * (1 - discount) * (1 + sales_tax) #here's the formula in getting the net price

# lets say i wanna buy a laptop for 700 dollars
#print (net_pricing(700)) # we can make this more flexible, if we put the defaut values in the parameters
#print (net_pricing(800,0.2))
#print (net_pricing(670, 0.01, 0.05))

#Exercise - we'll create a count up timer 
# we will import the time module

import time

#def time_counter(end, start=1): # when you are using default arguments in the parameters, the following argument must also be a default
                                # because it will cause a syntax error, you can fix it if you first put a parameter with no default value, and then the following parameter has one
#    for x in range (start, end + 1): # since the second argument is exclusive, we gonna add 1 in our time
#        print(x)
        #to make this thread running the program sleep
        # you can access the time.sleep module
#        time.sleep(1) # pass in for 1 second, this will make the counting stop for a second to be a bit realistic and accurate
#    print("DING DING DING, tapos naaaa")  # and outside of the for loop, let's print a statement saying the counting is done

# to invoke this function, we need to pass in two arguments
#time_counter(5) # you can set some custom values if you want them to start counting in a different value and stop at a different value 
#print(time_counter)
# same as the last example, we can just set the parameters with a default value, if the user doesn't want to change the counting start and end



#Exercise 2: with just name as default value
def describe_person1 (age, city, name = "carl"):
    return (name, age, city)

describe_ppl = describe_person1(21, "Cebu")
print(describe_ppl)


#Exercise 3: with all arguments, no default nor keyword, just positional arguments
def describe_person2 (name, age, city):
    return (name, age, city)

describe_ppl2 = describe_person2 ("Carl", 19, "Davao") #positional argument
print(describe_ppl2)


#Exercise 4: with name and city as keyword arguments and only age with default value
def describe_person3(name, city, age=18):
    return (name, age, city)

describe_ppl3 = describe_person3(name = "Carl", city = "Zamboanga")
print(describe_ppl3)

# so that's it for the positional, default, and keyword, next time na ang arbitrary HAHAHHAHA
