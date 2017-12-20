# this is a normal function
def func1():
    print('func1')

# this def (func, fn, f) takes 1 param
def func2(str):
    print('func2')
    print(str)

# this one takes 2
# str is short for 'string'
def func3(fn, str):
    print('func3')
    # were actually calling the passed fn inside func3 w/ the 2nd argument
    # fn is a callback
    fn(str);

# calling func3 w/ func2, which logs a str, w/ str 'hello'
func3(func2, 'hello')

# Python has 1st class functions
# which can be assigned, returned, and passed like parameters/arguments

def func4(str):
    print('func4')
    return (lambda print(str)) # this is an anonymous func because it doesn't have a name

func4ex = func4('hello2'); # func4 actually returned a func
func4ex(); # we are executing that returned func here

# recursion
def factorial(n):
    if (n == 0):
        return 1
    return (n * factorial(n - 1))
}
fac8 = factorial(8)
print(fac8)
