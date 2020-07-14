# Welcome back!

# Let's pick up where we left off!
# We saw you can use comparison operators and derive boolean results
# But why do we need them?

"""
They are used to determine what's called a "flow of control" of a program

Which means we can determine how a program "flows" based on certain checks

These checks facilitate "decision making" by the program, to help the program decide what to do next

This is done using the "if" and "else" statements, and here's the way to use it

if <condition>:
    Execute this command
else:
    Execute this command

NOTICE THE : AFTER THE if CONDITION
NOTICE THE COMMAND AFTER if IS INDENTED (4 SPACES / OR A TAB BEFORE THE COMMAND)
YOU WILL GET AN ERROR IF YOU DO NOT INDENT

Let's consider a simple program!
> Write a program to take 2 numbers and output the greatest number
"""

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 > number2:
    print("First number is the greatest!")
else:
    print("Second number is the greatest!")

"""
So what just happened?

this was how the code ran

                            if (number1 > number2):
                                print("First number is the greatest!")
                            else:
                                print("Second number is the greatest!")

                ______________________________|______________________________

if (True):                                                          if (False):
    print("First number is the greatest!") # This is executed                print("First number is the greatest!")
else:                                                               else:
    print("Second number is the greatest!")                                  print("Second number is the greatest!") # This is executed


"""

# Great! but now what if we had more than 2 numbers to check?
"""
Let's consider a simple program!
> Write a program to take 3 numbers and output the greatest number
"""

# One way to write is
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if (number1 > number2) and (number1 > number3):
    print("First number is the greatest!")
if (number2 > number1) and (number2 > number3):
    print("Second number is the greatest!")
if (number3 > number1) and (number3 > number2):
    print("Third number is the greatest!")


# An efficient way is
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if (number1 > number2) and (number1 > number3):
    print("First number is the greatest!")
elif (number2 > number1) and (number2 > number3):
    print("Second number is the greatest!")
else:
    print("Third number is the greatest!")

"""
Okay, now what's elif?

elif stands for "else if"

and the program runs like

if <condition>:
    then do this command
elif <another condition>:
    do this command
elif <another condition>:
    do this command
elif <another condition>:
    do this command
else:
    do this command


The advantage with elif is that if any if any of the if or elif condition evaluates to true,
THEN THE REST OF THE CONDITIONS ARE NOT CHECKED
this helps speed up the program greatly!

"""


# Okay let's revisit the string data type!
"""
RECAP

+ operator
E.g. Between two numbers: adds
E.g. Between two strings: concatenates
"""
full_name = "First name" + "Last name"
print(full_name)
"""
* operator
E.g. Between two numbers: multiplies
E.g. Between a number and a string: repeats the string
"""
non_sense = 5 * "nonsense "
print(non_sense)

"""
We can also use logical operators on strings
to determine the LEXOGRAPHIC ORDERING

s1 == s2     If two strings are equal, you can use to match passwords
s1 < s2      If the string s1 comes before string s2
s1 > s2      If the string s1 comes after string s2

"""

s1 = "ramesh"
s2 = "suresh"

print(" s1 == s2 is ",s1 == s2)
print(" s1 > s2 is ",s1 > s2)
print(" s1 < s2 is ",s1 < s2)

# That's good for today!

"""
Try some challenge!
1. Write a program to take a password string and print if it is the correct password,
(Hint: Define the password inside the program before asking for input)

2. Write a program to take three names and print the name that comes last in lexographic order.
(Hint: Refer how you printed the greatest of three numbers, this is the opposite)
"""
