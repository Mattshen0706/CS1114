ls1=[1,1]

for i in ls1:
    if ls1[-1]<500:
        ls1.append(ls1[-1]+ls1[-2])
        print(ls1[-1])

def func1(val=10):
    return val

def coolprint():
    for i in range(0,10):
        print(func1(i))
    

coolprint()
    
lst2=[1,2,3,4,5,6,7,8]
lst3=lst2*2
print(lst3)
print(lst2)


lst4=[1,2,3,4,5,6]
lst5=lst4+[8]
print(lst5)
print(lst4)

neword="WORLD"
lst6=["HELLO"]
lst6.extend(neword)
print(lst6)