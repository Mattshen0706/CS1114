list1=[1,2,3,"HELLO",4,5,6,"WORLD",7,8,9]

list1.extend("YES")
print(list1)

print("------------------------------------------------------------------------------------")

list1.append("YES")
print(list1)

print("------------------------------------------------------------------------------------")

list1.extend(["YES"])
print(list1) #(EXTENDING A LIST WILL CREATE A SINGULAR ELEMENT, MAKING THE LIST INTO A STRING)

print("------------------------------------------------------------------------------------")

list1.append(["HELLOWOLRD"]) 
print(list1)

print("------------------------------------------------------------------------------------")

list1.pop() #(REMOVE BASED OFF OF INDEX)
print(list1)

print("------------------------------------------------------------------------------------")

list1.remove("HELLO")  #(REMOVE BASED OFF OF VALUE)
print(list1)

if list1[0]==1:
    print("ABRACADABRA")

num = int(input("WHAT is your favrouite number"))
if num<50:
    print("EH")
elif num<100: #elif (num<=50 and num<100) IS INCORRECT, DUE TO PROGRAM INEFFICIENCY 
    print("OK")
else:
    print("BAD")




class Thing:
    def __init__(self,val):
        self.val = val
    def set_val(self,newval):
        self.val=newval
    def get_val(self):
        return self.val
    def __lt__ (self,other):
        return self.val<other
    def __gt__ (self,other):
        return other<self.val
    def __ge__(self,other):
        return not other<self.val
    def __le__(self,other):
        return not other>self.val
    def __add__(self,other):
        return Thing(self.val + other.val)
    def __str__(self):
        return self.val
    
obj1=Thing(1)
obj2=Thing(3)

print(obj1+obj2)