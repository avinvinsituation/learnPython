# Welcome back!

# Let's look at some more looping commands

"""
We know that, Boolean in if executes a command if the condition is true,

Sometimes we have to run a command to UNTIL a condition is true.

we have a new keyword for this control flow called 'while'

while <condition>:
    This command is executed until the condition is true
    And this command
    and this

    everything
    inside this while
    will be executed

    NOTICE THE INDENT! which tells
    which command is inside the while

    It is also IMPORTANT to
    make sure the condition
    becomes False
    at some point
    because if it doesn't
    the while will keep
    executing until eternity
    because it doesn't really
    care, ¯\_(ツ)_/¯

"""

# Here's were we can use "loops" which will execute the same command multiple times
"""
Revisitng 'while' loop, whose format is

while <condition>:
    command1
    command2
    command3
        .
        .
        .
"""
# Let us try a simple program that prints the numbers from 1 to 10

number = 1
while number < 11:
    print(number)
    number = number + 1 # the command that ensures the program reaches completion at some point
    # if the number was not incremented each time, then the number (1) will ALWAYS be less than 11,
    # and the while will run forever!


"""
Let's print 'something' twice with a loop,

TIP: remeber how we did the same on day5
"""
count = 1
while count<=2:
    print("something")
    count = count + 1


"""
Let's print 'something' 8 times with a loop
"""
count = 1
while count<=8:
    print("something")
    count = count + 1

# Do you see how short the command is?
# Now we can use this same concept to play more
"""
Let's print first 8 numbers!

without writing
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)

"""
count = 1
while count<=8:
    print(count) # Repeated 8 times
    count = count + 1 # Repeated 8 times

"""
Let's see what forever can look like!
That is if you don't have a counter!

"""
while True:
    variable = input("Enter something:")
    print("You entered :",variable)

# we have to have a way to change the condition to False to exit the while loop

condition = True
while condition:
    variable = input("Enter something:")
    if variable=='stop':
        condition = False
    else:
        print("You entered :",variable)

# notice how you stopped a loop without using a counter
# all that matters is the condition checked by while must be False to exit


"""
Let's see how we can print all the letters in a name

myName = "First Last"

Here is how python understands strings
  F  i  r  s  t     L  a  s  t
  0  1  2  3  4  5  6  7  8  9

So, in the memory, python stores the string as

myName[0] = "F"
myName[1] = "i"
myName[2] = "r"
myName[3] = "s"
myName[4] = "t"
myName[5] = " "
myName[6] = "L"
myName[7] = "a"
myName[8] = "s"
myName[9] = "t"

so now to print it!
"""

myName = "First Last"
character_index = 0
while character_index<len(myName):
    print("myName[",character_index,"] = ",myName[character_index])
    character_index = character_index + 1

"""
Let's revisit the program to count the number of words in a sentence!
eg. if the sentence is "I am from India"
the number of words need to be 4
"""

# First step is take an input
sentence = input("Enter a sentence :")

"""
Now that we have the sentence

REMEMBER HOW PYTHON STORES STRINGS

sentence = "I am from India"

  I     a  m     f  r  o  m     I  n  d  i  a
  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14

So, in the memory, python stores the string as

sentence[0] = "I"
sentence[1] = " "
sentence[2] = "a"
sentence[3] = "m"
sentence[4] = " "
sentence[5] = "f"
sentence[6] = "r"
sentence[7] = "o"
sentence[8] = "m"
sentence[9] = " "
sentence[10] = "I"
sentence[11] = "n"
sentence[12] = "d"
sentence[13] = "i"
sentence[14] = "a"

Now if you notice, there are 4 words in the sentence,
also notice, it has 3 spaces in the sentence

now if we count the number of spaces, and add 1, we should get the number of words! right?
Let's do that!
"""

words = 0
counter = 0
while counter < len(sentence):
    if(sentence[counter]==' '): # We are looking for a space in the word
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

A problem to think differently!
3. Write a program to repeatedly accept strings
   And print the paragraph received so far

"""
