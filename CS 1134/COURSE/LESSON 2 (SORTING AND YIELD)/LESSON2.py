SEARCHES 

LINEAR SEARCH:

def linersearch(lst,target):
    for i in range(0,len(lst)):
        if lst(i)==target:
            return lst[i]
        

BINARY SEARCH:

METHOD 1: (using loops)

def binarysearch(lst,target):
    left=0
    right=len(lst)-1
    found=False
    while ((found==False) and left<=right):
        mid=left+(right-left)//2
        if lst[mid]==target:
            found=True
            return mid
        elif target<lst[mid]:
            right=mid-1
        elif target>lst[mid]:
            left=mid+1

def main():
    lst=[2,3,3,3,3,4,5,6,7,8,9,9.5,10,2000,593959,35939539,53959395,3593952323232]
    print(binarysearch(lst,10))

main()


METHOD 2: (using recursions and helper function):

def binarysearchv2(lst,target):
    def binarysearchhelper(lst,target,left,right):
        if(left<=right):
            mid=(left+right)//2
            if lst[mid]==target:
                return mid
            elif (target<lst[mid]):
                right=mid-1
                return binarysearchhelper(lst,target,left,right)
            else:
                left=mid+1
                return binarysearchhelper(lst,target,left,right)
    return binarysearchhelper(lst,target,0,len(lst)-1)
    

SELECTION SORT:
WORST CASE: n^2
BEST CASE: n^2

import random

def selection_sort(lst):
    for i in range(0,len(lst)-1):
        min_index=i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[min_index]:
                min_index=j
        lst[i],lst[min_index]=lst[min_index],lst[i]

def main():
    randomlist=random.sample(range(0,100),100)
    selection_sort(randomlist)
    print(randomlist)

main()


INSERTION SORT: (REVISE)
WORST CASE: n^2
BEST CASE: n

def insertionsort(lst):
    for i in range(1,len(lst)):
        temp=lst[i]
        j=i
        while (j<0) and lst[j-1]>temp:
            lst[j] = lst [j-1]
            j-=1
        lst[j] = temp

MERGE SORT: (requires double space)
WORST CASE:nlogn
BEST CASE:nlogn

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(my_list)
print(sorted_list)





MERGE SORT CODE:

def mergesort(array):

    if len(array)>1:
        leftarray=array[:len(array)//2]
        rightarray=array[len(array//2):]

        mergesort(leftarray)
        mergesort(rightarray)

        leftindex=0
        rightindex=0
        mergeindex=0

        while leftindex<len(leftarray) and rightindex<len(rightarray):
            if leftarray[leftindex]>=rightarray[rightindex]:
                mergesort[mergeindex]=leftarray[leftindex]
                leftindex+=1
            else:
                mergesort[mergeindex]=rightarray[rightindex]
                rightindex+=1
            mergeindex+=1

        while leftindex<len(leftarray):
            mergesort[mergeindex]=leftarray[leftindex]
            mergeindex+=1
            leftindex+=1

        while rightindex<len(rightarray):
            mergesort[mergeindex]=rightarray[rightindex]
            mergeindex+=1
            rightindex+=1





    left=0
    right=0
    merged=[]

    while 

QUICK SORT: 
WORST CASE:n^2
BEST CASE:nlogn
Ideal fo4 bigger datasets

