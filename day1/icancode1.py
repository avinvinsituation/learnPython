# Everything in Python is an Object

literallyAnyWordWhichBeginsWithALetterOr_IsAValidObjectName = 3
print(literallyAnyWordWhichBeginsWithALetterOr_IsAValidObjectName)

# You can print something using print()
something = 5
print(something)

# Anything typed after '#' is a comment, it's something that is ignored by Python in a program
# So this, is a comment

# What if you want more lines?
""" then you
can add a
comment in
this way """

# a Python program has two things
# 1. A definition
# 2. A command

x = 7 # This is a definition, because you're defining an object named 'x'
print(x) # This is a command

_ = 5 # This is a definition, because you're defining an object named '_'
print(_) # This is a command

"""
How to differentiate between a definition and a command?
when you type a definition in the python interpreter, you do NOT get an output because definitions are EVALUATED
when you type a command in the python interpreter, you get an output because definitions are EXECUTED

BTW, this is again a multiline comment
"""

# Objects have a type
int_isATypeOfObect = 4 # 'int' is a type you use when you want to store say 4 chocolates

float_isATypeOfObect = 3.14 # 'float' is a type you use when you want to store the value of Pi
"""
Fun fact:
Decimals are called "float" because
the decimal point can "float around" in a number.
eg,
50.0
5.00
0.500 etc
"""

bool_isATypeOfObect = False # 'bool' stands for Boolean, is a type you use when you want to store information if the earth is flat
bool_isATypeOfObect = True # if you believe the earth is flat

str_isATypeOfObect = "Whatever Your Name Is" # 'str' stands for string, is a type you use when you want to store your name

"""
To discover the type of an object you
use the command type()

eg, type(int_isATypeOfObect)
"""

print(type(int_isATypeOfObect))
print(type(float_isATypeOfObect))
print(type(bool_isATypeOfObect))
print(type(str_isATypeOfObect))

# If you change your mind you can convert the type of objects
piWithoutDecimalPlaces = int(float_isATypeOfObect)
print(piWithoutDecimalPlaces)
TrueValueIsTreatedAs1 = int(bool_isATypeOfObect)
print(TrueValueIsTreatedAs1)
FalseValueIsTreatedAs0 = int(False)
print(FalseValueIsTreatedAs0)

# you can also convert a string to numeric!
sayANewStringIs = "42" # PROVIDED IT HAS A NUMERIC VALUE

int_sayANewStringIs = int(sayANewStringIs) # you can convert it to integer
print(int_sayANewStringIs)

float_sayANewStringIs = float(sayANewStringIs) # you also can convert it to float!
print(float_sayANewStringIs)

yourName = str_isATypeOfObect
try:
    tryToConvert = int(yourName) # but this will throw an error
except:
    print("The above statement threw an error!")


"""
Some basic math operators
+   -   Addition
-   -   Subraction
*   -   Multiplication
/   -   Division
**  -   Power of
//  -   Quotient
%   -   Reminder
"""
x = 10
y = 3

print(f"x+y = {x+y}")
print(f"x-y = {x-y}")
print(f"x*y = {x*y}")
print(f"x/y = {x/y}")
print(f"x**y = {x**y}")
print(f"x//y = {x//y}")
print(f"x%y = {x%y}")

# You may also store the math operation you used above
answer = x/2
print(answer)

differentAnswer = y*3
print(differentAnswer)

pi = 22/7
print(pi)

# You can also overwrite the value previously stored, if you noticed earlier with "bool_isATypeOfObect'
myOpinion = False
print(myOpinion)

myOpinion = True
print(myOpinion) # Python respects your new opinion :P
# We tried with boolean, same is true with numbers or strings ¯\_(ツ)_/¯

# you can use paranthesis '(' and ')' to tell which math operation to do first
aVeryComplexEquation = (1+2)*(3+4)
print(aVeryComplexEquation)


# Enough for today!

"""
Try some challenge!
1. Write a program to find 2 to the power of 8 and print it
2. Write a program to find the square root of 16 and print it
"""
