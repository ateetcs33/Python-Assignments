#/usr/local/bin/python3


def get_user_input(input_msg):
    return input(input_msg)

def get_student_marks():
    students_details = list()
    #student = tuple()
    while True:
        student = tuple(get_user_input("Enter Studen Name & marks :").split())
        if len(student) == 0:
            break
        students_details.append(student)
        
    print("Student details entered by the user:", students_details)
    return students_details

def get_marks(students):
    return students[1]

def sort_students(students, desc = False):
    if desc == True:
        students.sort(key = get_marks, reverse = True)
        print("Numbers sorted in Desc order:")
    else:
        students.sort(key = get_marks)
        print("Numbers sorted in Asc order:")
    print_students(students)
    return students

def print_students(students):
    for stud in students:
        print(stud)
    
def main():
    if __name__ == "__main__":
        students = get_student_marks()
        sort_students(students, True)
        sort_students(students)
        
main()
