# DICTIONARY PRACTICE PROBLEMS

# Write a program (Pythonic-style!) that generates 1000 random numbers between 1 and 500
# inclusive. Use a dictionary to count the number of occurrences of each and print a summary
# after the numbers have been generated and counted.

# Problem 1: random number

newdict={}
for i in range (0,1000):
    newrandom=random.randint(1,500)
    if newrandom not in newdict:
        newdict[newrandom]=1
    else:
        newdict[newrandom]+=1
    
print(newdict)

# Problem 2:

# An older, existing campus system has been previously storing student grades in list form with
# the following format:

# grades_list = [ [student_name_1, student_1_id, student_1_midterm,
# student_1_final], [student_name_2, student_2_id, student_2_midterm,
# student_2_final], ... ]

def convert_grades_to_dictionary(gradelist):
    newdict={}
    for outerlist in gradelist:
        for innerlist in gradelist:
            if innerlist[0] not in newdict:
                smalldict={"ID":innerlist[1],"Midterm Grade":innerlist[2],"Final Grade":innerlist[3]}
                newdict[innerlist[0]]=smalldict
    return(newdict)
    
gradelist = [["Emily Kaldwin", "ek12345", 88, 90], ["Sakura Kinomoto", "sk12345", 98, 98], ["Maximilien Robespierre", "mr12345",
76, 89], ["Emily Kaldwin", "ek12345", 100, 100]]
grades_dictionary = convert_grades_to_dictionary(gradelist)

print(grades_dictionary["Sakura Kinomoto"]["ID"]) 


# Problem 3:

updating dictionaries();





                

                








#IF 2 students have the same name, keep the grade of the original


A list of lists where each member list contains the student’s name, ID, midterm exam grade, and
final exam grade. This is a perfectly valid way of storing data, except that when we actually want
to use it, we have to rely on arbitrary indices to access each piece of information. Let’s say one
of the students in our list was: ["Emily Kaldwin", "ek12345", 88, 90]
And she was the 76th (or 75th in a zero-based system) student in our grades_list. In order
to print her midterm grade, we’d have to do the following:
print(grades_list[75][2])
which, for obvious reasons, is inconvenient, has nothing to do with Emily’s actual information,
and thus is tantamount to hard-coding since 75 and 2 look like random numbers.
Write a function, convert_grades_to_dictionary, that will take a list of grades similar to
the one above as a parameter and convert it into a dictionary of grades. If two students have the
same name, your function should assume that this is a mistake, and keep the ID, midterm
grade, and final grade of the original entry. The function should return a dictionary that functions
as below:
grades_list = [["Emily Kaldwin", "ek12345", 88, 90], ["Sakura
Kinomoto", "sk12345", 98, 98], ["Maximilien Robespierre", "mr12345",
76, 89], ["Emily Kaldwin", "ek12345", 100, 100]]
grades_dictionary = convert_grades_to_dictionary(grades_list)
print(grades_dictionary["Sakura Kinomoto"]["NetID"]) # prints
"sk12345"
print(grades_dictionary["Emily Kaldwin"]["Midterm Grade"]) # prints
88
print(grades_dictionary["Maximilien Robespierre"]["Final Grade"])
# prints 89
The use of dictionaries in this case is a lot more natural, since now we would only need to know
the student’s name in order to access their information! Keep in mind that you can nest
dictionaries. For example,
aDictionary = {"date and time": {"date": "June 25th", "time": 1235}}
print(aDictionary["date and time"]["date"]) # prints 'June 25th'

