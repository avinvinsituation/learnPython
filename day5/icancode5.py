# Welcome back!

# Yesterday we saw string manipulations


# Let's say we received the following input for a command
# sentence = input("Enter a sentence")

# And we received a sentence with
sentence = "This sentwnce has a typo"

# we can access the location of the typo
print(sentence[9])

# but we cannot change it like
#sentence[9] = 'e' # This will throw an error
# This is because strings are 'immutable' which is a fancy way of saying you can't modify the strings within the same memory location

# BUT, YOU CAN RE-DEFINE IT LIKE SO
sentence = sentence[:9]+'e'+sentence[10:16]+'d'+sentence[17:]
print(sentence)
# Tadaaaaaaaaaaa!

"""
Okay, we saw yesterday how we can use boolean for branching in a program

Remeber how you need to INDENT THE CODE to tell python which command to execute when
"""
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if (number1 > number2):
    if (number1 > number3):
        print("First number is the greatest!")
    else: # meaning number3 is greater than number1, indirectly also greater than number2
        print("Third number is the greatest!")
else:
    if (number2 > number3):
        print("Second number is the greatest!")
    else: # meaning number3 is greater than number2, indirectly also greater than number1
        print("Third number is the greatest!")

# Sometimes we need to run the same command multiple times, that's when loops come in handy

"""
Let's say we want to print 'something' twice
"""
print("something")
print("something")


"""
Let's say we want to print 'something' for 8 times
"""
print("something")
print("something")
print("something")
print("something")
print("something")
print("something")
print("something")
print("something")

# Notice how you are repeating the same command many times?
# Imagine if we had to print 'something' 100 times!
# You'd probably quit going through these files :P

# Here's were we can use "loops" which will execute the same command multiple times

# We'll look at looping examples on day6
