
#NOTES-------------------------------------------------------------------------------------------
# ITMES ARE A PAIR OF VALUES (KEY AND VALUE)
# FORMAT OF DICTIONARIES:
# dict={key:value,key:value,key:value}
# Keys need to be unique, values can be the same
# Dictionaries support Containmenet


#COMAMNDS-------------------------------------------------------------------------------------------

# popitem = pop for dictionaries
# when you pop a key from a dictionary, you will return the
# popitem will remove the last inserted item and removes and returns the ITEM
# pop will remove the item but return only the value of the item 


#ADD ELEMENTS-------------------------------------------------------------------------------------------

# if ___ not in dicitonary.keys():
#     dictionary[key]=['value']


#TUPLE ITERATIONS-------------------------------------------------------------------------------------------

# for tpl in aread_codes.itmes():
#     print(tpl)


#UNPACKING-------------------------------------------------------------------------------------------
#unpack each tuple as key and value
# for key,value in area_codes.items():
#     print(key,value)

# for item in area_codes.items():
#     print(item[0])
#     print(item[1])


#QUETIONS-------------------------------------------------------------------------------------------   

# QUESTION 1
# student_grades={"Alice":90,"Bob":85,"Charlie":95}


# for key,value in student_grades.items():
#     print(key,value)


# QUESTION 2
# inventory={}
# inventory["apple"]=10
# inventory["bananas"]=5
# inventory["oranges"]=8
# inventory["apple"]=15

# print(inventory)


# QUESTION 3
# inventory={'apples':10,"bananas":5,"oranges":8}
# inventory.pop("bananas")

# print(inventory)


# QUESTION 4
# capitals={"France":"Paris","Germany":"Berlin","Italy":"Rome","Spain":"Madrid"}
# if "Spain" in capitals:
#     print("Capital of Spain is:", capitals["Spain"])
# else:
#     print("No information available for Spain")


# QUESTION 5
# colors={'apple':'red','banana':'yellow','grape':'purple'}
# for key,value in colors.items():
#     print(f'The color of {key} is {value}')


# QUESTION 6
# population ={'China': 1400, 'India': 1350, 'USA': 330,'Japan':150}
# populationjapan=population.get("Mexico", "Population data not available")
# print(populationjapan)

# QUESTION 7
# fruits = ['apple', 'banana', 'apple', 'orange', 'banana','apple']
# fruitcount={}
# for fruit in fruits:
#     if fruit not in fruitcount:
#         fruitcount[fruit]=1
#     else:
#         fruitcount[fruit]+=1
# print(fruitcount)


# QUESTION 8
# course_students={"CS101":["Charlie","David"],"CS102":["Alice","Bob"]}
# studentsincs101=course_students.get('CS101')
# studentsincs101.append("Eve")
# course_students["CS101"]=studentsincs101
# print(course_students)

# course_students={"CS101":["Charlie","David"],"CS102":["Alice","Bob"]}
# course_students["CS101"].append("Eve")
# print(course_students)


# QUESTION 9
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# dict1.update(dict2)
# print(dict1) 

# VALUE OF SAME KEY GETS REPLACED BY THE NEWER UPDATE


# QUESTION 10
# DICTIONARY OF SQUARE NUMBERS
# squareinput=int(input("Enter how many square numbers you want:"))
# squaredict={}
# for i in range(1,squareinput+1):
#     squaredict[i]=i**2
# print(squaredict)


# QUESTION 11

# PART 1: FROM CODE TO FILE
# employeedict={101:("Alice","HR",55000),102:("Bob", "Engineering", 75000),103:("Charlie", "Sales", 65000),104:("David", "Engineering", 80000),105:("Eve", "HR", 50000)}
# with open("employees.txt","w")as writefile:
#     for key,value in employeedict.items():
#         print(key, end=" ",file=writefile)
#         for elements in value:
#             print(elements,end=" ",file=writefile)
#         print(file=writefile)

