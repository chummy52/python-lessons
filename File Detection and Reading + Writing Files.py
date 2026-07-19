# Basic File Detection using Python 

# to work with files using python, we will import the OS module
import os # means operation system, this module provides a way for python programs
          # to interact with the operating system
          # be sure to import the os module at the before before doing the coding

# for a demo, within my project folder, im going to create a new file and use txt for the file

# for convenience, im going to assign a variable of file path, it will be a string
# for file detection, we can use a relative file path or a absolute file path
# we'll cover relative file paths first, i would only need the file name including its extension

#file_path = "test.txt"
# we'll be passing in this string of file path as an argument

# to check if this file exist, i would use an if statement
#if os.path.exists(file_path): # "if access the OS module access the path", also there is a built-in method which is "exists"
                              # | exists(file_path) this method returns a Boolean value, True or False
#    print(f"the location '{file_path}' exists")
#lse:
#    print("That location does not exist")



# what if the file is in a folder, within my project folder 
#file_path = "stuff/test.txt"

#if os.path.exists(file_path): 

#    print(f"the location '{file_path}' exists")
#else:
#    print("That location does not exist")



# Now we're done with the relative, let's move on to the absolute, you should do this in ur desktop
# try making a new file in ur desktop
#file_path = "C:/Users/ACER/Desktop/aopsid.txt" # we would need to copy the location from the properties and add the file name and the extension

#if os.path.exists(file_path): 

#    print(f"the location '{file_path}' exists")
#else:
#    print("That location does not exist")






# there is a built-in method of "isfile" to check to see if that file is in fact
# a file and not a directory
#file_path = "C:/Users/ACER/Desktop/aopsid.txt" 

#if os.path.exists(file_path): 
#    print(f"the location '{file_path}' exists")

# lets add the following
# after we detect the file, we'll write an nested statement
#    if os.path.isfile(file_path): # is in fact a file and not a directory
#        print("That is a file")
#else:
#    print("That location does not exist")


# now what if it was a directory and not a folder?
# to know it is a directory and not a folder, we will be adding an elif statement
# we'll be using the "isdir" method to know if its a directory

#file_path = "C:/Users/ACER/Desktop/tesda.txt" 
#file_path = "C:/Users/ACER/Desktop/abc" 

#if os.path.exists(file_path): 
#    print(f"the location '{file_path}' exists")


#    if os.path.isfile(file_path): 
#        print("That is a file")
#    #lets add an elif statement here
#    elif os.path.isdir(file_path):
#        print("That is a directory")
#else:
#    print("That location does not exist")


# Alright so that's for the File Detection, Let's move on with Reading & Writing Files 

# Let's first start with write files (we'll cover .txt, .json, .csv)
# we will write and output files

#lets start with .txt, suppose we have some data we would like to output
#txt_data = "I like Ameera" # let's make a variable for the data

# for convenience, we will make a variable for a file path, it can be a relative or a absolute
#file_path = "output.txt" # within this file path, we would need a name
                         # then include the file extension
# this is a relative file path, when i generate this file, it will be within the same project folder 

# to create a file, we will write the following:
#with open(file_path, "w") as file: # |'with' open() function and then the file path within the parentheses
                      # and a character " " to write 'as' file:
#    pass
# for now ill write pass
# so there's a few things going on here, 'with' is a statement, its used to "wrap" a block of code to execute
# if we open a file, the 'with' statement will also close that file when we're done with it
# so we wont need to manually close files, when you open a file, it is good practice to close it
# because if you don't, you may run into unexpected behavior
# the 'with' statement takes care of that for you
# the 'open'() function will return a " file object ",
# the first parameter is the "file path", the second parameter is the "mode"
                            # (file_path,                             "w")
                                                                    # "w" is write,
                                                                    # "x" will write ("x") if the file doesnt exist, if it already does exist, we'll receive an error
                                                                    # "a" is for append, to append a file
                                                                    # "r" is to read, but we'll tuckle that later
                                                                    # but for now, we'll stick with "w" 
