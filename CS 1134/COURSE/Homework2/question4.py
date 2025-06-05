
# function is given lst01, a list of integers containing a sequence of 0s folllowed by a sequence of 1s, when it is called it rturns the first occurnace of 1
# e.g 
# if lst01=[0,0,0,0,0,1,1,1]
# the function will return 5

# The function must run in a lograithmic time complexity 

def findChange(lst):
    left=0
    right=len(lst)-1
    while left<=right:
        middle=(left+right)//2

        if lst[middle]==0:
            left=middle+1
        else:
            right=middle-1
    return left

lst01=[0,0,0,0,0,1,1,1]
print(findChange(lst01))


