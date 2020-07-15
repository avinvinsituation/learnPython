import time
# Welcome back!

# Yesterday we saw if and else statements how to compare strings
# Today, we will look at nested branches
# Nested means, to have a branch within a branch

"""

Let's consider the same simple program!
> To write a program to take 3 numbers and output the greatest number
"""


# Yesterday's version
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

start_time = time.time()
if (number1 > number2) and (number1 > number3):
    print("First number is the greatest!")
elif (number2 > number1) and (number2 > number3):
    print("Second number is the greatest!")
else:
    print("Third number is the greatest!")
method1_time = (time.time() - start_time)
print("\nTime taken by method 1 is", method1_time ,"seconds\n")

# Total number of logical operations are 4
# When we use nested branching we can bring down the number of logical operations to just 2!

start_time = time.time()
if (number1 > number2):
    if (number1 > number3):
        print("First number is the greatest!")
    else:
        print("Third number is the greatest!")
else:
    if (number2 > number3):
        print("Second number is the greatest!")
    else:
        print("Third number is the greatest!")
method2_time = (time.time() - start_time)
print("\nTime taken by method 2 is", method2_time ,"seconds\n")

print("Time by method2 < Time by method1 ? \n=",method2_time < method1_time)

# Do you see the power of using lesser comparision and efficient coding?
# Perfect! always strive to write the fastest code, you'll never regret it :)

"""

Cool! let's look at some string operations

We can find the length of the string object by using len() funciton
"""

myName = "First Last"
length_of_myName = len(myName)
print(length_of_myName)

"""
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

"""

# You can also extract nth letter from a string and print it

print("myName[4] = ",myName[4])
print("myName[3] = ",myName[3])
print("myName[8] = ",myName[8])

"""

We can also access the letters in the string by passing negative values,
only difference is looks it up backwards

  F  i  r  s  t     L  a  s  t
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1

myName[-10] = "F"
myName[-9] = "i"
myName[-8] = "r"
myName[-7] = "s"
myName[-6] = "t"
myName[-5] = " "
myName[-4] = "L"
myName[-3] = "a"
myName[-2] = "s"
myName[-1] = "t"

"""

print("myName[4] = ",myName[-4])
print("myName[3] = ",myName[-3])
print("myName[8] = ",myName[-8])


"""
We can also extract a certain sub string from a string

by using '[' and ']'

string[start index : stop index]
"""

sentence = "Does life have a meaning?"
print(sentence[17:24])

"""
We can also extract a certain sub string AT REGUALR INTERVALS from a string

by using '[' and ']'

string[start index : stop index : STEP INDEX]
"""

sentence = "m1e2a3n4i5n6g7"
print(sentence[1::2])

"""
Try some challenge!
1. Write a program to take two numbers, and divide the bigger number by the smaller number and print the result
(Hint: Look out for divide by zero error)
"""
