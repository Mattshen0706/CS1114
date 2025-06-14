import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

#ARRAYLIST CLASS -------------------------------------------------

class ArrayList:
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0

    def __len__(self):
        return self.n

    def pop(self, position=-1):

        if position<=-1:
            position+=self.n
        if position==-1 and self.n>0: # Theta (1)
            #self.resize(self.num_of_elements-1);
            temp = self.data[self.n];
            self.data[self.n-1]=None; #cybersecurity?????
        elif 0<=position<self.n: #Theta(n)
            temp = self.data[position];
            for i in range(position,self.n-1):
                self.data[i] = self.data[i+1];
        else:
            raise IndexError();

        self.n-=1;
        if self.n<self.capacity*0.25:
            self.resize(self.capacity//2)
        return temp;

    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)


    def __getitem__(self, ind):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        return self.data[ind]

    def __setitem__(self, ind, val):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        self.data[ind] = val


    def __repr__(self):
        data_as_strings = [str(self.data[i]) for i in range(self.n)]
        return '[' + ', '.join(data_as_strings) + ']'


    def __add__(self, other):
        res = ArrayList()
        res.extend(self)
        res.extend(other)
        return res

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __mul__(self, times):
        res = ArrayList()
        for i in range(times):
            res.extend(self)
        return res

    def __rmul__(self, times):
        return self * times

#STACK CLASS -------------------------------------------------

