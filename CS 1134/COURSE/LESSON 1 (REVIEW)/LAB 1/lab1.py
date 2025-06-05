# 1. Implement the following function (30 minutes):
# def can_construct(word , letters):
# """
# word - type: str
# letters - type: str
# return value - type: bool
# """
# This function is passed in a string containing a word, and another string containing
# letters in your hand. When called, it will return True if the word can be constructed
# with the letters provided; otherwise, it will return False.
# Notes:
# ● Each letter provided can only be used one.
# ● You may assume that the word and letters will only contain lower-case
# letters.
# ● You may not use a dictionary for this question.
# ● Hint : Try to think about how you can use a list to implement a dictionary.
# ex) can_construct("apples", "aples") will return False.


# ex) can_construct("apples", "aplespl") will return True.





# QUESTION 1:

# METHOD 1: BIG O time complexity of O(n)

def can_construct(word,letters):
    letterlist=[]
    for letter in word:
        letterlist.append(letter)

    for letter in letters:
        if letter in letterlist:
            letterlist.remove(letter)
    
    if len(letterlist)==0:
        return True
    else:
        return False
    

        
print(can_construct("apples","aplpes"))



# QUESTION 2:

# METHOD 1: BIG O time complexity of O(n)


class UnsignedBinaryInteger:

    def __init__(self,num_str):
        self.data=num_str

    def __lt__(self,other):
        if self.data == other.data:
            return False
        if len(self.data)>len(other.data):
            return False
        elif len(self.data)<len(other.data):
            return True
        else:
            for i in range (len(self.data)):
                if int(self.data[i])<int(other.data[i]):
                    return True
                else:
                    return False

    def __gt__(self,other):
        if self.data == other.data:
            return False
        if self<other:
            return False
        else:
            return True
        
    def __eq__(self,other):
        if self.data == other.data:
            return True
        else:
            return False
        
    def is_twos_power(self):
        onecount=self.data.count("1")
        if onecount==1:
            return True
        else:
            return False

    def largest_twos_power(self):
        largenum=self.data.find("1")
        return 2**(len(self.data)-largenum)
        
    def __repr__(self):
        return f'0b{self.data}'

    # def __add__(self,other):
        
    # def __or__(self,other):
    #     for

    # def __and__(self,other):



def main():
    num1=UnsignedBinaryInteger("10100")
    num2=UnsignedBinaryInteger("10110")
    num3=UnsignedBinaryInteger("100000")
    num4=UnsignedBinaryInteger("010110")
    print(num1<num2)
    print(num1>num2)
    print(num1==num2)
    print(num3.istwos_power())
    print(num4.largest_twos_power())
    print(num4)


main()





# Implement the UnsignedBinaryInteger class to represent non-negative
# integers by their binary (base 2) representation
# a. Decimal number 13 as an UnsignedBinaryInteger object is initialized
# with the string ‘1101’.
# ● __init__ (self, num_str): Initialize the
# UnsignedBinaryInteger class with a string representing the binary
# number.
# ● __lt__(self, other): Returns True if self is less than other, or False
# otherwise
# ● __gt__(self, other): returns True if self is greater than other, or
# False otherwise
# ● __eq__(self, other): returns True if self is equal to other, or False
# otherwise
# ● is_twos_power(self): returns True if self is a power of 2, or False
# otherwise
# ● largest_twos_power(self): returns the largest power of 2 that is
# less than or equal to self
# ● __repr__(self): Creates and returns the string representation of self.
# The string representation starts with 0b, followed by a sequence of 0s and 1s
# —------------------------------------- optional
# ---------------------------------------
# ● __add__(self, other): Returns an UnsignedBinaryInteger
# object that represent the sum of self and other (also of type
# UnsignedBinaryInteger) the result also shouldn’t have excess leading
# 0’s
# ● __or__(self, other): Returns a UnsignedBinaryInteger object
# that represents the bitwise or result of self and other
# ○ Example:
# ○ 1010 or 1001 results in 1011
# ■ 1 or 1 → 1
# ■ 0 or 0 → 0
# ■ 1 or 0 → 1
# ■ 0 or 1 → 1
# ● __and__(self, other): Returns a UnsignedBinaryInteger
# object that represents the bitwise and result of self and other
# ○ Example:
# ○ 1010 and 1001 results in 1000
# ■ 1 and 1 → 1
# CS-UY 1134 Lab 1 Summer 2024
# ■ 0 and 0 → 0
# ■ 1 and 0 → 0
# ■ 0 and 1 → 0
# Notes and assumptions:
# ● Your implementation should account for the edge case where both numbers
# do not have the same number of digits.
# ● bin_num_str passed in the constructor does not have excess leading ‘0’
# in the front and will always begin with a ‘1’ for positive numbers, and a single
# ‘0’ for 0.


# ● In Python, the bitwise OR is represented by a single vertical bar, |, and the
# bitwise AND is represented by a single ‘and’ symbol, &.


