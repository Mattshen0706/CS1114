# QUESTION 1

def recurse_function(input_data):
    if input_data == [-1]: # base case
        return 0
    else:
        if input_data[0] % 2 != 0:
            return input_data[0] + recurse_function(input_data[1:])
        else:
            return recurse_function(input_data[1:])

def main():
    sample_list = [8, 5, 4, 3, -1]
    print(recurse_function(sample_list))

main()

[8, 5, 4, 3, -1]
[5, 4, 3, -1]
5 + [4, 3, -1]
5 + [3, -1]
5 + 3 
8

# QUESTION 2

def recurse_function(input_data):
    if input_data == [-1]: # base case
        return input_data
    else:
        if input_data[0] % 2 == 0:
            return [-abs(input_data[0])] + recurse_function(input_data[1:])
        else:
            return [input_data[0]] + recurse_function(input_data[1:])
def main():
    sample_list = [8, 5, 4, 3, -1]
    print(recurse_function(sample_list))
main()

[8, 5, 4, 3, -1]
-8 + [5, 4, 3, -1]
[- 8,5,- 4,3,-1]



# QUESTION 3

def recurse_function(input_data):
    if input_data == [-1]: # base case
        return []
    else:
        if input_data[0] == 0:
            return recurse_function(input_data[1:])
        else:
            return [input_data[0]] + recurse_function(input_data[1:])
def main():
    sample_list = [0, 0, 4, 3, -1]
    print(recurse_function(sample_list))

main()

[0, 0, 4, 3, -1]
[4,3]


# QUESTION 4
def recurse_function(input_data):
    if input_data == [-1]: # base case
        return input_data
    else:
        if input_data[0] % 2 != 0:
            return [input_data[0] * 3] + recurse_function(input_data[1:])
        else:
            return [input_data[0]] + recurse_function(input_data[1:])
def main():
    sample_list = [8, 5, 4, 3, -1]
    print(recurse_function(sample_list))
main()

[8, 5, 4, 3, -1]
[8,15,4,9,-1]


# QUESTION 5
def power(base,exponent):
    if exponent==1:
        return base
    else:
        return base * power(base,exponent-1)


# QUESTION 6 Count Vowel
def count_vowels(str):
    count=0
    if len(str)==0:
        return 0
    else:
        if str[0] in "AEIOUaeiou":
            return 1 + count_vowels(str[1:])
        else:
            return count_vowels(str[1:])
        
print(count_vowels("This is a test"))


#Recursion Questions from Online:

# Fibonnaci Sequence:

def fibsequence(index):
    if index==0:
        return 0
    elif index==1:
        return 1
    else:
        return fibsequence(index-1)+fibsequence(index-2)
    
print(fibsequence(5))

# Sum of digits:

def sumofdig(digits):
    stringdigits=str(digits)
    sum=0
    if len(stringdigits)==0:
        return 0
    else:
        return int(stringdigits[0]) + sumofdig(stringdigits[1:])
    
print(sumofdig(125))

# Geomtric Series using recursions: (INCOMPLETE>>>>>>>>>>>>>>>>>>>>>)

def geoseries(termnum,commonratio):
    if termnum==0:
        return 1
    else:
        return geoseries(termnum-1)*commonratio
    

# GCD using recursions: (INCOMPLETE>>>>>>>>>>>>>>>>>>>>>)

def gcdequ(num1,num2):
    low=min(num1,num2)
    high=max(num1,num2)
    if num1%num2==0:
        return low
    else:
        return gcdequ(low,high%low)

print(gcdequ(2032,32))




    


