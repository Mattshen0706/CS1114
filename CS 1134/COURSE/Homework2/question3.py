# Power of 2 Generator: 


# Method 1: Using yield and storing it in an iterable:

def powers_of_two(n):
    number=2
    for i in range(0,n):
        yield(number**i)
        
variablestored=powers_of_two(6)
print(next(variablestored))
print(next(variablestored))
print(next(variablestored))
print(next(variablestored))
print(next(variablestored))
print(next(variablestored))


# Method 2: Using for loop directly: 

def powers_of_two(n):
    number=2
    for i in range(0,n):
        print(number**i)
        
variablestored=powers_of_two(6)