#with open(file_path, "w") as file:
#    pass

# the open function returns the file object,
# the first argument is the "file"
# the second argument is the "mode"
# you could set them (file = file_path ; mode = "w") as keyword arguments if it's easier for you to read
#with open(file = file_path, mode = "w") as file:
#    pass
# when the open() function returns a file object for us,
# we're using the 'as' keyword to give it a name "as" 'file'
# its kind of like we're instantiating a file object
# file = File()


# to write to this file, we're going to take our file object, 
# and use the built-in 'write()' method, and then pass in our data (txt_data)

#with open(file = file_path, mode = "w") as file:
#    file.write(txt_data) # after this, im going to print a confirmation message
#    print(f"txt file '{file_path}' was created")

# now we also have the capability of setting an absolutue file path

#file_path = "C:/Users/ACER/Desktop/output.txt"
#with open(file = file_path, mode = "w") as file:
#    file.write(txt_data) 
#    print(f"txt file '{file_path}' was created")

# like i said earlier that we have a few modes other than 'write

#with open(file = file_path, mode = "x") as file:
    #file.write(txt_data) 
    #print(f"txt file '{file_path}' was created")

# as you can see, you will receive an error, so for us to not be interrupted by the error
# we can use the "try" statement and "except" statement

#try:
#    with open(file = file_path, mode = "x") as file:
#        file.write(txt_data) 
#       print(f"txt file '{file_path}' was created")
#except FileExistsError:
#    print("that file already exists dumbahh")

# and if i were to delete the file, it would create the output since it detects that the file doesnt exist




# now there is also the "a" mode right? which is the append mode
#try:
#    with open(file = file_path, mode = "a") as file:
#        file.write(txt_data) 
#        print(f"txt file '{file_path}' was created")
#except FileExistsError:
#    print("that file already exists dumbahh")

# any new data will be appended to that file 
# also when appending data, if you would like the new datas on a new line
# we can add a new line character


#try:
#    with open(file = file_path, mode = "w") as file:
#        file.write(txt_data) 
#        print(f"txt file '{file_path}' was created")
#except FileExistsError:
#    print("that file already exists dumbahh")

# "w" will overwrite the file, basically back to the original



# when appending, either before or after we write our "text data"
# we could add a new line of character

#try:
#    with open(file = file_path, mode = "a") as file:
#        file.write("\n" + txt_data) # here | so "\n" means 'new line' and then plus text data
#        print(f"txt file '{file_path}' was created")
#except FileExistsError:
#    print("that file already exists dumbahh")
# so whenever we print this, we would append every new data on a new line 
# reminder: appending and writing are not the same, not the same modes


# okay let's work with a collection, let's say we have a list of employees

#employees = ["lorenz", "mark", "enzo", "jairus"]
#file_path = "C:/Users/ACER/Desktop/output.txt"

#try:
#    with open(file = file_path, mode = "a") as file:
#        file.write(employees) 
#        print(f"txt file '{file_path}' was created")
#except FileExistsError:
#    print("that file already exists dumbahh")
# if you try to run this, it will be an error, because we're dealing with a collection
# arguments should be a string and "employees" is a string
# so in order to write each item within a list, we'll need to iterate over it using some sort of loop


#employees = ["lorenz", "mark", "enzo", "jairus"]
#file_path = "C:/Users/ACER/Desktop/output.txt"

#try:
#    with open(file = file_path, mode = "a") as file:
#       for employee in employees:
#            #file.write("\n" + employee) # we're iterating over something that is iterable, we will access our file object and use the write method then write the argument
#            file.write(", " + employee)
#       print(f"txt file '{file_path}' was created")
#except FileExistsError:
#    print("that file already exists dumbahh")

# now when we print this, we would create that written each item inside the collection in a new line 
# you can also use a space, a comma, whatever you want








