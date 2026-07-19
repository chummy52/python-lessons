# class variables = Shared among all instances(objects) created from a 'class'
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class
#example:
#class Car:
#    wheels = 4 -> this is a class variable

#    def __init__(self, model, year, color): 
#        self.model = model # this is an instance variable
#        self.year = year # this is an instance variable
#        self.color = color # this is an instance variable

# instance variables are defined inside of the constructor
# class variables are defined outside of the constructor

# with class variables, they allow you to share data among all objects created from the class

# with instance variables, each object has their own version
# with the class variables, all those objects share ONE variable

# heres an example: we will create a class of Student
#class Student:
    # we also need a constructor
    # when we create a student object, this constructor is automatically going to be called, but we need to pass in some arguments
#    def __init__(self, name, age):
#                       |     |
#                      parameters
    # we will assign 'self', the object we're currently working with, set the attribute to equal the data for the name that we receive from a parameter
#        self.name = name
#        self.age = age
    # this will automatically call The Constructor

# now let's construct two student objects
#student1 = Student("AJ", 20)
#student2 = Student("CJ", 21)
#let's make sure that this works
#print(student1.name)
#print(student1.age)
#print(student2.name)
#print(student2.age)

# now we'll create a class variable
# this is outside  of the constructor
# and they are shared among all objects created from that class
# each object has their own name and attributes

# self.name = name-|
#                  ---->  these are instance variables
# self.age = age --|

# but class variables are defined outside the constructor
# each object will share this one variable,
# it should be placed before placing the constructor

class Student:
# here
    # so if we're working with students, let's say there is a class variable of class year
    class_year = 2025 # what is the graduating year of this class?
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
# ------------------------------------
        Student.num_students += 1 # increment by 1 
# --------------------------------------

student1 = Student("AJ", 20)
student2 = Student("CJ", 21)
# --------------------------
student3 = Student("VJ", 23) # added during the later part of the study
# -------------------------------------

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)

# now going back here, let's print hmm student1's graduation
print(student1.class_year)
# how about student2
print(student2.class_year)

# now with class variables, you can access them through any one object such as student1,
# but it's good practice to access a class variable by the name of the class which is | class Student: |
# so it will be like this:
print(Student.class_year) # this helps with Clarity and Readability
                          # if i was looking at this print statement
                          # i can tell that class_year is a class variable
                          # because we are accessing it directly from the class which is | class Student: |
                          # and not any instance from this class
                          # without looking at the class, | ex; (student2.class_year) |
                          # i can't tell if class year is an instance variable or a class variable
                          # but if i access it via the class name, it's more explicit

# alright lets create another class variable
# we'll create a class variable to keep track of how many students we have created
# we will add the class variable on the top again, come back after
# after that, lets go to the constructor, in the constructor we can write any code that we want
# the code will always be executed when we instantiate an object
# i would like to take the number of students and increment it by one
# each time we construct a new student object. 
# so instead of using self, self refers to the object we're currently working with
# if we're constructing student1, just iamgine we're replacing 'self' with student1 or student2
# if we're going to be modifying a class variable
# in place of self, we'll use the name of the class instead | class Student: |
# after doing the additions, we are constructing two student objects
# i will print: access our class of Student, get the class variable which is the num_students and print it

print(Student.num_students) # we're constructing two student objects, if i print the number of students that we have
                            # it should give us 2
                            # now to be sure, i will add another student object
                            # it should work

# so for an exercise: using a F string, let's print the student classes class year as well as the number of students
# i will print:
print(f"The graduating class of {Student.class_year} includes {Student.num_students} students. They are {student1.name},{student2.name}, and {student3.name} Congratulations!")

# now another exercise; create a student class: __init__ (name, age, gpa), a method introduce()
# that prints a sentence about the student.
# create 3 objects. Then add a class variable student_count that increments on every __init__

class Estudyante:
    student_count = 0

    def __init__ (self, name, age, gpa):
        self.name = name # this is a instance
        self.age = age # this is a instance
        self.gpa = gpa # this is a instance
    # ------------------------------
    # this here is a class variable
        Estudyante.student_count += 1
    # ------------------------------
    # make another constructor where u introduce the student
    def introduce(self):
        print(f" This is {self.name}, {self.age}, and has a {self.gpa} gpa.")

stud1 = Estudyante("Carl", 25, 4.0)
stud2 = Estudyante("Pearl", 30, 3.5)
stud3 = Estudyante("Vince", 35, 4.1)

stud1.introduce()
stud2.introduce()
stud3.introduce()

print(f" \n The total amount of students in this class is {Estudyante.student_count}")

# so that's it for class variables and objects