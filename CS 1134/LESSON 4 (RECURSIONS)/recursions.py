
def sumoffirstfewnum(num):
    if num==1:
        return 1
    else:
        return num + sumoffirstfewnum(num-1)
    
print(sumoffirstfewnum(10))



def count_up(start,end):
    if start>=end:
        print(start)
    else: 
        print(start)
        count_up(start+1,end)


def count_down(start,end):
    if start==end:
        print(start)
    elif start<end:
        return
    else: 
        print(start)
        count_down(start-1,end)


def count_up(n):
    if n<0:
        return
    elif n==0:
        print(n)
    else:
        count_up(n-1)
        print(n)

def count_down(n):
    if n<0:
        return
    elif n==0:
        print(n)
    else:
        print(n)
        count_down(n-1)
        



# count_up(0,14)
# count_down(14,0)
# count_up(5)
# count_down(5)


def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
def factorial(n):
    if n==0:
        return 1
    else:
        rest= factorial(n-1)
        return n * rest
    
def factorial(n):
    return (1 if n==0 else n*factorial(n-1))
    
def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


# # print(factorial(10))
# print(fib(20))



def count(ls,item): #Quadratic Solution with slicing
    if len(ls)==0:
        return 0
    else:
        if ls[-1]==item:
            return 1 + count(ls[0:len(ls)-1],item)
        else:
            return count(ls[0:len(ls)-1],item)
        
        #Whilst slicing will create more memory and greater time complexity, it preserves the original list
        #don't assume that you are able to modify the list


def count(ls,item):  #Linear Solution with pop 
    if len(ls)==0:
        return 0
    else:
        if ls[-1]==item:
            ls.pop()
            return 1 + count(ls,item)
        else:
            ls.pop()
            return count(ls,item)
        
        #popping a count function is not good as you will destory the memory of the list


def count(ls,item):  #Linear Solution with pop 
    def counthelper(ls,item,low,high):
        if low>high:
            return 0
        elif ls[low]==item:
            return 1+ counthelper(ls,item,low+1,high)
        else:
            return 0+ counthelper(ls,item,low+1,high)
    return counthelper(ls,item,0,len(ls)-1)

        
lst=[1,1,1,1,2,4,2,5,2,5,1,1,1,]
# print(count(lst,2))



# def power1(base,exp):
#     if exp==0:
#         return 1
#     else:
#         return base* power1(base,exp-1)

def power1(base,exp):
    if exp==1:
        return base
    else:
        part1=power1(base,exp//2)
        if exp%2==0:
            return part1*part1
        else:
            return base *part1*part1

# print(power1(2,1000))
    

def pos_ints_list(n):
    if (n==1):
        return [1]
    else:
        rest = pos_ints_list(n-1) #will keep calling until base case is reached hence, why the outcome is an increasing list
        # rest=rest+[n] #makes the function quadratic
        rest.append(n)
        return rest
    

# Order of Execution in Recursion:
# When you call pos_ints_list(n), it doesn't append anything until all the recursive calls finish.
# So if n = 4, this happens:
# pos_ints_list(4) calls pos_ints_list(3)
# pos_ints_list(3) calls pos_ints_list(2)
# pos_ints_list(2) calls pos_ints_list(1)
# pos_ints_list(1) returns [1]
# Now going back up the recursion stack:
# rest = [1], then append 2 → [1, 2]
# append 3 → [1, 2, 3]
# append 4 → [1, 2, 3, 4]
# You're always adding the larger number last, so the list grows in increasing order.
# print(pos_ints_list(20))


def reverse(lst):
    def reversehelper(lst,low,high):
        if low<high:
            lst[low],lst[high]==lst[high],lst[low]
            reversehelper(lst,low+1,high-1) #if the high is connected to the lenght of the list, you will have to subtract by 2
    reversehelper(lst,0,len(lst)-1))

def reversed_list(lst):
    result=lst[:]
    return reverse(result)

list1=[1,2,3,4,5,6]
print(list1)
reversed_list(list1)
print(list1)

