# # LAB 3

# Question 1: (n is a power of 2)
# # a) logn number of numbers
# 1+2+4+8+16+n
# (1(2^n-1)/2-1)

# for i in range(0,n): linear operation 
#     sum+=2^i 
#     return sum

# O(linear)


# n+n/2+n/4+n/8 + 1
# 1(0.5^n-1)/0.5-1) + 1

# while i >1:
#     sum+=i/2

# O(logN)

# # b)
# 1 + 2 +3 + 4 + 5 + n^0.5
# O()

# 1 + 2 + 4 + 8 + 16 + n^0.5
# O()


# 2.
def countuptilln(n):
    lst=[]
    for i in range(n): #linear time complexity 
        lst.insert(i,i) #linear time complexity 

    # worst case run time: O(n^2)
    # Extra space usage: n

def sumuptilln (n):
    for i in range(1,n+1): #linear time complexity
        total=sum([num for num in range(i)]) #n^2 time complexity 
        print(total) #constant time complexiyt 

    # worst case run time: O(n^3)
    # Extra space usage: n^2

def palindromiclist (lst):
    lst2=lst.copy() #linear time 
    lst2.reverse() #linear time 
    if (lst == lst2): #linear time
        return True
    return False

    # worst case run time: O(n)
    # Extra space usage: lst

# 3)

#a 
def func1(n):
    if n<=1:
        return 0
    else:
        return 10 + func1(n-2)
    
    # worst case run time: n
    # output for fun1(16): 80

16 (+10)
14 (+10)
12 (+10)
10 (+10)
8 (+10)
6 (+10)
4 (+10)
2 (+10)
0 (0)

#b
def func2(n):
    if n<=1:
        return 1
    else:
        return 10 + func1(n//2)
    
    # worst case run time: logn
    # output for fun2(16):40

16 (+10)
8 (+10)
4 (+10)
2 (+10)
1 (+0)

#c
def func3(lst):
    if len(lst)==1:
        return lst[0]
    else:
        return lst[0] + func3(lst[1:]) #linear call (accessing elements)
    
    # worst case run time: n^2 
    # output for fun3([1,2,3,4,5,6,7,8]): 36

# 4.
#ARRAY LISTS 
#a)



def __repr__(self):
    s="["
    for i in range(self.arr-1):
        s+=(str(self[i])+',')
    s+=']'
    return s

#b)
def __add__(self,other):
    newlst=Arraylist()
    for i in range(self.)




    























