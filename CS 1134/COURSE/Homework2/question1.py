# Fibonacci Sequence :

# 1,1,2,3,5,8,13,21,34,55

# def fibs(n):
# returns a generator that when iterated over it will have the first n elements in the fibonacci sequence 

# e.g 

def fibs(n):
    fiblist=[]
    for i in range (0,n):
        if len(fiblist)==0 or len(fiblist)==1:
            fiblist.append(1)
        else:
            fiblist.append(fiblist[-1]+fiblist[-2])
        yield fiblist[-1]
 
for curr in fibs(8):
    print (curr)


