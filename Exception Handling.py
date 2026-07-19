# exception = An event that interrupts the flow ofa program
# there are different types of exceptions which include but are not limited to:
# (ZeroDivisionError) = when you attempt to divide a number by zero for example, 1/0
# (TypeError) = that's if we attempt to perform an opeartion of a value that's of the wrong data type
#               for example, 1 + "1" 
# (ValueError) = tend to happen when you attempt to typecast a value of the wrong data type
#                let's say we attempt to type case the pizza as an integer | int("pizza") |

# here's how we can do that, there's three steps:
# try:
      # try some code

# except Exception:
      # Handle an Exception

# finally:
      # Do some clean up

# these block any code that's dangerous where it could cause an error, 
# you'll place within a  tri block, for example: anytime we accept user input,
# that's considered dangerous code because a user can type in anything:

# so let's say we have a number 
#number = int(input("Enter a number: "))
#print(1 / number) # we would like to prevent out program from stopping
# the code is considered dangerous, a user can really type in anything,
# so we will surround the code in try block

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError: # for example a zero division error, instead of crashing, let's do something lke this:
    print("You can't divide by 0")

except ValueError:
    print("Enter only numbers please") 

# some people just type: | except Exception: | which is a bad pratice because it doesn't actually 
# catch all exceptions, however, it's too broad of a clause,
# it's good practice to tell the user what went wrong exactly,
# if we resort to just catching all exceptions, you may see an error message such as:
# "something went wrong"
# we want to tell the user what went wrong exactly, i would only catch all exceptions as a last resort
# so after we customized excepting specific errors, if there's a different error, then we can\
# except all of the errors

# now let's move on with the finally block
# this block always executes, regardless if there's an exception or not, it's usually used for any
# sort of cleanup that you need to do such as if you're handling files
# you may try and open a file and then you'll want to be sure to close the file, after you're done
# with it. That would be handled with the finally block.

finally: 
    print(" Do some cleanup here ")
    # the finally block, we'll talk about it soon, 