# Welcome back!

# Let's look at some more looping commands

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

"""
Let's print 'something' for twice with a loop
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
    print(count)
    count = count + 1

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
"""
