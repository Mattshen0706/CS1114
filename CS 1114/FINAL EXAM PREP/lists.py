#REVERSE ORDERING A LIST
import copy
values = [ 16, 1, 7, 2, 19, 12, 5, 20, 2, 10, 17, 14, 1, 9]
splicedlist=values[-1:-5:-1]
print(splicedlist)
values.sort()
print(values)
values.reverse()
print(values)


# Take the last 5 elements and flip the order 
splicedlist=values[-1:-5:-1]

print(splicedlist)
splicedlist=values[13:9:-1]
print(splicedlist)



# copy and deepcopies:

import copy

listrial=[[1,2,3,5],[1,2,3,4,5]]
listcopy=copy.copy(listrial)
listcopy.sort(key=len)
print(listcopy)





