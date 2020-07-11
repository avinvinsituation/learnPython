# Welcome back!

# Let's pick up where we left off!
# We saw you can use paranthesis '(' and ')' to tell which math operation to do first
aVeryComplexEquation = (1+2)*(3+4)
print(aVeryComplexEquation)

# Let's look at what happens if you don't use '(' and ')' ?
# Python has an order to evaluate the operations

"""
This is the order of precedence

**  -   Power of

*   -   Multiplication
/   -   Division
%   -   Reminder
//  -   Quotient

+   -   Addition
-   -   Subraction

They are evaluated from left to right, same direction as you are reading this sentence. Makes sense?
"""

# So let's consider
Equation = 8/4*2*3*4**2
print(Equation)

"""
The above is evaluated internally like so
Given               > 8/4*2*3*4**2

Python's precedence > 8/4*2*3*(4**2)

result              > 8/4*2*3*16

Python's precedence > (8/4)*2*3*16

result              > 2.0*2*3*16    # Notice where the decimal point creeped in!

Python's precedence > (2.0*2)*3*16

result              > 4.0*3*16

Python's precedence > (4.0*3)*16

result              > 12.0*16

Python's precedence > (12.0*16)

result              > 192.0
"""

# Try
Equation = 2*2*3*4**2
print(Equation) # you get the same result without the decimal.

# Now let's look at how we could swap variables

print("\nStupid")
sayA = 2
sayB = 304
print(f"sayA = {sayA}")
print(f"sayB = {sayB}")


#we can't do
sayA = sayB
#and
sayB = sayA
print(f"sayA = {sayA}")
print(f"sayB = {sayB}")

# Why? because the computer is stupid. Right?
# ammm nope, it's just listening to you, so you decide!

# Remember we saw how to overwrite the value previously stored
myOpinion = False
print(myOpinion)

myOpinion = True
print(myOpinion)
# This is why it's stupid

print("\nConventional")
sayA = 2
sayB = 304
print(f"sayA = {sayA}")
print(f"sayB = {sayB}")

# Conventionally, this is how it's done
sayA = 2
sayB = 304

temporary = sayA
sayA = sayB
sayB = temporary
print(f"sayA = {sayA}")
print(f"sayB = {sayB}")

print("\nPython Way")
sayA = 2
sayB = 304
print(f"sayA = {sayA}")
print(f"sayB = {sayB}")

# Python has a smarter way!
sayA = 2
sayB = 304

sayA,sayB = sayB,sayA

print(f"sayA = {sayA}")
print(f"sayB = {sayB}")

# Let's look at adding strings!
first_name = "First"
last_name = "Last"
full_name = first_name + last_name
print(full_name)

# It's common to forget that damn space inbetween
print("It's common to forget that damn space inbetween")
full_name = first_name + " " + last_name
print(full_name)

# You can also create strings like so
non_sense = 5 * "nonsense "
print(non_sense)

# Another way to print is using ',' commas
print("sayA =",sayA)

"""
Okay cool! let's make this more fun and interactive!
We do that using the funtion input()


"""
# This takes an input
input()

# But we need to store that input somewhere, right?
storingInputInHere = input()
print(storingInputInHere)

# We can also ask what we're seeking input for by passing a message string
something = input("Enter something ¯\_(ツ)_/¯ : ")
print("Here is the something you entered",something)

print("Here is the same something printed 3 more times", (something+" ")*3)

# Let's try multiplying the number
text = input("Enter something a number to multiply by 5 : ")
print("Here is your number multiplied by 5",text*5)


# Oops! we forgot that int() to ensure it's a number
number = int(input("Enter something a number to multiply by 5 : "))
print("Here is your number multiplied by 5",number*5)

"""

We can also compare the values we take in

i > j     i Greater than j ?
i >= j    i Greater than or equal to j ?
i < j     i Lesser than j ?
i <= j    i Lesser than or equal to j ?
i == j    i equal to j ?
i != j    i not equal j ?

"""
i = 2
j = 3
print("i > j is",i > j)
print("i >= j is",i >= j)
print("i < j is",i < j)
print("i <= j is",i <= j)
print("i == j is",i == j)
print("i != j is",i != j)

# This command evaluates to bool
print(type(i>j))

"""
There are ways we can also work with boolean using the keywords

not      Will return the result OPPOSITE to the bool | not True = False | not False = True
or       Will ADD all the bools and return the result  | True or False = True | True or False => 1 + 0 => 1 => True
and      Will MULTIPLY all the bools and return the result | True and False = True | True and False => 1 * 0 => 0 => False

"""

sayABoolValue = True
sayAnotherBoolValue = False

print("not sayABoolValue is", not sayABoolValue)
print("sayABoolValue or sayAnotherBoolValue is", sayABoolValue or sayAnotherBoolValue)
print("sayABoolValue and sayAnotherBoolValue is", sayABoolValue and sayAnotherBoolValue)

"""
Try some challenge!
1. Write a program to take first and last name as input and print the full name
2. Write a program to take numbers as input and print if it is greater than 0
"""
