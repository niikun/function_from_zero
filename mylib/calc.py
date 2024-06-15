import math

def add(x, y):
    return x + y   

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y

#bulid a function to calculate the function and 2 number

def calculate(func, x, y):
    return func(x, y)

# bulid a function sigmoid to calculate the sigmoid of a number

def sigmoid(x):
    return 1/(1+math.exp(-x))   

# bulid a function to calculate the ReLU function

def ReLU(x):
    return max(0,x)

# bulid a function to calculate the softmax function

def softmax(x):
    return math.exp(x)/sum([math.exp(i) for i in x])
