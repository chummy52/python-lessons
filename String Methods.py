# name = input(" enter your name: ")

#length function (len) - this gives us the lenght of a string

#result = len(name) # this function returns as a integer because 
# it gives us the number of characters in a string, 
# it also includes the spaces inside the string as characters

#print(f" hello {name}")
#print (f" your name has {result} characters")



#if we put a dot after the variable like this:
#variable = name.find, we wil have a lot of access to a bunch of methods

#1st: Find Method - this will return the first occurence of a given character
#result = name.find("C") #there can be any string inside the parenthesis
#print(result)

#2nd: Reverse Find Method - the opposite of the 1st Method
#result = name.rfind ("a")
#print(result)

#3rd: Capitalize Function: We can Capitalize the first letter of a string with this function
#name = name.capitalize()
#print(name)

#4th: Upper Method Function: Will take all of the characters in a string 
# And make them all uppercase letters
#name = name.upper()
#print(name)

#5th: Lower Method Function: Wil take all of the characters in a string
# And make them all lowercase letters
#name = name.lower()
#print(name)

#6th: isdigit Method Function: will return either True or False, if a string only contains digits
# The result is a Boolean, True or False, it returns True if there's only digits in a string, no letters
# if the string has letters, it will return False
#result = name.isdigit()
#print(result)

#7th isalpha Method Function: wil return either True or False, if a string only contains alphabetical characters
# It will return as True, if it has digits in the string, it will return False
# When there are "spaces" in the string, they are not considered as alphabetical characters
#result = name.isalpha()
#print(result)

#8th: Count Method - counts the amount of a character in a string
#  and will always return in a integer
# phone_number = input("enter your phone number: ")
# result = phone_number.count("-") # you can put anything here
# print(result)

#9th: Replace Method: We can replace any occurence with one character with another
# phone_number = input("Enter your phone number: ")
# result = phone_number.replace("-", "_") #it replaces the first string inside with the second string inside the parentheses
# print(result)

#if you like a comprehensive list of the string methods do this # this can be helpful in the near future  print(help(str))


#Exercise: characters don exceed 12 characters, no spaces, no digits

# username = input("Please put ur username here: ")

# if len(username) > 12 or not username.isalpha():
#     print("the character exceeds 12 characters, there should be no digits, and no spaces")

# else:
#     print(f" welcome to the hub {username}!")


