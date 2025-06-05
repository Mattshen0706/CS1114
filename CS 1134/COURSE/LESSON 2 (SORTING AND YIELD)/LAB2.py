VITAMINS:

1)

a. 
    n^3 = O(nlog(n^n))

    False 

b.  
    n^0.5 = O(log(n))

    False

c.

    n^0.5 = O(n/log(n))       

    False
d.

    n! = O(100^n)

    False 

2.

1 + 1 + 1 + 1 ... + 1 = n = O(n)

n + n + n + n ... + n = n*n = O(n^2)

1 + 2 + 3 + 4 ... + n = n/2 (2+(n-1)) = n/2(n+1) = n^2/2 +n/2 = O(n^2)

log2 + log4 + log8 + log16 ... log(n) = logn/2(2+(logn-1)log2) = log2logn^2= O(logn^2)


3. 

log2(2)+log2(2)=log2(4)

log2(4)+log(2)=log2(8)


3. 

a) def func(lst):
    # for i in range(len(lst)):  TIME COMPLEXITY: O(n)
    #     for j in range (i):    TIME COMPLEXITY: O(n)
    #         print(lst[j],end="")    TIME COMPLEXITY: constant
            
            worst case run: O(n^2)
            # The inner loop will run i-1 for every outer loop value. As long as the len of the list is not equal to 1 in which the time complexity will be linear as the inner loop will not run at all 

b) def func(lst):
    # for i in range(0,len(lst),2):    TIME COMPLEXITY: O(n/2)
    #     for j in range(i):           TIME COMPLEXITY: O(n)/2
    #         print(lst[j],end="")     TIME COMPLEXITY: constant
        
            worst case run: O(n^2)
            # As long as the length of the list is greater than 2, the inner loop will run n-1 times, leading to a n^2 time complexity 

c) def func(n):
    # for i in range(n): TIME COMPLEXITY: O(n)
    #     j=1
    #     while j<80: TIME COMPLEXITY: O(constant)
    #         print("i=",i,'j=',j)
    #         j*=2

            worst case run: O(n)
            # No matter what value i is it will not affect how many times the while loops run as the j value is not affected by any input variable 

# d) def func(n):
#     for i in range(n): TIME COMPLEXITY: O(n)
#         j=1
#         while j<=n: TIME COMPLEXITY: O(n)
#             print("i=",i,"j=",j)
#             j*=2

            worst case run: O(nlogn)
            # the amount of times the while loop runs is directly impacted by the value of n. As the value of j is incrementing by a multiple of 2 every loop, the number of times the inner while loop will run ends up
            # being log2(n) times. Which makes the final time complexity of the function nlogn


4.  Given a string fucntion that reutrns true, if it is a palindrome and false if it is not 

1)

def is_palindrome(s):
    leftpointer=0
    rightpointer=(-1)
    while leftpointer<=len(s)//2:
        if s[leftpointer]==s[rightpointer]:
            leftpointer+=1
            rightpointer-=1
        else:
            return False
    return True



2) Write a vowel that takes in a string as input and returns a new string with its vowels reversed
e.g tandon would returnn tondan
must be an O(n) solution 

    Hints:
    list constructor converts a string into a list in linear time
    .join mstring is linear



def reverse_vowels(string1):
    list_str = list(string1) 
    left = 0
    right = len(string1) - 1

    while left < right:
        if list_str[left] not in "aeiou":
            left += 1
        elif list_str[right] not in "aeiou":
            right -= 1
        else:
            list_str[left], list_str[right] = list_str[right], list_str[left]  
            left += 1
            right -= 1

    return "".join(list_str)


print(reverse_vowels("tandon"))



3) function below takes in a sorted list with n numbers, from range 0 to n. function searches through the list and returns the missing number

# lst=[0,1,2,3,4,5,6,8]

# function will returnn 7

# def find_missin(lst):
#     for num in range(len(lst)+1):
#         if num not in lst:
#             return num
        
# better run time should be in logn 


O(n) run time:

def better_find_missing(lst):

    middle=len(lst)//2
    if middle not in lst:
        return middle
    elif middle==lst[middle]:
        better_find_missing(lst[middle+1:])
    else:
        better_find_missing(lst[:middle-1])

O(nlogn) run time:

def better_find_missing(numlist,start=0,end=0):
    
    middle=(start+end)//2
    
    if middle not in numlist:
        return middle
    elif middle==numlist[middle]:
        return better_find_missing(numlist,middle+1,len(numlist))
    else:
        return better_find_missing(numlist,0,middle)
        
def main():
    numlist=[0,2,3,4,5,6,7,8]
    length=len(numlist)
    print(better_find_missing(numlist,0,length))
    
main()

O(logn) run time:


def better_find_missing(numlist,start=0,end=0):
    
    if start >= end:
        return start
    
    middle=(start+end)//2
    
    if middle==numlist[middle]:
        return better_find_missing(numlist,middle+1,end)
    else:
        return better_find_missing(numlist,0,middle)
        
def main():
    numlist=[0,1,2,3,4,5,6,8]
    length=len(numlist)
    print(better_find_missing(numlist,0,length))
    
main()
    
# 4) takes a unsorted list 

# lst=[8,6,0,4,3,5,1,2]

# using a new sort method:
# sort and evaluat the difference

def findmissing(array):
    
    n=len(array)
    realsum=n*(n+1)//2
    arraysum=sum(array)
    return abs(arraysum-realsum)



# 4. finding an element in a sorted list can be done in logn time 

# lst=[1,3,6,7,10,12,14,15,20,21] goes to [15,20,21,1,3,6,7,10,12,14]


# binary search to search for 21. 

# lst[left]=15
# lst[right]=14
# lst[mid]=3

# 2 sorted parts


# given a rotated sorted list

# input: nums=[15,20,21,1,3,6,7,10,12,14]

# output=3
# at index 3, the minimum value is 1


# find the index of the smallest value:

def find_pivot(lst):

    left=0
    right=len(lst)-1

    while left<right:
        middle=(left+right)//2

        if lst[middle]>lst[right]:
            left=middle+1
        else:
            right=middle
            
    return left


lst=[15,20,21,22,3,6,7,10,12,14]
print(find_pivot(lst))



# find index of target value:

# pivot=find_pivot(lst)

def findtarget(lst,target,pivot):
    left=0
    right=len(lst)-1

    if target>=pivot and target <=lst[right]:
        left=pivot
    
    else:
        right=pivot-1

    while left<=right:
        middle=(left+right)//2
        if target==lst[middle]:
            return middle
        elif target>lst[middle]:
            left=middle+1
        else:
            right=middle-1
            

nums=[15,20,21,22,3,6,7,10,12,14]
pivot=find_pivot(nums)
print(findtarget(nums,22,pivot))

    
        





















