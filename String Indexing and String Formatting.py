# String Indexing - accessing elements of a sequence using [] 
# It is also known as indexing operator
# Using this set of square brackets [], following a string, there are up to three fields that we can fill in

#[ start : end : step] these are the 3 fields we can fill in
# we can access a starting point in the string, an ending point, and a step

#Example:
credit_number = "1234-567-8935"
# if for example, i need the first character within the string
# I can type the name of my string variable followed by the indexing operator
print(credit_number[1]) # this would print out the character or in this example, this would print out the number in this number position

print(credit_number[0:4]) #what if you want only the four digits of the string
# you can also remove the 0 because python will assume that it will start from the beginning of the string

print(credit_number[3:]) # what if you want to start with the 3rd digit first and exclude the first two

print(credit_number[4:9]) # what if you want to start with the 4th digit and stop in a specific amount of digits

print(credit_number[-1]) # you can also use negative index, for example, if you need the last character in string

print(credit_number[:: 2]) # what if you want to count by 2s or 3s, you can use :: or step
print(credit_number[:: 5]) #  heres another one


#Exercise- what if you just want to get only the last four digits of a credit card number
last_digits = credit_number[-4:] 
print (f"xxxx-xxx-{last_digits}") 

#Exercise 2: What if you want to reverse the characters in the string, or in this case the digits
last_digits = credit_number[:: -1] # so if you want to reverse the string, the "step" should be negative one (-1)
print(last_digits)

# By the way, if you didnt know, Python starts counting at 0, so like (01234)
#                                                                     (abcde)







#String Formatting - str.format() = optional method that gives user more control
#                                   when displaying output

#Example: lets use a famous line("The fox jumped over the fence")

animal = "fox"
item = "fence"

print(" The {} jumped over the {}".format(animal,item))

# but just use the F-string tbh its much more easier
print(f" The {animal} jumped over the {item}") #see? much easier














# number = 1000
# print("The number pi is {:.3f}".format(number)) #
# print("The number is {:,}".format(number)) #
# print("The number is {:b}".format(number))
# print("The number is {:o}".format(number))
# print("The number is {:X}".format(number))
# print("The number is {:E}".format(number))