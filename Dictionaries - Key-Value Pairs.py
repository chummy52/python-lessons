# Dictionaries - a collection of {key:value} pairs
#                they are ordered and changeable. No Duplicates

# a few examples of {key:value} pairs could be:
# - An ID and Name
# - An Item and a Price
# but in todays example we'll create a dictionary for places
# let's name our dictionary "capitals"
capitals = {"usa":"Washington DC",
             "luzon":"manila",
               "visayas":"cebu",
                 "mindanao":"davao"}

print(capitals.get("usa")) # we would need to use the "get" function
# if ever there is a key that doesnt exist in the dictionary, this method would return "none"
# this can be also used within an if statement
if capitals.get("luzon"):
    print("this capital exist bro")
else:
    print("this capital dont exist bro")
# you can use this method if u want to know if a key:value exists in a dictionary
# just a reminder, if you want to see all of the different attributes and methods of a dictionary,
# you can use the dir function
print(dir(capitals))
# if you would like an in-depth description of all of these aatrributes and mehtods
print(help(capitals))



# alright lets move on, let's update the dictionary
#capitals = {"usa":"Washington DC",
#             "luzon":"manila",
#               "visayas":"cebu",
#                 "mindanao":"davao"}

capitals.update({"Lubotbot":"pukemon"}) # this will update the dictionary, 
                                        # you can insert new key:value or update an existing key:value in the dictionary
capitals.update({"usa":"america"}) # here is an example of updating a existing key:value in the dictionary

capitals.pop("usa") # if you want to remove a key value pair, you can use the pop method, just pass in a key

capitals.popitem() # this removes the most recent or the last key-value pair on the dictionary list

capitals.clear() # this just simply removes every key-value pair within the dictionary

# to get all of the keys within the dictionary but not the values, there is a "keys method"
keys = capitals.keys() # i think im going to insert this within a variable
print(keys)
vals = capitals.values() # same as the keys method but it will print out all of the values in the dictionary
print(vals)

# technically "Keys" is an object which resembles a list, we will talk more about this in the following lessons
# this is a topic from OOP or object oriented programming
# we can also use the keys method within a for loop, they're iterable
# we can also do the same for the "values" using the values method

for key in capitals.keys(): #reminder: | for every " " in ()
   print(key)

for vals in capitals.values():
    print(vals)

#the next one is the most tricky, this is the items method
items = capitals.items()
print(items)
# this returns a dictionary object which resembles a 2d list of tuples
# this might be a little bit complicated how might this be useful
# this time we're going to use a for loop to print 

for key, value in capitals.items(): # for every key, value in capitals.items()
# we have in essence two counters this time  
# i will print using an fstring | every {key}:{value} pair, this will print
# the key value pairs without the curly brackets or the 2d lists of tuples    
    print(f"{key}:{value}") # this will lay out the dictionary of ours,
                            # we have iterated over every key:value pairs
                            # its like an advanced topic but it's aight to bring it up now
print(capitals)

# so yeah everyone, so those are key-value pairs, 

#Exercise a student dictionary containing:
#name, age, course, gpa

student = {"name":"cj", "age":"18", "course":"computer science", "gpa":"3.50"}
# Access each value individually. 
# Add a "school" key. Update the gpa. 
# Delete age. Print all keys with .keys(),
#  all values with .values(), all pairs with .items().

# ACCESS EACH VALUE INDIVIDUALLY
print(student["name"])
print(student["age"])
print(student["course"])
print(student["gpa"])

student.update({"school":"WMSU"})

student.update({"gpa":{"4.0"}})

student.pop("age")

keys = student.keys()
print(keys)

vals = student.values()
print(vals)

for key, value in student.items():
    print(f"{keys}:{vals}")

# try it yourself, thanks for watching 