# PART 2: FROM FILE TO CODE
# datadict={}
# with open ('employees.txt',"r")as readfile:
#     for lines in readfile:
#         linestring=lines
#         linelist=linestring.split(' ')
#         datadict[linelist[0]]=(linelist[1],linelist[2],linelist[3])
# print(datadict)


# PART 3: APPENDING PEOPLE TO CODE:
  
# def add_employeeID(datadict):
#     with open("employees.txt","w")as writefile:
#         new_employee=input("Enter a new/existing ID, (Q) to quit: ")
#         new_employeedata=[]
#         while new_employee!="Q":
#             new_employeedata.append(input("Enter the employees name: "))
#             new_employeedata.append(input("Enter the employees position: "))
#             new_employeedata.append(input("Enter the employees salary: "))
#             new_employeedata=tuple(new_employeedata)
#             datadict[new_employee]=new_employeedata
#             new_employee=input("Enter a new/existing ID, (Q) to quit: ")
#             new_employeedata=[]
#         for key,value in datadict.items():
#             print(key, end=" ",file=writefile)
#             for elements in value:
#                 print(elements,end=" ",file=writefile)
#             print(file=writefile)

# def main():
#     datadict={}
#     with open ('employees.txt',"r")as readfile:
#         for lines in readfile:
#             linestring=lines
#             linelist=linestring.split(' ')
#             datadict[linelist[0]]=(linelist[1],linelist[2],linelist[3])
#         print(datadict)
#     add_employeeID(datadict)
        
# main()


# PART 4: AVERAGE SALARY OF ALL DEPARTMENTS:

# with open("employees.txt","r") as readfile:
#     departmentsalary={}
#     for lines in readfile:
#         linestring=lines
#         linelist=linestring.split()
#         if linelist[2] not in departmentsalary:
#             departmentsalary[linelist[2]]=int(linelist[3])
#         else:
#             departmentsalary[linelist[2]]+=int(linelist[3])
# print(departmentsalary)
        
# PART 5: AVERAGE SALARY OF ALL DEPARTMENTS:




#MORE DICTIONARY PRACTICE:

#1.

# def template(map):
#     for elements in map:
#         if elements=="dog":
#             return(map["dog"])
#         else:
#             return(-1)
        
# def main():
#     animalmap={"dog":25,"cat":40204,"elephant":1}
#     template(animalmap)

#2.
#     accounts={"saving":100,"checking":150}
# def checkfunds(amt,chargeto):
#     accounts[chargeto]-=amt

# def main():

#     withrdrawamaount=int("input amount to be withdrawn")
#     checkfunds(withrdrawamaount,"saving")  


#3.  
#         
# d1 = {'a':'a', 'b':'b', 3:'c', 'x':'5', 'y':'6', 'z':'7'}
# d2 = {1:'111', 3:'222', 4:'333', 'y':'6', 'z':'7'}  
# newd={'a':'a', 'b':'b', 3:'c', 'x':'5', 'y':'6', 'z':'7'}

# d1 = {'a':'a', 'b':'b', 3:'c', 'x':'5', 'y':'6', 'z':'7'}
# d2 = {1:'111', 3:'222', 4:'333', 'y':'6', 'z':'7'}
# newd = {'a':'a', 'b':'b', 3:'c', 'x':'5', 'y':'6', 'z':'7'}

# for key2 in d2.keys():
#     if key2 in newd:
#         newd[key2]+=d2[key2]
#     else:
#         newd[key2]=d2[key2]
    
# print(newd)

#4.  

# def check_sentance(sentance):
#     wordcount={}
#     new_list=sentance.split()
#     lastword=""
#     count=0
#     for i in new_list:
#         if i==lastword and i not in wordcount:
#             wordcount[i]=1
#         elif i==lastword:
#             wordcount[i]+=1
#         lastword=i
#     return wordcount

# def main():
#     sentance=input("Enter a sentance: ")
#     print(check_sentance(sentance))

            
# main()
        

        
        




