# # Problem 1.1:x
# 82

# # Problem 1.2:
# Oleg

# # Problem 1.3:
# {"Kimberly" : 13, "Amalie" : 27, "Mariam" : 19, "Oleg" : 23}


# # Problem 2:
# my_dict = {"a": 15 , "c": 35 , "b": 20}

# a) 
# for key in my_dict:
#     print(key)

# b)
# for key in my_dict:
#     print(my_dict.get(key))

# c)
# for key,value in my_dict.items():
#     print(key,value)

# d)
# keylist=[]
# valuelist=[]
# my_dict = {"a": 15 , "c": 35 , "b": 20}
# for key,value in my_dict.items():
#     keylist.append(key)
#     valuelist.append(key)
#     keylist.sort()
    
# for keys in keylist:
#     print(keys, my_dict[keys])
    

# Problem 3:

# def readfile():
#     emptydict={}
#     try:
#         readfile=open("LABS/sample_text.txt","r")
#         output=count_vowels("LABS/sample_text.txt")
#         print(output)
#         readfile.close()
#     except FileNotFoundError:
#         print(emptydict)

# def count_vowels(filename):
#     new_dict={}
#     with open (filename,"r") as readfile:
#         for lines in readfile:
#             newline=lines
#             lines=lines.upper()
#             lines=lines.strip()
#             lines=lines.replace(" ","")
#             for char in lines:
#                 if char in "AEIOU":
#                     if char not in new_dict:
#                         new_dict[char]=1
#                     else:
#                         new_dict[char]+=1
#     return new_dict

# readfile()

# Problem 4:
import copy
# def sentence_cleaner(string1):
#     newlist=[]
#     newstring=copy.copy(string1)
#     newstring=newstring.strip()
#     stringlist=newstring.split()
#     for elements in stringlist:
#         if elements not in newlist:
#             newlist.append(elements)
#         # elif elements.isalpha()==False:
#         #     newlist.append(elements)
#     for elements in newlist:
#         print(elements,end=" ")

# def main():
#     sentance='I love cats, I love fish, and I love birds, but I love dogs more than all of them'
#     sentence_cleaner(sentance)

# main()


# Problem 5:
# def merge_databases(database1,database2):
#     dict1=database1
#     dict2=database2
#     allids=[]
#     for keys in dict1:
#         allids.append(keys)
#     for keys in dict2:
#         allids.append(keys)
    
#     allids.sort()
#     lastid=allids[-1]
#     lastid+=1
    
    
#     for elements in dict2:
#         if elements not in dict1:
#             dict1[elements]=dict2[elements]
#         else:
#             dict1[lastid]=dict2[elements]
#             print(dict2[elements][0],"had their employee number changed from", elements, "to", lastid)
#             lastid+=1
#     print()
#     print(dict1)
    
# def main():
#     skyward_database = {100: ['Alice', 'Manager', 'HR'], 101: ['Arnold', 'Team Lead', 'IT'], 102: ['Chris', 'Developer', 'IT']}
#     formulaic_database = {101: ['Lucas', 'Developer', 'IT'], 102:['Anna', 'Intern', 'Marketing'], 103: ['Muhammad', 'Research Analyst', 'Marketing']}
#     merged_database = merge_databases(skyward_database, formulaic_database)
    
# main()
        


        