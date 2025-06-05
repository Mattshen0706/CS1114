# LISTSSS

#1

# - Reverse a List
# Given a list lst, write code to reverse the entire list using slicing.

# lst = [1, 2, 3, 4, 5]
# reversed_list=lst[::-1]
# print(reversed_list)


#2
# Given a list lst of even length, slice it to extract the middle two elements.
# import copy
# lst = [1, 2, 3, 4, 5, 6]
# newlist=copy.copy(lst)
# print(newlist[(len(newlist)//2)-1:(len(newlist)//2)+1])


#3
# Create a new list that includes every third element from a given list lst
# import copy
# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# newlist=copy.copy(lst)
# for i in range(0,len(newlist),3):
#     print(newlist[i])

#5

# 

# COPIES AND DEEP COPIES 

# 1.
# import copy
# animals=["cat","dog",["rabbit","hamster"]]
# animalshallow=copy.copy(animals)
# animaldeep=copy.deepcopy(animals)
# animalshallow[2][0]="turtle"
# animaldeep[2][0]="lizard"
# print(animals,animalshallow,animaldeep)

# 2.
# import copy
# nested=[1, 2, [3, 4, [5,6]]]
# nesteddeep=copy.deepcopy(nested)
# nestedshallow=copy.copy(nested)
# nestedshallow[2][2][0]=100
# print(nested)
# print(nesteddeep)
# print(nestedshallow)

# 3.
import copy
original_list = [10, 20, [30, 40]]
shallow_copy=copy.copy(original_list)
shallow_copy[2][0]=99
print(original_list)
print(shallow_copy)

# expected output:
# shallow_copy=originalcopy





    
    