# Now we're done with the txt files, let's move on with .json or jason files
# so a jason file is made of key-value pairs
# here's an example:
#{
#    "firstName": "Carl Joaquin",
#    "lastName": "Taguba",
#    "gender" : "Male",
#    "age" : 18,
#    "address" : {
#        "streetAddress": "258",
#        "city": "zamboanga",
#        "state": "CA"
#    },
#    "phoneNumbers": [
#        {"type": "home", "number": "01230981249"}
#        ]
#}

# lets first add the json module
#import json
# for our data, let's say we have a dictionary of employees

#employees = {
#    "name": "Jeb",
#    "age": 49,
#    "job":"sex offender",
#    "workplace":"pegasus" 
    # so this is the data i would like to output
#}

# we will change the file extension
#file_path = "stuff/output.json"

#try:
#    with open(file = file_path, mode = "w") as file:
            # within our width block, we will make the following changes:
#            json.dump(employees, file, indent=3) # we're going to access our json module and use the 'dump' method
                      # the dump method will convert our dictionary to a json string to output it      
                      # we would need two arguments the dictionary and the name which is the "file"
                      # the things we removed are the for loop, and the write mode
#            print(f"json file '{file_path}' was created")
#except FileExistsError:
#    print("that file already exists dumbahh")

# so yeah this is a json file, it is a collection of key-value pairs
# a dictionary or anything that uses key-value pairs is a great candidate to be output for json files




# let's move on to .csv files or (Comma Separated Values)
# csv files are pretty common with a speadsheet of data like an excel 

# here's an example:
#Report generated on 01-01-2024,,,
#Created by : user1234,,,
#Company XYZ,,,
#,,,
#Date, Country, Units, Revenue
#2023-01-06, USA, 234, 11234.23
#2023-01-08, Panama, 654, 1156734.32
#2023-01-10, Panama, 27, 11456456.43
#2023-01-12, Brazil, 643, 1234234.34
#2023-01-14, USA, 154, 14574.45
#2023-01-16, Canada, 96, 11224.54
#2023-01-18, Philippines, 194, 11234.56
#2023-01-20, Germany, 456, 7572.65
#2023-01-22, Brazil, 23, 8456.76
#2023-01-24, Canada, 34, 14234.87


# we will create a 2d data structure of employees
#import csv
# this is gonna be a list of lists
#employees = [["Name", "Age", "Job"], # i will add name, age, and job
#             ["Spongebob", 21, "Software Engineer"],
#             ["Sandy", 26, "Scientist"],      
#             ["Chum", 18, "Gamer"]]       
# think of our 2d data structure as a table of rows and columns

#file_path = "stuff/output.csv" # we will switch the extension to a .csv

#try:
#    with open(file = file_path, mode = "w") as file:
            # within our 'with' block, we will make the following changes:
#        writer = csv.writer(file)    # we're going to create a writer object to write to a file
        # writer is an object, it provides methods for writing data to a csv file              
#        print(f"csv file '{file_path}' was created")
#except FileExistsError:
#    print("that file already exists dumbahh")

    # if we run this, the csv file will be made but the 2d collection will not be presented in the file
    # so we would have to iterate over all the rows in our 2d collection:
#try:
#    with open(file = file_path, mode = "w", newline = "") as file:
            # within our with block, we will make the following changes:
#        writer = csv.writer(file)
#        for row in employees: # for every "row" in our employees
#            writer.writerow(row) # and we'll use the writer object and use the 'writerow() function from the imported csv, for csv files
            # however, the writer method gives us a new line after each row
            # so if we would like to prevent that, when we open the file,
            # i would set a keyword argument (anything is fine) = (equal) to, 'no characters', an empty string

#        print(f"csv file '{file_path}' was created")
#except FileExistsError:
#    print("that file already exists dumbahh")

# so yeah that's how you write files in python, covering three file extensions, txt, json, and csv


# Now let's move on with Reading Files
# like before, ill start with txt, json, and lastly csv 
# for convenience, i will create a variable of file path
#file_path = "stuff/test.txt" # if you use absolute file path, and see '\' then it backlashes or escape sequences for special characters 
                                # but this time im gonna usea relative file path

