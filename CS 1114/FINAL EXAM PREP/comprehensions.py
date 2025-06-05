# Problem 1/Problem 2: Simple-ish Dictionary Building with Random data

# Use a dictionary comprehension to create a dictionary which has key values in the range of
# 1-100. Each entry should have a value that is a random number between -100.0 and 100.0
# (floats!) inclusive. Print the contents of the dictionary once it is created.
# Example output:
# {1: -7.846764512786876, 2: 66.41690885729574, 3: -32.54890492255491, 4:
# 63.80228782158633, 5: 0.8680812036612906, … }

import random 
numberofterms=10
newdict={term:float(f'{random.uniform(1,100):.3f}') for term in range(1,numberofterms+1)}
print(newdict)



# Problem 3: Words

# Write a program to read the contents of the file into a list. You can do this with a list
# comprehension, so try to do so! (Hint: you have to open the file first but the LC can be inside of
# the with open statement…) But if you simply can't, do it without a LC and figure that out later…
# Print the length of the list. How many "words" did you read? Next…
# Write a dictionary comprehension that builds a dictionary where each word is a key and the
# value that is stored is a tuple. The tuple will comprise two integer values: the length of the word,
# and the sum of the ordinal values of the characters that comprise the word.
# For example, if the list starts with the following:
# ['a', 'aa', 'aaa', 'aah', 'aahed', 'aahing', 'aahs', 'aal', 'aalii', ...]
# The resulting dictionary should be:
# {'a': (1, 97), 'aa': (2, 194), 'aaa': (3, 291), 'aah': (3, 298), 'aahed': (5,
# 499), 'aahing': (6, 616), 'aahs': (4, 413), 'aal': (3, 302), 'aalii': (5,
# 512), ...}
# Hint: when building the tuple (in the expression portion, you may need to call a function you
# write to compute the second value of the tuple!)

def readingfile(filename):
    try:
        with open(filename,"r") as readfile:
            newlist=[line for line in readfile]
            strippedlist=[line.strip("\n ") for line in newlist]
            print(len(strippedlist))
            newdict={element:(len(element),sumoford(element)) for element in strippedlist}
            print(newdict)

    except FileNotFoundError:
        print ("File does not exit")
    
def sumoford(element):
    sum=0
    for char in element:
        sum+=int(ord(char))
    return sum

def main():
    filename="comprehensionq.txt"
    readingfile(filename)

main()


# Problem 4: Reading File Data

# Given an input file of student data:

# n_number,first_name,last_name,gpa,grad_year
# N69367,Germayne,Summersby,0.853,2024
# N60829,Joann,Gellett,0.102,2023
# N50434,Josey,Poundford,1.466,2025
# N65334,Leighton,Runsey,1.168,2027
# N47787,Hephzibah,Bemrose,1.93,2024
# N61638,Cori,Haselhurst,3.886,2027
# N50023,Loise,Van Velden,2.829,2023
# N43151,Lindy,Haffner,3.062,2024
# N47613,Chandra,Keneleyside,1.469,2024
# N70164,Margot,Jeannenet,2.266,2024
# N42114,Coralie,Churchin,0.556,2027
# N79364,Mela,Tweedlie,2.847,2023

# Write a function that opens the file and reads the file, populating a dictionary of student values.
# The key is the student N-number, and the rest of the data is a sub-dictionary. Use a list
# comprehension to read the data, create the sub-dictionary, and populate the dictionary. The
# function should return the dictionary.
# The resulting dictionary would look like this (the start of it anyway…):
# {'N69367': {'first_name': 'Germayne', 'last_name': 'Summersby', 'gpa': '0.853',
# 'grad_year': '2024'},
# 'N60829': {'first_name': 'Joann', 'last_name': 'Gellett', 'gpa': '0.102', 'grad_year':
# '2023'},
# 'N50434': {'first_name': 'Josey', 'last_name': 'Poundford', 'gpa': '1.466', 'grad_year':
# '2025'},
# …}
# Hint:
# ● The dictionary comprehension will need to:
# ○ Read each line of the file
# ○ Split the line
# ○ Access the data
# ○ Build the dictionary and sub-dictionary entries


