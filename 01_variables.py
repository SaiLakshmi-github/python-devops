#declaring variable
a = 42
print(a)
#Types of variables
"""
-integer
- Boolean
 - strings
  - Dictionary
"""
#Datatype
"""
-list
-tuple
-set
-Dictionary
"""
#Python is case sensite i.e., True and true are 2 different things
#list
test_list = ["hello","world","python"]
print(test_list)
#tuple
test_tuple = ("hello","world","python")
print(test_tuple)
#Dict - stores the values in key value pairs
test_dict = {'a' : 1, 'b' : 2}
print(test_dict)
#set - unordered data, consider and print values in random way
test_set = {'a',"b",'abc'}
print(test_set)
#type () function- is a python buildin function ; prints the datatype of the variable
print(type(test_dict))
print(type(print))
#Operations - Add, Subtract, multiply, divide, integer division, modulo division(reminder)
a = 42
b = 6
c = a+b
print(a+b)
d = a-b
print(d)
e = a*b
print(e)
f = 12
g = 3
h = f/g
print(h)
print(h, type(h))
#by default division return float value
#integer division
h = f//g
print(h)
#reminder(modulo division)
i = f%g
print(i)
#concatenation
a = "42"
b = "43"
print(a+b)