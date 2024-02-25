#Calling a Function
#To call a function, use the function name followed by parenthesis:
'''
def my_function():
  print("Hello from a function")

my_function()

'''

#Arguments
#Information can be passed into functions as arguments.

#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
'''
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
'''

'''
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")'''

#TypeError: my_function() missing 1 required positional argument: 'lname'
'''
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
'''


#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:

#Example
#If the number of arguments is unknown, add a * before the parameter name:


'''
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
'''


#Keyword Arguments
#You can also send arguments with the key = value syntax.

#This way the order of the arguments does not matter.
'''
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
'''


#Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

#This way the function will receive a dictionary of arguments, and can access the items accordingly:

#Example
#If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")