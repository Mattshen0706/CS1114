#QUESITON 1

# students = [
# ("Alice Johnson", 101, [("Math", 95.0, 3), ("History", 87.5, 4), ("Physics", 92.0, 3)]),
# ("Bob Smith", 102, [("Math", 76.0, 3), ("History", 83.0, 4), ("Biology", 89.5, 4)]),
# ("Charlie Brown", 103, [("Math", 85.0, 3), ("History", 78.0, 4), ("Chemistry", 91.0, 3)]),
# ]


# def calculate_gpa(student_data):
#     totalGPA=0
#     totalcredit=0
#     GPA_LIST=[]
#     for students in student_data:
#         for elements in students[2]:
#             totalGPA+=elements[1]*elements[2]
#             totalcredit+=elements[2]
#         GPA_LIST.append([students[0],totalGPA/totalcredit])
#         totalGPA=0
#         totalcredit=0
#     return GPA_LIST


# def main():
#     datafunction=input("WHAT WOULD YOU LIKE TO KNOW(Student GPA(1), Student Ranking (2), Course Average(3)):")
#     if datafunction=="1":
#         print(calculate_gpa(students))
# main()


#PROBLEM 1 DEPASCUALE
# import random 
# innerlist=[]
# outerlist=[]
# sum=0
# count=0
# for i in range(0,5):
#     for j in range(0,5):
#         innerlist.append(round(random.uniform(0.0,10.0),1))
#     outerlist.append(innerlist)
#     innerlist=[]

# for data1 in outerlist:
#     for data2 in data1:
#         sum+=data2
#         count+=1

# average=sum/count
# print(outerlist)
# print(average)


#PROBLEM 2 DEPASCUALE


# def get_nucleotide_frequency(dna):
#     character_dict={}
#     character_list=[]
#     for char in dna:
#         if char not in character_dict:
#             character_dict[char]=1
#         else:
#             character_dict[char]+=1

#     for key,value in character_dict.items():
#         character_list.append((key,value))
#     return character_list

# def main():
#     dna = "ACGTTTTCCCCCA"
#     print(get_nucleotide_frequency(dna))

# main()
#PROBLEM 3 DEPASCUALE
#Problem 3: update_frequencies


# def get_nucleotide_frequency(dna):
#     character_dict={}
#     character_list=[]
#     for char in dna:
#         if char not in character_dict:
#             character_dict[char]=1
#         else:
#             character_dict[char]+=1

#     for key,value in character_dict.items():
#         character_list.append((key,value))
#     return character_list

# def update_frequency(newlist,oldformatlist):
#     oldformatlisted=[]
#     for elements in oldformatlist:
#         oldformatlisted.append(list(elements))

#     for char in newlist:
#         for i in range(0,len(oldformatlisted)):
#             if char==oldformatlisted[i][0]:
#                 oldformatlisted[i][1]+=1
#     return oldformatlisted

# def main():
#     dna = "ACGTTTTCCCCCA"
#     current_frequency= get_nucleotide_frequency(dna)
#     new_sequence="AACCTTAGG"
#     current_frequency=update_frequency(new_sequence,current_frequency)
#     print(current_frequency)
# main()



# Problem 5:
# import random
# dataset=[]
# name_list=["Matt Shen","Ella Chuang","Cheng Yu","Shirley Lin","Dylan Wu","Shen Jian","Ivy Yang","Maxime Bell","Brion Chew"]
# major_list=["math","physics","chemistry","biology","economics","buisness","electricalengineering","mechanicalengineering"]
# for elements in name_list:
#     dataset.append((elements,major_list[random.randint(0,len(major_list)-1)],round(random.uniform(0.0,4.0),2),random.randint(0,120)))

# for elements in dataset:
#     print(elements)
#     print()