# Starter Template
# class Python:
# def __init__(self, bin_num_str):
# """
# :type coefficients: list
# """
# self.data = bin_num_str
# def __lt__(self, other):
# """
# :type other: Polynomial
# :return type: Boolean
# """
# def __gt__(self, other):
# """
# :type other: Polynomial
# :return type: Boolean
# """
# def __eq__(self, other):
# """
# :type other: Polynomial
# :return type: Boolean
# CS-UY 1134 Lab 1 Summer 2024
# """
# def is_twos_power(self):
# """
# :return type: Boolean
# """
# def largest_twos_power(self):
# """
# :return type: int
# """
# def __repr__(self):
# """
# :return type: string
# """
# def __add__(self, other):
# """
# :type other: Polynomial
# :return type: Polynomial
# """
# def __or__(self, other):
# """
# :type other: Polynomial
# :return type: Polynomial
# """
# def __and__(self, other):
# """
# :type other: Polynomial
# :return type: Polynomial


# QUESTION 3:

# METHOD 1: BIG O time complexity of O(n)

# 3. Reverse List
# a. Given a list of values (int, float, str, …), write a function that reverses its
# order in-place. You are not allowed to create a new list. Your solution must run in
# (n), where n is the length of the list (10 minutes).Θ
# def reverse_list(lst):
# """
# : lst type: list[]
# : return type: None
# """
# b. Modify the function to include low and high parameters that represent the
# positive indices to consider. Your function should reverse the list from index low
# to index high, inclusively. By default, low and high will be None so these
# parameters are optional. If they’re both None (no parameters passed), set low to
# 0 and high to len(lst) - 1 just like in the previous function above.
# You are not allowed to create a new list. Your solution must run in (n),Θ
# where n is the length of the list (5 minutes).
# def reverse_list(lst, low = None, high = None):
# """
# : lst type: list[]
# : low, high type: int
# : return type: None
# """
# Example:
# lst = [1, 2, 3, 4, 5, 6], low = 0, high = 5
# reverse_list(lst) #default, no parameters passed
# print(lst) → [6, 5, 4, 3, 2, 1]
# lst = [1, 2, 3, 4, 5, 6], low = 1, high = 3
# reverse_list(lst, 1, 3)
# print(lst) → [1, 4, 3, 2, 5, 6]


def reverse_list(lst):
    originallength=len(lst)
    iterable=len(lst)-1
    while iterable>=0:
        lst.append(lst[iterable])
        iterable-=1
    return lst[originallength:]



def modified_reverse_list(lst,low=None,high=None):
    if low==None:
        low=0
    if high==None:
        high=len(lst)-1
    originallength=len(lst)
    iterable=high
    while iterable>=low:
        lst.append(lst[iterable])
        iterable-=1
    return lst[originallength:]

def reverse_list_v2(lst):
    for i in range (len(lst)//2):
        lst[i],lst[-i-1]=lst[-i-1],lst[i]
    return lst

def reverse_list_v1_high_low(lst,low,high):
    if low==None:
        low=0
    if high==None:
        high=len(lst)-1
    for i in range ((high-low)//2):
        lst[low+i],lst[high-i]=lst[high-i],lst[low+i]
    return lst

def main():
    lst=["anc",23,"2324",1273.23,"cheng","welcome",123123,'123123',232.23]
    print(reverse_list_v2(lst))
    lst=["anc",23,"2324",1273.23,"cheng","welcome",123123,'123123',232.23]
    print(reverse_list_v1_high_low(lst,0,4))

main()

    


# QUESTION 4:

# 4. Move Zeros
# Given a sorted list of positive integers with zeros mixed in, write a function to move
# all zeros to the end of the list while maintaining the order of the non-zero numbers. For
# example, given the list [0, 1, 0, 3, 13, 0], the function will modify the list to become [1, 3,
# 13, 0, 0, 0]. Your solution must be in-place and run in (n), where n is the length of theΘ
# list.
# def move_zeros(nums):
# """
# : nums type: list[int]
# : return type: None
# """
# Hint: You should traverse the list with 2 pointers, both starting from the
# beginning. One pointer will traverse through the entire list, but when should the
# other pointer move?


def movezeroes(lst):
    first_possible_zero=0
    for i in range(len(lst)):
        if nums[i]!=0:
            nums[i],nums[first_possible_zero]= nums [first_possible_zero],nums[i] # (swap method betwen 2 elements)
            first_possible_zero+=1


    for elements in lst:
        if elements==0:
            lst.pop(index(elements))


def movezeroes(lst):
    pointerposition=0
    for i in range(len(lst)):
        if lst[i]!=0:
            lst[pointerposition],lst[i]==lst[i],lst[pointerposition]
            pointerposition+=1
            

# QUESTION 5:

# MAXIMUM SUM SUBARRAY




