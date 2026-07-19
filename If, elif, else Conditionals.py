
# If statements - do some code if a condition is true
# else - do some code if the condition is false

age = int(input("Enter you age: "))
if (age) >= 18 and age <= 100:
    print("You can sign up for this")

# Elif - else if - check another condition if the first condition is false
elif age < 0:
    print("You are not born yet") 
elif age > 100:
    print (" you are too old for this unc")
else:   
    print("You are a child")


# another example

response = input("bembang, ano tara? (sigi/dili): ")
if response == "sigi":
    print("come here bebe <3")
elif response == "dili":
    print("sige, magsisisi ka, masarap pa naman ako")
else:
    print(" anu raw? tara na 5k")

# to see if the two values are equal, we use "==" 
# because if we use "=", that's an assignment operator
# this is used for comparisons


#Booleans in if, else, elif, statements

you_like_boys = True
I_eat_fries = True 
you_like_sleeping = False

if you_like_boys:
    print ("you gay ahh")
else:
    print ("aight u good")

if I_eat_fries:
    print ("same me too!")
else:
    print ("that's okay, people have preferences")

if you_like_sleeping:
    print("you are practicing death")
else:
    print ("you are not practicing death")

