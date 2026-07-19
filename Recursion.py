# recursion = a function that calls itself from within
#             helps to visualize a complex problem into basic steps,
#             which can be solved more easily iteratively or recursively

# def walk():
#     do something
#     walk()

# Iteratively, using a for loop or a while loop
#    def walk(steps):
#        for step in range(steps):
#            print(step)

#               or

# Recursively, which we will talk about in this lesson
# def walk(steps):
#     if steps == 0:
#         return
#     walk( steps - 1)
#     print(steps)


# okay let's say we have a complex task like walkings
# we can break walking, down into basci steps such as:
# taking a single step multiple times
# let's make a program that does this, both iteratively and recursively:

# Interative
#def walk (steps):
    # if i were to take an iterative approach in this function, within this function,
    # i could create a loop such as a for loop
#    for step in range(1, steps + 1): # 1 through steps + 1
#        print(f" you take step #{step}")
        # so this is iterative, we're looping within a function

# let's do a recursive approach this time
# Recursive
# Recursion involves a function calling itself from within
def walk (steps):
    if steps == 0:
        return # to exit a function, you can 'return'
    #print(f" you take step #{steps}")
    # at the end of our function, I will pass in 'steps'
    walk(steps - 1)
    print(f" you take step #{steps}")
    # we're invoking this function from within, it's creating a loop but we will include
    # the function itself whereas in with Iteration, we're only looping only within the function
    # let's see what happens: if we print this, it will give us the RecursionError
    # maximum recursion depth exceeded, this time, we're beginning at #100, 
    # we're iterating downwards, and we're going below zero, we don't want to take negative steps
    # so we need what is know as "a base condition" -- when do we want to stop?
    # I'm gonna add one line after the def walk(steps):
    # after that, if we print it again, it will stop at the base condition that we set
    # what if i want to count upwards and not downwards?
    # im only going to print the number of steps, after we invoke the walk function
    # and that solves the problem:

    # how does it work?:
    # when we enter the walk function, after accepting a number of steps we check our base condition
    # and then we invoke the walk function again but pass in one less than the number we originally
    # accepted, in a way we're creating a loop but we're involving the function itself,
    # when you invoke a function, you add what is known as a  "frame to the call stack"
    # there is a certain order in which we resolve functions, it's a "stack data structure"
    # you start at the top and work your way down, from 1 - 10, 1-100, it's like a stack of CD's
    # or movies, we add frames to the call stack until our base condition is met
    # then we undo everything starting at the top.
    
    # what if you have too many frames on the call stack, like a thousand steps
walk (100)
#walk (1000) # there's a maximum recursion depth, and we exceeded it, leading to a RecursionError
# for problems like this, i would stick with a iterative approach rather than a recursive approach 
# a recursive approach can be slower than a iterative approach but at times,
# it can be simpler to write, which you'll see in data structures and algorithms
# recursion is going to be your best friend

# Let's take a different approach, we're gonna print thefacotiral of a number, both iteratively
# and also recursively
# n! = n x (n - 1) x (n - 2) x... x 1

# let's do iteratively:
def factorial(x):
    result = 1
    if x > 0:
        for y in range(1, x + 1):
            result = result * y
        return result # i will return whatever the result is
print(factorial(8))
    
# let's do recursively:
def factorial_2(x):
    if x == 1: # if x is equal to 1
        return 1 # then we will return 1
    else:
        return x * factorial (x - 1) # all we need to do is return x times, invoke the factorial function
                                     # again, but we will pass in x - 1
print(factorial_2(10))
# and that's all, even though recursion is slower than iteration, 
# the code can be simpler and easier to write
# with a problem like this, i would lean more toward the recursion approach

# so that's all guys thank you 