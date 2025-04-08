#QUESITON 1

students = [
("Alice Johnson", 101, [("Math", 95.0, 3), ("History", 87.5, 4), ("Physics", 92.0, 3)]),
("Bob Smith", 102, [("Math", 76.0, 3), ("History", 83.0, 4), ("Biology", 89.5, 4)]),
("Charlie Brown", 103, [("Math", 85.0, 3), ("History", 78.0, 4), ("Chemistry", 91.0, 3)]),
]


def calculate_gpa(student_data):
    totalGPA=0
    totalcredit=0
    GPA_LIST=[]
    for students in student_data:
        for elements in students[2]:
            totalGPA+=elements[1]*elements[2]
            totalcredit+=elements[2]
        GPA_LIST.append([students[0],totalGPA/totalcredit])
        totalGPA=0
        totalcredit=0
    return GPA_LIST


def main():
    datafunction=input("WHAT WOULD YOU LIKE TO KNOW(Student GPA(1), Student Ranking (2), Course Average(3)):")
    if datafunction=="1":
        print(calculate_gpa(students))
main()