def createdict(filename):
    try:
        with open (filename,"r") as readfile:
            firstline=readfile.readline().strip('\n')
            firstline=firstline.split(',')
            studentdict={}
            for line in readfile:
                newline=line.strip().split(",")
                key = newline[0]
                studentdict[newline[0]]={firstline[i]:newline[i] for i in range(1,len(newline))}
                
            print(studentdict)

    except FileNotFoundError:
        print ("This file does not exist")



#HOMEWORK QUESTIONS FOR COMPREHENSIONS:

# Write a function group_students that organizes students into clubs based on their preferences.
# The function should take two arguments:

def clubsort(clubspecs,studentpref):
    # return a list of lists
    clubdiction={innerel[0]:innerel[1] for innerel in clubspecs}
    finaldict={}
    for students in studentpref: 
        if students[1] in clubdiction:
            if clubdiction.get(students[1])!=0:
                finaldict[students[1]]+=students[0]
                clubdiction["students[1]"]-=1
    finallist=[[value] for key,value in finaldict.items()]
    for listel in finallist:
        print(listel)
        print()

def main():

    club_specs = [("Chess Club", 15), ("Art Club", 20), ("Writing Club", 3)]

    student_prefs = [
    ("Alice", "Chess Club"),
    ("Bob", "Chess Club"),
    ("Flora", "Writing Club"),
    ("Charlie", "Art Club"),
    ("David", "Writing Club"),
    ("Melody", "Writing Club"),
    ("Ana", "Writing Club")
    ]
    clubsort(club_specs,student_prefs)

main()




# 1. A list of club specifications, where each club specification is a tuple containing the name of
# the club and its maximum capacity. For example:
# club_specs = [("Chess Club", 15), ("Art Club", 20), ("Writing Club", 3)]
# 2. A list of students' preferences, where each student preference is a tuple containing the
# student's name and the preferred club. For example:
# student_prefs = [
# ("Alice", "Chess Club"),
# ("Bob", "Chess Club"),
# ("Flora", "Writing Club"),
# ("Charlie", "Art Club"),
# ("David", "Writing Club"),
# ("Melody", "Writing Club"),
# ("Ana", "Writing Club")
# ]
# The function should return a list of lists, where each inner list represents the students
# assigned to a particular club. The assignment process should follow these rules:
# ● Each student is assigned to their preferred club if there are available seats.
# ● If a club has no available seats for a student, that student should be excluded from the
# results.
# Here is a sample execution:
# print(group_students(club_specs, student_prefs))
# Expected Output:
# [
# ['Alice', 'Bob'],
# ['Charlie'],
# ['Flora', 'David', 'Melody']
# ]
# Explanation:
# ● Alice and Bob both prefer the Chess Club, and there are 15 seats available. Therefore, both Alice and Bob will be
# assigned to the Chess Club.
# ● Charlie prefers the Art Club, and there are 20 seats available. Therefore, Charlie will be assigned to the Art Club.
# ● Flora, David, Melody, and Ana prefer the Writing Club. However, there are only 3 seats available. Therefore, only
# the first 3 students (Flora, David, Melody) will be assigned to the Writing Clu


def clubsort(clubspecs,studentpref):
    # return a list of lists
    clubdiction={innerel[0]:innerel[1] for innerel in clubspecs}
    finaldict={}
    for students in studentpref:
        clubpref=students[1]
        studentname=students[0]
        if students[1] in clubdiction:
            if clubdiction.get(clubpref)!=0:
                if finaldict.get(clubpref)==None:
                    finaldict[clubpref] = []
                    finaldict[clubpref].append(studentname)
                else:
                    finaldict[clubpref].append(studentname)
                clubdiction[clubpref]-=1
    finallist=[value for key,value in finaldict.items()]
    for listel in finallist:
        print(listel)
        print()

