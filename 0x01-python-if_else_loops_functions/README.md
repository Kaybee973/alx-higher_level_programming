Basic if statement in Python
Let's start by looking at a regular if statement.
In python this will be used as the following syntax.
if condition:
    # do something
You might want to check a variable for True/False, check if a number is higher/lower, or a string is a certain value.
number = 5
string = "Chris"
boolean = True

if number > 3:
    print("Number is positive")

if string == "Chris":
    print("Chris in the building")

if boolean == True:
    print("Boolean is true")
This will result in the following:
Number is positive
Chris in the building
Boolean is true
Multiple returns for an if statement
The cool part about this is that we can have multiple returns by using the correct indentation.

Let's say we need two lines of prints.
if number > 3:
  print("Number is positive")
  print("This is a second positive line")
That will return both lines if the statement is met!

If...else in python
As you may have guessed, this also gives us an excellent opportunity to use an else statement if the if fails.

The logic for that is as follows:
if condition:
    # do something
else:
    # do something else
Let's try that out with a better use case.
number = 10

if number > 20:
  print("Number is bigger then 20")
else:
  print("It's a smaller number")
Running this code will result in:
It's a smaller number