# to read the file, i will add a with block, a with block is a statement used to wrap a block of codewithin a context manager, and it'll close a file if we open it
# like i said earlier, it is good practice to close a file if you do open it , if you dont, it can lead to unexpected behavior
#with open(file_path, "r") as file: # we will use the open() function
                           # the open() function has two arguments, our file path and a mode
                           # the open() function is going to return a file object which we will give a nickname of 'file'
    # when we read our file object, it's going to return one long string, which we will assign to a variable named, "content"
#    content = file.read() # use the read method 
#    print(content) # when we print the variable, this is gonna give us what is the content of the txt file

# let's say we cant find this file and perhaps i forgot the file extension
# when we print it without the file extension, it will give us an error 
# FileNotFoundError, and this will interrupt our program,
# so in order to not interrupt it

#try:
#    with open(file_path, "r") as file:
#        content = file.read()
#        print(content)
#except FileNotFoundError:
#    print("Can't find the file bro")

# what if you dont have permission to read the file?
# i dont know how it goes in macbook but in windows, here's how it will go:
# you would have to go to the properties of a file, and go to security and edit the permission
# and i would deny any sort of control, and if you try to run the program at this point, 
# it would come back as an error | PermissionError: [Errno 13] Permission denied: ur file path
# we could handle this exception as well:

# except PermissionError:
#   print("you do not have permission to read that file")

# so those are a few exceptions we can handle in case they appear 
#FileNotFoundError and PermissionError




# now let's move on to json files
# we would need the help of the json module
import json



file_path = "stuff/output.json" 

try:
    with open(file_path, "r") as file:
        content = json.load(file) # we're only gonna change the "content" except of file.read() 
        # with the data of your json file, you could access a value given a key
        # i would access our content by its key of name
        print(content["name"])
        print(content)
except FileNotFoundError:
    print("Can't find the file bro")



# now let's move on in reading .csv files or comma separated values
# we will import the csv module
import csv
file_path = "stuff/output.csv" 

try:
    with open(file_path, "r") as file:
        content = csv.reader(file) # we're only gonna change the "content"  
        # we're gonna use the reader method, and put in the file
        #print(content) # when we print this, we will be given a memory address
        
        #so what we need to do is read the csv file line by line 
        # all the data is within a collection(dictionary) which means we need to iterate them over
        # just like when we were writing a csv file
        # so we need to create a for loop
        for line in content:
            print(line)
            # now when we run this, it will list each lines of the dictionary
            # it resembles as a speadsheet excel lol
            # to get a specified column, we can access an index to get specified data 
            #ex:
            #print(line[0]) # this gives me the names only,
            #print(line[1]) # this gives me the ages only
            # you already know how it goes at this point

except FileNotFoundError:                       
    print("Can't find the file bro")

# so that's it for Reading files


#Exercise
#name = input(" please enter ur name: ")
#subject =input(" what is ur favorite subject?: ")
#data = f"{name} : {subject}"

#file_path = "stuff/output2.txt"

#try:
#    with open(file = file_path, mode = "w") as file:
#                file.write(data) 
#    print(f"txt file '{file_path}' was created")
#    with open(file_path, "r") as file:
#        content= file.read()
#    print(content)
#except FileExistsError:
#    print("that file already exists dumbahh")

# next is combine them into one script and with a menu
# basically make the 2 blocks into functions

def write_file():
    name = input(" please enter ur name: ")
    subject =input(" what is ur favorite subject?: ")
    data = f"{name} : {subject}"
    with open(file = file_path, mode = "w") as file:
                file.write(data) 
    print(f"txt file '{file_path}' was created")

def read_file():
    with open(file_path, "r") as file:
        content= file.read()
    print(content)

while True:
    choice = input(" Please pick a number (1-3): ")
    
    if choice == "1":
        write_file()
    elif choice == "2":
        read_file()
    elif choice == "3":
        print("good bye")
        break
    else:
        print("Wrong Input, Please Try Again: ")