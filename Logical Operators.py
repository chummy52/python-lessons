# Logical Operators = used on conditional statements

# and = checks two or more conditions if True
# or = checks if at least one condition is True
# not = True if condition is False, and vice versa

# temp = "put any value" #much better if it aligns with the variable
# cloudy = True

# if temp >= 0 and temp >= 35:
#     print("the temperature is bad")
# else:
#     print("The temperature is good")

# if temp <= 0 or temp >= 35:
#     print(" The temperature is bad")
# else:
#     print(" The temperature is good")


# if cloudy:
#     print("It is cloudy outside")
# else:
#     print("It is sunny outside")

# if not cloudy:
#     print("It is sunny outside")
# else:
#     print("It is cloudy outside")


# Exercise - Login System
name = input("Please put your username: ")
password = input("Please put your password: ")

if (name) =="admin" and (password) == "1234":
    print("You are logged in!")
else:
    print("Please try again")

