# Remove all function that is n^2 runtime

def remove_all(lst,value): 
    end=False
    while(end== False): #Linear
        try:
            lst.remove(value) #Linear
        except ValueError:
            end= True

# Worst Run Time: O(n^2)
# there can be n copies of value within the list hence the run time for the while loop is N and subsequently the remove function has to iterate through the list therefore another linear function, a linear function inside a linear funciton will produce a time complexity of n^2
    
# Remove all function that is n runtime

def remove_all(lst,value): 
    leftpointer=0
    print(lst[leftpointer])
    while leftpointer<len(lst)-1:
        if lst[leftpointer]==value:
            lst.remove(lst[leftpointer])
        else:
            leftpointer+=1

lst=[1,2,3,4,5,5,2,3,45,5,4,5,2]
remove_all(lst,5)
print(lst)

# worst case run time for above function: O(n), no matter how long the list is, the leftpointer will only iterate throught every element in the list once, hence a constant time complexity minus the remove method which has linear complexity will produce a final O(n) time complexity


