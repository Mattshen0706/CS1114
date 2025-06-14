# ITERABLE:

# list1=[1,2,3,4,5,6]
# iterable=iter(list1)
# end=False
# while end==False:
#     try:
#         print(next(iterable))
#     except StopIteration:
#         print("list finished")
#         end=True




# YIELDING:


# class Produce():
#     def __init__ (self, lst):
#         self.lst=lst

#     def __iter__ (self):
#         for i in self.lst:
#             yield i

# numlist=[1,2,3,4,5,6]
# newproduce=Produce(numlist)
# for i in newproduce:
#     print(i)



# class Produce2():
#     def __init__ (self, lst):
#         self.lst=lst

#     def __iter__ (self):
#         for i in self.lst:
#             yield i*2

# numlist=[1,2,3,4,5,6]
# newproduce=Produce2(numlist)
# for i in newproduce:
#     print(i)



# BinarySort 

# def binaryfind(index,lst): 
#     leftpointer=0
#     rightpointer=len(lst)-1
    
#     while leftpointer<rightpointer:
#         midpointer=(leftpointer+rightpointer)//2
#         if index<lst[midpointer]:
#             rightpointer=midpointer-1
#         else:
#             leftpointer=midpointer+1
#     return leftpointer


# lst=[1,2,3,4,5,6,7,8,9,10,20,44]

# print(binaryfind(5,lst))

#Merge Sort 

# def mergesort(lst):
#     if len(lst)>1:
#         leftarray=lst[:len(lst)//2]
#         rightarray=lst[len(lst)//2:]
#         mergesort(leftarray)
#         mergesort(rightarray)

#         leftpointer=0
#         rightpointer=0
#         mergepointer=0

#         while leftpointer<len(leftarray) and rightpointer<len(rightarray):
#             if leftarray[leftpointer]<rightarray[rightpointer]:
#                 lst[mergepointer]=leftarray[leftpointer]
#                 leftpointer+=1
#             else:
#                 lst[mergepointer]=rightarray[rightpointer]
#                 rightpointer+=1
#             mergepointer+=1
        
#         while leftpointer<len(leftarray):
#             lst[mergepointer]=leftarray[leftpointer]
#             leftpointer+=1
#             mergepointer+=1

#         while rightpointer<len(rightarray):
#             lst[mergepointer]=rightarray[rightpointer]
#             rightpointer+=1
#             mergepointer+=1
#     return 

# lst=[1,2,4,4444,52,4,23,4,34324,5,343,1,23,245,2314,5,34,34,3,0]

# mergesort(lst)
# print(lst)



#Quick Sort

# def quicksort(lst,low,high):
#     if low>=0 and high>=0 and low<high:
#         pivot_index=partition(lst,low,high)
#         quicksort(lst,low,pivot_index-1) #This principle is similar to that of binary sorting, divides up the the list indefinitely into 2 and recursively divide it up to two smaller parts 
#         quicksort(lst,pivot_index+1,high) #Notice how the the pivot value is not within the low high range as the position of the pivot has already been sorted from the above function call for partition
        
# def partition(lst,low,high):
#     i=low
#     j=high-1
#     pivot=lst[high]

#     while i<j:
#         while i<high and lst[i]<pivot:
#             i+=1
#         while j>low and lst[j]>=pivot:
#             j-=1
#         if i<j:
#             lst[i],lst[j]=lst[j],lst[i]
#     if lst[i]>pivot:
#         lst[i],lst[high]=lst[high],lst[i]

#     return i

# unsortedlist=[1,20,455,23,45,583,40,1,3,4,5,23]
# quicksort(unsortedlist,0,len(unsortedlist)-1)
# print(unsortedlist)



# def partition(lst,low,high): #low is the lower bound and high is the upper limit of the paritioned lsit, j is all the elemtns that need to be searche d
#     i=low
#     j=high-1
#     pivot=lst[high]

#     while i<j:
#         while i<high and lst[i]<pivot:
#             i+=1
#         while j>low and lst[j]>pivot
#             j-=1
#         if 


# QUICK SORT (does it as a duplicate rather than in place)

# def quicksort(arr):
#     if len(arr)<=1:
#         return arr
#     else:
#         pivot=arr[0]
#         left=[x for x in arr[1:]if x<pivot]
#         right=[x for x in arr[1:]if x>pivot]
#         return quicksort(left) + [pivot] + quicksort(right)

# list1=[1,2,34,2,5,2,24,345,345,23,35,3,124,3245,324,3,5,34,2,34,-234,2343,-3,4,5,0]
# newlist=quicksort(list1)
# print(newlist)



