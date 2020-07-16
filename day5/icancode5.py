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


"""
Boolean in if executes a command if the condition is true,

But what if we want the command to KEEP RUNNING UNTIL the condition is true?

we have a new keyword for this control flow called 'while'

while <condition>:
    This command is executed until the condition is true
    And this command
    and this

    everything
    inside this while
    will be executed

    NOTICE THE INDENT!

    It is also important to
    make sure the condition
    becomes False
    at some point
    because if it doesn't
    the while will keep
    executing until eternity
    because it doesn't really
    care, ¯\_(ツ)_/¯
    ¯\_(ツ)_/¯
    ¯\_(ツ)_/¯
    ¯\_(ツ)_/¯
    ¯\_(ツ)_/¯
    ¯\_(ツ)_/¯
    ¯\_(ツ)_/¯
    ¯\_(ツ)_/¯
    ¯\_(ツ)_/¯

"""

# Let us try a simple program that prints the numbers from 1 to 10

number = 1
while number < 11:
    print(number)
    number = number + 1 # the command that ensures the program reaches completion at some point
    # if the number was not incremented each time, then the number (1) will ALWAYS be less than 11,
    # and the while will run forever!


# Let us look at a simple while program to count the number of words in a sentence!

sentence = input("Enter a sentence to find the word count:\n")
words = 0
counter = 0
while counter < len(sentence):
    if(sentence[counter]==' '):
        words = words + 1
    counter = counter + 1

words = words + 1 # Because the number of spaces are always one less than the number of words
print("Total number of words in given sentence =",words)


"""
Try some challenge!
1. Write a program to take a number as an input, and print the sum of all numbers from 0 to that input number
(Hint: refer to first while loop in this program)

2. Write a program to take 2 inputs,
    > a string And
    > an alphabet
   and print all the index numbers of that alphabet in that string
(Hint: refer to second while loop in this program)
"""
