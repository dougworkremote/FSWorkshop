# + - * / %
a = 3
b = 6
c = a + b
d = b - a
e = a * c
f = e / a
g = 12 % d # modulus = remainder

# if/elif/else < > <= >= == !=
if (a < b):
    print('a < b')
if (a > b):
    print('should never happen')
h = 3
if (a == h):
    print('these are exactly equal')
if (a):
    print('eval to true')
i = 4
if (a > b):
    print('a was reassigned')
elif (a < b):
    print('a might have its original val')
else:
    print('something else happened to a')

# or and not
if (a < b and e > c):
    ('math is working, yay!')
if (a > b or b > a):
    ('well the second one is true')
# ! is negation
if (not a):
    print('will this log?')
if (not False):
    print('what about this?')

# loops
for x in range(0,5):
    # doing some iterative processing here
for k, v in {'key': 1, 'key2': 2}:
    print(k, v)
