# While Loops - execute some  code WHILE some conditions remains  true
#example

# name = input (" Enter your name: ")
# if name == "":
#     print("You didn't type any characters!")
# else:
#     print(f" Hello, welcome {name}")

# this is how it is in conditional statements



#and this is how it is when you use While Loops
#example 1:
# name = input(" Enter your name: ")
#while name == "":
#    print("You did not put any characters/name")
#    name = input("Enter your name: ") # if you don't put an exit strategy in the loop, then it would go for infinite
#print(f" Hello {name}, welcome")

#example 2: asking for user's age
# age = (input("Enter your age: "))
# while age == "" or age < "0":
#    print("There's no characters or Numbers can't be negative!")
#    age = input("Please put your age: ")
# print(f" so you're {age} years old")

#example 3: Using Logical Operators on While Loops
pagkain = input(" Ano mga gusto mong kinakain? (press q to quit): ")

while not pagkain == "q":
    print(f" You like eating {pagkain}")
    pagkain = input("Ano pa mga gusto mong kinakain (press q to quit): ")
print("babye")

#example 4: enter a number within a certain scale

number = int(input(" Enter a # between 5 - 15: "))

while number < 5 or number > 15:
    print(f" number {number} is not valid")
    number = int(input("Enter a # between 5 - 15: "))
print(f" your number {number} is valid")


#Exercise 1: Countdown from 10 - 0 using a while loop
count = 10                    # Start with number 10
while count >= 0:             # WHILE count is 10 or more (10,9,8...0)
    print(count)              # Print the number
    count -= 1                # Subtract 1 (count = count - 1)
print("Blast off!")           # When loop ends, print this

#Exercise 2: Number guessing game: the program picks a number, user keeps guessing until correct. Print "Too High", "Too Low", or "Correct!"
import random                 # Get random number tool
secret = random.randint(1,10) # Computer picks secret number (1-10)
guess = int(input("Guess the number: ")) # User types first guess

while guess != secret:        # WHILE user's guess is WRONG
    if guess < secret:        # If guess too small
        print("Too Low")
    else:                     # If guess too big
        print("Too High")
    guess = int(input("Guess the number "))  # Ask for new guess

print("Correct!")             # When guess == secret, loop stops