def main():

    club_specs = [("Chess Club", 15), ("Art Club", 20), ("Writing Club", 3)]

    student_prefs = [
    ("Alice", "Chess Club"),
    ("Bob", "Chess Club"),
    ("Flora", "Writing Club"),
    ("Charlie", "Art Club"),
    ("David", "Writing Club"),
    ("Melody", "Writing Club"),
    ("Ana", "Writing Club")
    ]
    clubsort(club_specs,student_prefs)

main()


# Question 03: Word Frequency and Index Tracker

def word_frequency(filename):
    
    try:
        with open (filename, "r") as readfile:
            wordbank={}
            for line in readfile:
                newline=line.strip().split()
                for word in newline:
                    if word not in wordbank:
                        wordbank[word]=[1,[newline.index[word]]]
                    else:
                        wordbank.get[word][0]+=1
                        wordbank.get[word][1].append(word)

    except FileNotFoundError:
        print(filename,"does not exist")
    
    if wordbank=={}:
        return "None"
    else:
        return wordbank
    
def main():
    filename=".txt"
    word_frequency(filename)


# Write a function word_frequency_counter that takes the path to a text file as input. The file
# contains multiple lines of space-separated words, and the function should read each line as a separate
# string. It should return a dictionary where keys are unique words in the text, and values are tuples
# containing the word's frequency and the positions where the word appears across all lines. The
# position is relative to the line where the word appears..
# A sample_file.txt file could look like this:
# apple banana orange banana apple
# grape apple banana
# orange banana grape
# Your function should handle exceptions gracefully, considering scenarios such as an invalid file path. If an
# exception occurs, the function should print an informative error message and return None.
# For example:
# word_stats = word_frequency_counter_from_file("invalid_file.txt")
# print(word_stats)
# The expected output should be:
# Error: Unable to read the file. Please check the file path.
# None
# In a successful scenario, using the provided sample file:
# word_stats = word_frequency_counter_from_file("sample_text.txt")
# print(word_stats)
# The expected output should be similar to:
# {
# 'apple': (3, [0, 4, 1]),
# 'banana': (4, [1, 3, 2, 1]),
# 'orange': (2, [2, 0]),
# 'grape': (2, [0, 2])
# }
# In this example,
# 'apple': (3, [0, 4, 1]), The word 'apple' appears 3 times in the multiline text, at positions 0, 4, and 1.
# 'banana': (4, [1, 3, 2, 1]), The word 'banana' appears 4 times, at positions 1, 3, 2, and 1.
# 'orange': (2, [2, 0]), The word 'orange' appears twice in the multiline text, at positions 0 and 4.
# 'grape': (2, [0, 2]), The word 'grape' appears twice in the multiline text, at positions 0 and 2.

def word_frequency(filename):
    try:
        with open (filename, "r") as readfile:
            wordbank={}
            for line in readfile:
                newline=line.strip().split()
                count=0
                for word in newline:
                    if word not in wordbank:
                        wordbank[word]=[1]
                        wordbank[word].append([count])
                    else:
                        wordbank[word][0]+=1
                        wordbank[word][1].append(count)
                    count+=1

    except FileNotFoundError:
        print(filename,"does not exist")
    
    if wordbank=={}:
        return "None"
    else:
        return wordbank
    
def main():
    filename="comprehensionq.txt"
    print(word_frequency(filename))
    
main()

numbers = [1,2,3,4,5]
newnumber=[number*2 for number in numbers]

words=["bears","eat","blue","berry"]
newlist=[word for word in words if word.startswith("b")]

fruits=["apple","banana","cherry"]
newlist=[fruit for fruit in fruits if fruit[0] not in "aeiou"]

student_grades = [("Alice",80),("Bob",90),("Charlie",95),("Dave",85)]
gradesorted = [student for student in student_grades if student[1] >=90]

horoscopes = ["Aries", "Taurus", "Gemini", "Cancer", "Leo",
"Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
horoscope_list = [horoscope for horoscope in horoscopes if len(horoscope)<5]


