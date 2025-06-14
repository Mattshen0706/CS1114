# Stacks: 
## (LIFO) Last in First out data structure
eg. undo function, taking plates out of a recessed buffet setting

### Operations of the stack class:

- Stack() - creating stack
- push() - putting element into the stack
- pop() - remove and return the item 
- peek()/top() - returns the top item 
- isempty() - returns a boolean for whether the stack is empty
- len() - returns the length of the stack 




## Creating the Stack Class

    class Stack:
        def __init__ (self):
            self.data=Arraylist()

        def top(self):
            return self.itmes[-1]

        def pop(self):
            return self.data.pop()

        def push(self, item):
            self.data.append(item) 

        def is_empty(self):
            return len(self.data)==0

        def __len__(self): 
            return len(self.data)

    
### Example of Stack Usage:
verifying code e.g nested brackets/syntax checker 
assume we have a line of code with brackets out of place:
> 
    d={}
    lst=[]
    lst[d{"DM]} 
>

## Code Checker using Stakcs
>
    def parser(file): 
        chars=Stack()
        for line in file:
            for char in line:
                if char in "[{(":
                    chars.push(char)
                elif char == ")":
                    if chars.pop()!="(":
                        return False
                elif char == "]":
                    if chars.pop()!="[":
                        return False
                elif char == "}":
                    if chars.pop()!="{":
                        return False
        
        return chars.is_empty()
                    
## Order of Operation Checker

Let eps be the smallest possible number in machine:
> 
    eps/2 = eps
    eps + eps = eps
    1 + eps = 1 + eps
    1 + eps != 1 
    eps/2 + eps/2 = eps

>

### How to convert from infix to postfix operand

Infix Operand: 2*(3+4)*5

Postfix Operand 234+*5*

(use the postfix operand to push numbers and operators onto the stack )

1. If the input is an operand, send to ouput
2. If the input is an open parantheses push onto the stack 
3. If the input is a close parentheses, pop from the stack and send to ouput all operators until the open parns is reached, discard all parens

The top of the stack will always have the highest presendence, to input a lower presendent operator you need to pop the higher operator from the stack 

e.g 
)3+

operands = numbers
operators = BEDMAS



> 
    def OrderofOps(file): 
        chars=Stack()
        for line in file:
            for char in line:
                if char in "[{(":
                    chars.push(char)
                elif char == ")":
                    if chars.pop()!="(":
                        return False
                elif char == "]":
                    if chars.pop()!="[":
                        return False
                elif char == "}":
                    if chars.pop()!="{":
                        return False
        
        return chars.is_empty()
            

    

# QUEUES: 
## (FIFO) First in First out data structure
eg. lines, customer service calls

### Operations of the Queues class:

- Queue() - creating queue
- enqueu() - putting element into the end of the queue
- dequeu() - remove element from the front of the queue
- first() - returns the first elemnt of the queue
- isempty() - returns whehter the queue is empty
- len() - returns the length of the queue

## Creating the Queue Class

    class Queue:
        def __init__ (self):
            self.data=Arraylist()
            self.front=0
            self.rear=0

        def first(self):
            if is_empty():
                raised IndexError
            return self.data[self.front]

        def dequeue(self):
            front=self.first()
            if self.front!=self.rear:
                self.front = -1
                self.rear=-
                self.data.clear()
            else:
                self.front+=1
                if self.front == self.capacity:
                    self.front ==0
            

        def enqueue(self, item):
            if self.front<=0:
                self.data.append(item)
                self.rear=0
            elif self.front<self.rear and self.rear!=self.data.capacity:
                self.data.append(item)
                self.rear+=1
            elif self.front< self.rear:
                self.rear=0
                self.data[0]=item
            elif self.rear<self.front-1:
                self.rear+=1
                self.data[self.rear] = item 
            elif self.rear==self.front-1
                temp=ArrayList()
                temp.resize(self.data.capacity*2)
                for i in range(self.front, self.capacity):
                    temp.append(self.data[i])
                for i in range(0,self.rear+1):
                    temp.append(self.append[i]) 
                self.data=temp
                self.front=0
                self.rear=temp.num_of_elements-1


        def is_empty(self):
            return len(self.data)==0

        def __len__(self): 
            if self.rear==self.front:
                return 0;
            elif self.rear<self.front:
                total=self.data.num_of_elements-self.front
                total+=self.rear+1
                return total
            else:
                return self.rear-self.front+1

Issue with using arraylist for queues is that when you continously dequeue and enqueue, there will be an infinitely large gaped create before the first element as you are constantly dequeing from the front and enquing to the back. 





    

