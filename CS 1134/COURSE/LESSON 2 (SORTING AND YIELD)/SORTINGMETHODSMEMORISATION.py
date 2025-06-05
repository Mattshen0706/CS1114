# Binary Serach:
# runtime: Logarithmic
# works only on a sorted list

def bin(lst,target):
    
    left=0
    right=len(lst)-1

    while left<=right: #use <= if you are trying to find a specific element in a list, otherwise use < if you are trying to index or insert an element into the list
        middle=(left+right)//2
        if lst[middle]<target:
            left=middle+1
        else:
            right=middle-1
    return left



def binarysearch(lst,target):
    left=0
    right=len(lst)-1
    while left<=right:
        middle=(left+right)//2
        if target<middle:
            right=middle-1
        else:
             left=middle+1
    return left
        


# Merge Sort: 
# runtime: nLogn 
# sorts a list using the principles of breaking down lists into smaller list and subsequently merging them in the correct order in place:
# Uses principles of recursions to make changes to the original list until all elements are sorted 

def mergesort(lst):

    if len(lst)>1:
        leftarray=lst[0:len(lst)//2]
        rightarray=lst[len(lst)//2:]
        mergesort(leftarray)
        mergesort(rightarray)
    
        leftpointer=0
        rightpointer=0
        mergepointer=0

        while leftpointer<len(leftarray) and rightpointer<len(rightarray):
            if leftarray[leftpointer]<rightarray[rightpointer]:
                lst[mergepointer]=leftarray[leftpointer]
                leftpointer+=1
            else:
                lst[mergepointer]=rightarray[rightpointer]
                rightpointer+=1
            mergepointer+=1
    
        while leftpointer<len(leftarray):
                lst[mergepointer]=leftarray[leftpointer]
                leftpointer+=1
                mergepointer+=1

        while rightpointer<len(rightarray):
                lst[mergepointer]=rightarray[rightpointer]
                rightpointer+=1
                mergepointer+=1


def mergesort(lst):
    if len(lst)>1:
        leftarray=lst[0:len(lst)//2]
        rightarray=lst[len(lst)//2:]
        mergesort(leftarray)
        mergesort(rightarray)

        leftpointer=0
        rightpointer=0
        mergepointer=0

        while leftpointer<len(leftarray) and rightpointer<len(rightarray):
            if leftarray[leftpointer]>rightarryay[rightpointer]:
                lst[mergepointer]=leftarray[leftpointer]
                leftpointer+=1
            else:
                lst[mergepointer]=right[rightpointer]
                rightpointer+=1
            mergepointer+=1

        while leftpointer<len(leftarray):
            lst[mergepointer]=leftarray[leftpointer]
            leftpointer+=1
            mergepointer+=1

        while rightpointer<len(rightarray):
            lst[mergepointer]=rightarray[rightpointer]
            rightpointer+=1
            mergepointer+=1
            
            
             
                  

# Quick Sort: 
# runtime: nLogn (best case)
# Uses the principle of setting a pivot and comparing all the values in the list to the pointer and saving the position of where to insert the pointer so that all 
# the values to the left of the pointer is less than the pointer and the values to the right are all greater than the pointer. The way it is done is that the function keep track of the index of the first number greater than the index
# and when all the values have been interated, it initiates a swwap between the last value and that index. 
# PS you do not have to choose the last value of the list to be the pointer, it can be any numbe. 

#uses 2 functions, one to sort and the other to partition the values
def quicksort(lst,low,high):
    if low>=0 and high>=0 and low<high:
        pivot_index=partition(lst,low,high)
        quicksort(lst,low,pivot_index-1) #This principle is similar to that of binary sorting, divides up the the list indefinitely into 2 and recursively divide it up to two smaller parts 
        quicksort(lst,pivot_index+1,high) #Notice how the the pivot value is not within the low high range as the position of the pivot has already been sorted from the above function call for partition
        
def partition(lst,low,high):
    i=low
    j=high-1
    pivot=lst[high]

    while i<j:
        while i<high and lst[i]<pivot:
            i+=1
        while j>low and lst[j]>=pivot:
            j-=1
        if i<j:
            lst[i],lst[j]=lst[j],lst[i]
    if lst[i]>pivot:
        lst[i],lst[high]=lst[high],lst[i]

    return i

unsortedlist=[1,20,455,23,45,583,40,1,3,4,5,23]
quicksort(unsortedlist,0,len(unsortedlist)-1)
print(unsortedlist)

    


# Insertion Sort: 
# runtime: n^2
# Divides the list into two parts, elements in the left part are sorted however only sorted within the values that have already been considered
# The position of the elments may still change later on when more elements are considered hence the positioning is not final 


# Method 1: continuosly shifting position until correct position is found

def insertionsort(lst):
    for i in range(1,len(lst)):
        for j in range(0,i):
            if lst[i]<lst[j]:
                lst[j],lst[i]=lst[i],lst[j]

    

# Method 2: Storing elements in a temp value and inserting when position is found, focuses on reassigning elements in the list and not doing swaps

def insertionsortv2(lst):
    for i in range(1,len(lst)):
        insertionitem=lst[i]
        j=i
        while j>0 and lst[j-1]>insertionitem:
            lst[j]=lst[j-1]
            j-=1
        lst[j]=insertionitem #when you exit the while loop that means that the insertionitem value is no longer smaller than the previous elment in the sorted list and subsequenetly you can reassing the value at position j to be the insertionvalue


# unsortedlist=[1,20,455,23,45,583,40,1,3,4,5,23]
# insertionsortv2(unsortedlist)
# print(unsortedlist)

# Selection Sort: 
# runtime: n^2
# Funadmental sorting algorthm which continuously swaps the smalles element as it loops through a list:

def selectionsort(lst):
    for i in range(0,len(lst)-1):
        minimum=i
        for j in range(i,len(lst)):
             if lst[j]<lst[minimum]:
                  minimum=j
        lst[i],lst[minimum]=lst[minimum],lst[i]


# unsortedlist=[1,20,455,23,45,583,40,1,3,4,5,23]
# selectionsortv2(unsortedlist)
# print(unsortedlist)


def selectionsort(lst):
    for i in range(0,len(lst)-1):
        minimum=i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[minimum]:
                minimum=j
        lst[i],lst[minimum]=lst[minimum],lst[i]

