# A class is a blueprint for creating different versions of an object

# A class is a seperate file which can later be imported into

# First thing that runs in a class is __new__ (new is automatically built into the python interpreter)
# Second thing that runs in a class is __init__ (init is what gives the object its properties)


# NAMING CONVENTIONS:

# for Class --- Should start with a Capital:

# for variables --- lower_snake_casing


# class Car:

#     def __init__(self,ma,mo,ye):
#         self.make=ma
#         self.model=mo
#         self.year=ye

#     def start (self):
#         print(self.model,"is starting......")

# def main():
#     car1=Car("BMW","X6",2025)
#     car2=Car("Benz","TX2",2022)
#     car1.start()
#     car2.start()


# main()


# PRACTICE CLASS IN CLASS PROBLEM:

#PROBLEM 1
# class Dog:

#     def __init__(self,name,age):
#         self.name=name
#     def bark(self):
#         print("Woof! My name is", self.name)
    
# def main():
#     dog1=Dog("Charlie",5)
#     dog2=Dog("Milo",3)
#     dog1.bark()
#     dog2.bark()

# main()


#PROBLEM 2
# class Square:

#     def __init__(self,side_length):
#         self.side_length=side_length

#     def area(self):
#         print("The area of square with side length ",self.side_length ,"  is ", self.side_length**2)
#         return "hello"
    
# def main():
#     square1=Square(20)
#     print(square1.area())

# main()


#PROBLEM 3
# class StudentModel:
#     def __init__ (self,name,grade):
#         self.name=name
#         self.grade=grade
    
#     def update_grade(self):
#         self.grade=float(input("New Grade)"))
    
#     def method_display(self):
#         print(f"studen: {self.name}, Grade {self.grade}")

# def main():
#         st1=StudentModel("Cheng",1)
#         st2=StudentModel("Bob",1)
#         st1.update_grade()
#         st1.method_display()
# main()


# LESSON NOTES 23 APR ------------------------------------------

# what gets called when you use a print fucntion on a class 

# class Student:
#     def __init__ (self,name,age):
#           self.name=name
#           self.age=age
    
#     def __str__(self):
#      return f"({self.name},{self.age})"
    
#     def __repr__(self):
#         return f"({self.name},{self.age})"
    
#     __str__ will be used automatically as the print call back function
#     __repr__ will be used as a backup in case __str__ does not exist. However you can call repr in your main function if you want to call that

# def main():
#     student1=Student("Ana",18)
#     student2=Student("Tom",20)
#     major="CS"
#     print(major)
#     print(repr(student1))
    
import random

class Instrument:

    def __init__(self,model,brand,strength):
        self.model=model
        self.brand=brand
        self.strength=strength

    def __str__(self):

        return f"{self.model},{self.brand},({self.strength*100}/100 strength)"

    def does_break(self):  
        return self.strength < random.uniform(0, 1)

    # def get(self):

    # def set(self):


class Musician:
    def __init__(self,stage_name,instruments,number_of_instruments):
        self.stage_name=stage_name
        self.instruments=instruments
        self.number_of_instruments=number_of_instruments

    def __str__(self):
        instruments_str = ", ".join(str(instrument) for instrument in self.instruments)
        return f"{self.stage_name}: [{instruments_str}], Total Instruments: {self.number_of_instruments}"
        
    def pick_instrument(self,instrument_index="None"):
        self.instrument_index=instrument_index
        if self.number_of_instruments==0:
            return "None"
        if self.instrument_index>self.number_of_instruments:
            return self.instruments[-1]

def main():
    fender_vi = Instrument("VI Bass", "Fender", 0.99)
    print(fender_vi.model)
    print(fender_vi.brand)
    print(fender_vi.strength)
    Piano = Instrument("VI Bass", "Fender", 0.99)
    Violin = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
    print(fender_vi)
    print(four_double_o_one)  
    print (four_double_o_one.does_break())       

    number_of_test=100
    breaks=0
    for i in range(0,number_of_test):
        if four_double_o_one.does_break()==True:
            breaks+=1    

    print(f"The string broke a totle of {breaks} times")            

    listofinstruments=[Piano,Violin,"Drums"]
    Albert=Musician("Alberto",listofinstruments,len(listofinstruments))
    print(Albert)

main()


#CREATING MUSICIAN OBJECTS



#CLASS LESSON 3:

class Animal:
    def __init__(self,species,legs):
        self.species=species
        self.legs=legs
    
    def has_fur(self):
        return self.species in ["dog","cat","rabbit"]

    def has_feathers(self):
        return self.species=="parrot"

    def __str__(self):
        return f"{self.species}({self.legs})"
    
    def __repr__(self):
        return f"Animal({self.species},{self.legs})"
    
def main():
    dog=Animal("dog",4)
    parrot=Animal("parrot",2)
    cat=Animal("cat",4)
    snake=Animal("snake",0)
    animals=[snake,dog,parrot,cat]

main()

print(sum([animal.legs for animal in animals if animals.has_fur()]))

dog and cat in has has fur 

sum[4,4]=8




class Character:

    def __init__(self,name, species,color,description):
        self.name=name
        self.species=species
        self.color=color
        self.description=description

    def __str__(self):
        return f"{self.name},{self.species},{self.color},{self.description}"


class Episode:

    def __init__(self,string,air_date,characters):
        self.string=string
        self.air_date=air_date
        self.characters=characters
    
    def add_character(self,character):
        self.characters.append(character)
    
    def display_characters(self):
        for elements in self.characters:
            print(elements)

def main():
    characterlist=[]
    bobby=Character("bobby","bird","red","He is one fat bird")
    tyler=Character("tyler","dog","brown","He is one long dog")
    characterlist.append(bobby,tyler)
    episode1=Episode("ep1","Jan 5th 2024",characterlist)
    episode1.display_characters()
