# def shift(lst,k):
#     given a list of n numbers and some postivie intgeer k where k<N
#     function should shift the numbers circularly k steps to the left 

#     shift has to be done in place, should not need to create and return a new list 

#     example: 
#     if lst=[1,2,3,4,5,6]
#     shift(lst,2)
#     lst will be [3,4,5,6,1,2]

# a) 


def shift(lst,k):
    startposition=k
    for i in range(0,k):
        lst.append(lst[i])
    return lst[startposition:]

lst=[1,2,3,4,5,6]
print(shift(lst,2))


# b) 

# potentially pass in a third arguemnt stating either left or right:
# if only 2 paramters pass in, direction will default to left 

#     example: 
#     if lst=[1,2,3,4,5,6]
#     shift(lst,2,right)
#     lst will be [5,6,1,2,3,4]

def shift(lst,k,direction="left"):
    if direction=="left":
        startposition=k
    else:
        startposition=len(lst)-k
    for i in range(0,startposition):
        lst.append(lst[i])
    return lst[startposition:]


lst=[1,2,3,4,5,6]
print(shift(lst,2,"right"))