class StaticArrayStack:
    def __init__(self, max_capacity):
        self.data = make_array(max_capacity)
        self.capacity = max_capacity 
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def is_full(self):
        return (len(self) == self.capacity)

    def push(self, item):
        if(self.is_full()):
            raise Exception("Stack is full")
        self.data[self.n] = item
        self.n += 1

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        item = self.data[self.n - 1]
        self.data[self.n - 1] = None
        self.n -= 1
        return item

    def top(self):
        if(self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[self.n - 1]


#STACK CLASS -------------------------------------------------


class ArrayStack:
    def __init__(self):
        self.data = ArrayList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.pop()
    
    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            stack_elements = ", ".join(str(item) for item in self.data if item is not None)
            return f"Stack: [{stack_elements}]"
        


#QUEUE CLASS -------------------------------------------------

class ArrayQueue:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data_arr = make_array(ArrayQueue.INITIAL_CAPACITY)
        self.capacity = ArrayQueue.INITIAL_CAPACITY
        self.n = 0
        self.front_ind = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, elem):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        if (self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.n += 1
        else:
            back_ind = (self.front_ind + self.n) % self.capacity
            self.data_arr[back_ind] = elem
            self.n += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity #Move the front index forward by 1. The modulo (%) makes it a circular queue, wrapping around to 0 if it reaches the end of the array.
        self.n -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.n < self.capacity // 4) and
                (self.capacity > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(self.capacity // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]

    def resize(self, new_cap):
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        for new_ind in range(self.n):
            new_data[new_ind] = self.data_arr[old_ind]
            old_ind = (old_ind + 1) % self.capacity
        self.data_arr = new_data
        self.capacity = new_cap
        self.front_ind = 0

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            items = []
            index = self.front_ind
            for _ in range(self.n):
                items.append(str(self.data_arr[index]))
                index = (index + 1) % self.capacity
            queue_elements = ", ".join(items)
            return f"Queue: [{queue_elements}]"
#LAB4 -------------------------------------------------

#Q1 --------------------------------------------------------------------------------------------------

def nothing(lst):
    s = ArrayStack()  #create array
    for i in range(len(lst)): #append all elements of list into the array)
        s.push(lst.pop()) #remove from list from the back and add to the front of the array list 
    for i in range(len(s)): #iterate through all elements
        lst.append(s.pop()) #takes the last element inserted and appends it to the first element in the list 

# list1=[1,2,3,4,5,6]
# nothing(list1)
# print(list1)


#Q2 --------------------------------------------------------------------------------------------------

def smallestnumber(s):
    if len(s) == 1: #if length of list is 1 
        return s.top() #print out that value 
    else:
        val = s.pop() #store the most recent input in a variabel 
        result = smallestnumber(s) #store in a recursive call, with one less element in s
        if val < result: #if the second last element is less than, compare it to the previous call, will only return a value when lenght becomes 1
            result = val #make the result equal to value
        s.push(val)
        return result #makes result the smallest number
    
# s=ArrayStack()
# s.push(109000)
# s.push(1)
# s.push(33232)
# s.push(40)
# smallestnumber(s)
# print(smallestnumber(s))
# print(s)

#Q3 --------------------------------------------------------------------------------------------------

def oddonly (q):
    if (q.is_empty()): #check to see if queue is empty 
        return #if it is end the function call 
    else:
        val = q.dequeue() # if it isn't, take out the first inserted elemenet 
        oddonly(q) #call the function again with one less element
        if val % 2 != 0: # if the value which was removed is divisble by 2
            q.enqueue(val) #put the number back into the queue

q=ArrayQueue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(2)
q.enqueue(15)
q.enqueue(4)
q.enqueue(6)
oddonly(q)
print(q)




#Q4 --------------------------------------------------------------------------------------------------


# class ArrayQueue:
#     INITIAL_CAPACITY = 4
#     def __init__(self):
#         self.data_arr= make_array(ArrayQueue.INITIAL_CAPACITY)
#             self.num_of_elems = 0
#         self.front_ind = None
#     def __len__(self):
#     def is_empty(self): 
#     def enqueue(self, elem):
#     def dequeue(self): 
#     def first(self): 
#     def resize(self, new_cap): 

# Show the values of the data members: front_ind, num_of_elems, and the contents of
# each data_arr[i] after each of the following operations. If you need to increase the
# capacity of data_arr, add extra slots as described in class

# OPERATIONS:
q=ArrayQueue()
    # front_ind = None
    # num_of_elem = 0 
    # data_arr = [None,None,None,None]

q.enqueue("A")
print("_____________________________")
print("frontid:" + str(q.front_ind))
print("numofel:" + str(len(q)))
    # front_ind = 0
    # num_of_elem = 1 
    # data_arr = [A,None,None,None]
q.enqueue("B")
    # front_ind = 0
    # num_of_elem = 2
    # data_arr = [A,B,None,None]
q.dequeue()
    # front_ind = 1
    # num_of_elem = 1
    # data_arr = [None,B,None,None]
q.enqueue("C")
    # front_ind = 1
    # num_of_elem = 2
    # data_arr = [None,B,C,None]
q.dequeue()
    # front_ind = 2
    # num_of_elem = 1
    # data_arr = [None,None,C,None]
q.enqueue("D")
    # front_ind = 2
    # num_of_elem = 2
    # data_arr = [None,None,C,D]
q.enqueue("E")
    # front_ind = 2
    # num_of_elem = 3
    # data_arr = [E,None,C,D]
q.enqueue("F")
    # front_ind = 2
    # num_of_elem = 4
    # data_arr = [E,F,C,D]
q.enqueue("G")
    # front_ind = 0 
    # num_of_elem = 5
    # data_arr = [C,D,E,F,G,None,None,None]
q.enqueue("H")
    # front_ind = 0
    # num_of_elem = 6
    # data_arr = [C,D,E,F,G,H,None,None]
print(q)


#Q5 --------------------------------------------------------------------------------------------------

# Write a recursive function that takes in a Stack of integers and returns the sum of all
# values in the stack. Do not use any helper functions or change the function signature.
# Note that the stack should be restored to its original state if you pop from the stack. (15
# minutes)
# ex) s contains [1, -14, 5, 6, -7, 9, 10, -5, -8] from top → bottom.
# stack_sum(s) returns -3
# def stack_sum(s):
# """
# : s type: ArrayStack
# : return



#takes in a stack as an input and returns the sum of all the numbers
def stack_sum(s):
    if len(s)==0:
        return 0
    else:
        val=s.pop()
        total = val + stack_sum(s) #makes the check before you push back the elements into the stack 
        s.push(val)
        return total 

s=ArrayStack()
s.push(-20)
s.push(100)
s.push(21)
print(stack_sum(s))
print(s)


#Q6 --------------------------------------------------------------------------------------------------

# Implement the MeanStack class. The MeanStack pushes only integers and floats and
# rejects any other data type (bool, str, etc). It can also provide the sum and average of all
# numbers stored in O(1) run-time. You may define additional member variables of
# O(1) extra space for this ADT.
# The MeanStack will use an ArrayStack as its underlying data member. To test the data
# type, you may use the “type(var)” function in python.


class ArrayStack:
    def __init__(self):
        self.data = ArrayList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.pop()
    
    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            stack_elements = ", ".join(str(item) for item in self.data if item is not None)
            return f"Stack: [{stack_elements}]"
        


class MeanStack:
    def __init__(self):
        self.data = ArrayStack()
        self.num = 0
    def push(self,item):
        if type(item)==int or type(item)==float:
            self.data.push(item)
        else:
            raise Exception ("Type Error")
    def pop(self):
        return self.data.pop()
    def top(self):
        return self.data.top()
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data)==0
    def __str__(self):
        return str(self.data)
    def sum(self): 
        sum=0
        for i in range(0,len(self)):
            sum+=self.data.data[i]
        return sum
    def average(self):
        summation=self.sum()
        return summation/len(self)
    # def average(self):



# obj1=ArrayStack()

obj2=MeanStack()
print(obj2)
obj2.push(1)
obj2.push(2)
obj2.push(3)
obj2.push(500)
obj2.push(1)
print("----------------------------")
print(obj2.pop())
print(obj2.top())
print(obj2)
print(len(obj2))
print(obj2.sum())
print(obj2.average())
print(obj2.is_empty())


#Q7 --------------------------------------------------------------------------------------------------

# Write an iterative function that flattens a nested list while retaining the left to right
# ordering of its values using one ArrayStack and its defined methods. That is, you should
# not directly access the underlying array in the implementation. Do not use any helper
# functions or change the function signature. (30 minutes)

print("----------------------------")

lst = [ [[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
# flatten_list(lst)
# print(lst) → lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# s=ArrayStack()


def flatten_list(lst):
    s=ArrayStack()
    stringversion=str(lst)
    for i in stringversion:
        if i not in "[, ]":
            s.push(i)
    lst.clear()
    for i in s.data:
        lst.append(int(i))

flatten_list(lst)
print(lst)

#Q8 --------------------------------------------------------------------------------------------------

# Implement the ArrayDeque class, which is an array based implementation of a
# Double-Ended Queue (also called a deque for short).
# A deque differs from a queue in that elements can be inserted to and removed from both
# the front and the back. (Think of this as a queue and stack combined).
# Like the ArrayQueue and ArrayStack, the standard operations for an ArrayDeque should
# occur in O(1) amortized runtime. You may want to use and modify the ArrayQueue
# implementation done in lectures.


# ● __init__(self): Initializes an empty Deque using an array as
# self.data
# ● __len__(self): Return the number of elements in the Deque
# ● is_empty(self): Return True if the deque is empty
# ● first(self): Return (but don't remove) the first element in the
# ArrayDeque. Raise an Exception if it is empty
# ● last(self): Return (but don't remove) the last element in the
# ArrayDeque. Raises an Exception if it is empty
# ● enqueue_first(self, elem): Add elem to the front of the ArrayDeque
# ● enqueue_last(self, elem): Add elem to the back of the ArrayDeque
# ● dequeue_first(self): Remove and return the first element from the
# Deque. Raise an Exception if the ArrayDeque is empty
# ● dequeue_last(self): Remove and return the last element 

class ArrayDeque:
    def __init__ (self):
        self.data = ArrayList()
        self.n = 0
        self.capacity= 4
        self.front_ind = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)
    
    def enqueue_first(self, elem):
        self.data.append(elem)
        # if (self.n == self.capacity):
        #     self.resize(2 * self.capacity)
        # if (self.is_empty()):
        #     self.data[0] = elem
        #     self.front_ind = 0
        #     self.n += 1
        # else:
        #     back_ind = (self.front_ind + self.n) % self.capacity
        #     self.data[back_ind] = elem
        #     self.n += 1

    # def enqueue_last(self, elem):
    #     if (self.n == self.capacity):
    #         self.resize(2 * self.capacity)
    #     if (self.is_empty()):
    #         self.data[0] = elem
    #         self.front_ind = 0
    #         self.n += 1
    #     else:
    #         back_ind = (self.front_ind + self.n) % self.capacity
    #         self.data[back_ind] = elem
    #         self.n += 1

    def first(self): 
        return self.data[0]
    
    def last(self): 
        return self.data[-1]
    
    def resize(self, new_cap):
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        for new_ind in range(self.n):
            new_data[new_ind] = self.data[old_ind]
            old_ind = (old_ind + 1) % self.capacity
        self.data = new_data
        self.capacity = new_cap
        self.front_ind = 0

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            items = []
            index = self.front_ind
            for _ in range(self.n):
                items.append(str(self.data.data[index]))
                index = (index + 1) % self.capacity
            queue_elements = ", ".join(items)
            return f"Queue: [{queue_elements}]"
        
    

    
obj3=ArrayDeque()
print(len(obj3))
obj3.enqueue_first(22)
obj3.enqueue_first(12)
# obj3.enqueue_first(232)
# obj3.enqueue_first(42)
print(obj3.first())
print(obj3.last())
print(obj3)
print(obj3.is_empty())



# class ArrayQueue:
#     INITIAL_CAPACITY = 8

#     def is_empty(self):
#         return (len(self) == 0)

#     def enqueue(self, elem):
#         if (self.n == self.capacity):
#             self.resize(2 * self.capacity)
#         if (self.is_empty()):
#             self.data_arr[0] = elem
#             self.front_ind = 0
#             self.n += 1
#         else:
#             back_ind = (self.front_ind + self.n) % self.capacity
#             self.data_arr[back_ind] = elem
#             self.n += 1

#     def dequeue(self):
#         if (self.is_empty()):
#             raise Exception("Queue is empty")
#         value = self.data_arr[self.front_ind]
#         self.data_arr[self.front_ind] = None
#         self.front_ind = (self.front_ind + 1) % self.capacity #Move the front index forward by 1. The modulo (%) makes it a circular queue, wrapping around to 0 if it reaches the end of the array.
#         self.n -= 1
#         if(self.is_empty()):
#             self.front_ind = None
#         if((self.n < self.capacity // 4) and
#                 (self.capacity > ArrayQueue.INITIAL_CAPACITY)):
#             self.resize(self.capacity // 2)
#         return value

#     def first(self):
#         if self.is_empty():
#             raise Exception("Queue is empty")
#         return self.data_arr[self.front_ind]

#     def resize(self, new_cap):
#         new_data = make_array(new_cap)
#         old_ind = self.front_ind
#         for new_ind in range(self.n):
#             new_data[new_ind] = self.data_arr[old_ind]
#             old_ind = (old_ind + 1) % self.capacity
#         self.data_arr = new_data
#         self.capacity = new_cap
#         self.front_ind = 0

#     def __str__(self):
#         if self.is_empty():
#             return "Queue is empty"
#         else:
#             items = []
#             index = self.front_ind
#             for _ in range(self.n):
#                 items.append(str(self.data_arr[index]))
#                 index = (index + 1) % self.capacity
#             queue_elements = ", ".join(items)
#             return f"Queue: [{queue_elements}]"