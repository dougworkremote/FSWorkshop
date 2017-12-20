# the primary data structures in Python are lists, tuples, sets, and dictionaries
# if youre familiar w/ the idea of arrays or sequences, lists are the similar here
# sets are just a list of unique values
# dictionaries would be like maps, hash maps, or key-value objects
# and tuples are a group of 'unchanging' values

listOfAnimalTypes = ['cats', 'dogs', 'lizards', 'dinos', 'hippos']

singleDino = {'name': 'T-Rex', 'aggression': 7, 'coolness': 10}
singleDino['name'] = 'Triceratops';

# unlike JS, Python dictionaries don't have the ability to create methods with them

# like PHP, Python makes heavy use of lists (like PHP's array)
# where a large part of your data manipulation, and built-in functions are for lists

# Python also have powerful list comprehension
# gives you the ability to generate lists from lists
# this is one of the bigger strengths in Python for data manipulation/generation

squares = [x**2 for x in range(10)]
# for x in range(10), gen a list of its squares

combination = [(x,y) for x in ['xs','s', 'm','l'] for y in ['blue shirt','red shirt', 'green shirt']]

# sets are handy for finding unique vals
# tuples are handy for related data
# dictionaries are handy for key-val pairs
