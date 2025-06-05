CLASSES

class Name:
    def __init__(self, firstName, mi, lastName):
        self.firstName = firstName
        self.mi = mi
        self.lastName = lastName

firstName = "John"
name = Name(firstName, 'F', "Smith")
firstName = "Peter"
name.lastName = "Pan"
print(name.firstName, name.lastName)

 A. True False
 B. True True
 C. False True
 D. False False





class Count:
    def __init__(self, count = 0):
       self.__count = count

c1 = Count(2)
c2 = Count(2)
print(id(c1) == id(c2), end = " ")

s1 = "Good"
s2 = "Good"
print(id(s1) == id(s2))
 A. True False
 B. True True
 C. False True
 D. False False






class MyDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

class Name:
    def __init__(self, firstName, mi, lastName, birthDate):
        self.firstName = firstName
        self.mi = mi
        self.lastName = lastName
        self.birthDate = birthDate

birthDate = MyDate(1990, 1, 1)
name = Name("John", 'F', "Smith", birthDate)
birthDate = MyDate(1991, 1, 1)
birthDate.year = 1992
print(name.birthDate.year)
 A. The program displays 1990.
 B. The program displays 1991.
 C. The program displays 1992.
 D. The program displays no thing.




To concatenate two strings s1 and s2 into s3, use _________.
 A. s3 = s1 + s2
 B. s3 = s1.add(s2)
 C. s3 = s1.__add(s2)
 D. s3 = s1.__add__(s2)



Suppose t = (1, 2), 2 * t is _________.
 A. (1, 2, 1, 2)
 B. [1, 2, 1, 2]
 C. (1, 1, 2, 2)
 D. [1, 1, 2, 2]
 E. illegal


 Suppose t1 = (1, 2, 4, 3) and t2 = (1, 2, 3, 4), t1 < t2 is ________.
 A. True
 B. False



Suppose s = {1, 2, 4, 3}, which of the following is incorrect?
 A. print(s[3])
 B. s[3] = 45
 C. print(max(s))
 D. print(len(s))
 E. print(sum(s))


Suppose d1 = {"john":40, "peter":45} and d2 = {"john":466, "peter":45}, d1 > d2 is _______.
 A. True
 B. False
 C. illegal


 Suppose d = {"john":40, "peter":45}, to delete the entry for "john":40, use ________.
 A. d.delete("john":40)
 B. d.delete("john")
 C. del d["john"]
 D. del d("john":40)



What does this output: 
newdict={"name1":20,"name2":30,"name3":1246,"name4":213}

del newdict["name1"]
print(newdict.pop("name2"))
print(newdict.popitem())
print(newdict)

del for dictionary, deletes the item from the dictionary and does not return anything
.pop() for dicitonary, you must specify the key and will return the value but remove the item from the dict
.popitem() for dictionary, you dont have to specify the key, it will only auomatically pop the last item in the dict and return it as a tuple



Suppose d = {"john":40, "peter":45}, what happens when retieving a value using d.get("susan")?
 A. Since "susan" is not a value in the set, Python raises a KeyError exception.
 B. It is executed fine and no exception is raised, and it returns None.
 C. Since "susan" is not a key in the set, Python raises a KeyError exception.
 D. Since "susan" is not a key in the set, Python raises a syntax error.

IMPORTANT!!!
.get wont return an error if the key isnt present in the dictionary but instead will return none