# def quicksort(lst,low,high):
#     if low>=0 and high>=0 and low<high:
#         pivot_index=partition(lst,low,high)
#         quicksort(lst,low,pivot_index-1) #This principle is similar to that of binary sorting, divides up the the list indefinitely into 2 and recursively divide it up to two smaller parts 
#         quicksort(lst,pivot_index+1,high) #Notice how the the pivot value is not within the low high range as the position of the pivot has already been sorted from the above function call for partition


# def quicksortmain(arr,low,high):
#     if low>=0 and high>=0 and low<high:
#         pivot_index=quicksortinplace(arr,low,high)
#         quicksortmain(arr,low,pivot_index-1)
#         quicksortmain(arr,pivot_index+1,high)

# def quicksortinplace(arr,low,high):
#     i=low
#     j=high-1
#     pivot=arr[high]
#     while i<j:
#         while i<high and arr[i]<pivot:
#             i+=1
#         while j>low and arr[j]>pivot:
#             j-=1
#         if i<j:
#             arr[i],arr[j]=arr[j],arr[i]
#     arr[high],arr[i]=arr[i],arr[high]
#     return i #(index of pivot)

# list1=[1,2,34,2,5,2,24,345,345,23,35,3,124,3245,324,3,5,34,2,34,-234,2343,-3,4,5,0]
# quicksortmain(list1,0,len(list1)-1)
# print(list1)




import ctypes;

def makearray(n):
    return (n * ctypes.py_object)();

class ArrayList:
    def __init__(self):
        self.data=makearray(1);
        self.capacity=1;
        self.num_of_elements=0;

    def __len__(self):
        return self.num_of_elements;

    def append(self, item):
        if (self.num_of_elements==self.capacity):
            self.resize(self.num_of_elements*2);
        self.data[self.num_of_elements] = item;
        self.num_of_elements+=1;

    def pop(self, position=-1):
        if position==-1 and self.num_of_elements>0: # Theta (1)
            #self.resize(self.num_of_elements-1);
            temp = self.data[self.num_of_elements];
            self.data[self.num_of_elements-1]=None; #cybersecurity?????
        elif 0<=position<self.num_of_elements: #Theta(n)
            temp = self.data[position];
            for i in range(position,self.num_of_elements-1):
                self.data[i] = self.data[i+1];
        else:
            raise IndexError();

        self.num_of_elements-=1;
        return temp;
        
    def extend(self, iterable):
        size=len(iterable);
        if (self.num_of_elements+size)>self.capacity:
            self.resize(self.num_of_elements+size);
        for item in iterable:
            self.append(item);
        
    def resize(self, newsize):
        newarray = makearray(newsize);

        #copy over the elements
        if (newsize>self.num_of_elements): #new size is larger
            for i in range(self.num_of_elements):
                newarray[i] = self.data[i];
        else: #new size is smaller, not all elements will fit.
            for i in range(newsize):
                newarray[i] = self.data[i];
            self.num_of_elements=newsize;
        self.data = newarray; # not a copy, just an alias
        self.capacity=newsize;

    def __getitem__(self,index):
        if (index<0):
            index+=self.num_of_elements;
        if (0<=index<self.num_of_elements):
            return self.data[index];
        raise IndexError("Invalid Index");

    def __setitem__(self, index, value):
        if (index<0):
            index+=self.num_of_elements;
        if (index<0 or index>=self.num_of_elements):
            raise IndexError("list assignment index out of range");
        self.data[index] = value;
    def index(self, value):
        index = 0;
        while (index<self.num_of_elements):
            if self.data[index] == value:
                return index;
            index+=1;
        raise ValueError(value+" is not in the list");
    def remove(self, value):
        self.pop(self.index(value));
    def count(self, value):
        times =0;
        for i in self:
            if i==value:
                times+=1;
        return times;
    def insert(self, index, value):
        self.append(None);
        for i in range(self.num_of_elements-1, index,-1):
            #self.data[i],self.data[i-1] = self.data[i-1],self.data[i];
            self.data[i] = self.data[i-1];
        self.data[index] = value;
    def clear(self):
        self.data=makearray(1);
        self.capacity=1;
        self.num_of_elements=0;
    def copy(self):
        temp = ArrayList();
        temp.extend(self);
        return temp;
    
def main():
    ls = ArrayList();
    ls.append(100);
    print(ls[0]);
    ls[0] = 200;
    print(ls[0]);
    ls.append(300);
    ls.append(400);
    ls.append(500);
    
    size = len(ls);
    print(size);

    #for item in ls:
    print(ls);
    #temp = ls[1:3]; #Slice datatype so we'll skip that
    #print(temp);
    
    
if __name__=='__main__':
    main();
















import ctypes;

def makearray(n):
    return (n * ctypes.py_object)();

class ArrayList:
    def __init__(self):
        self.data=makearray(1)
        self.capacity=0
        self.num_of_elements=0

    def __len__ (self):
        return self.num_of_elements

    def __getitem__(self):

    def __setitem__(self):






