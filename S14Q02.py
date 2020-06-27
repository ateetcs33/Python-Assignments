#/usr/local/bin/python3

import S14Q01 as base

def get_file_for_reading(file_path):
    try:
        return open(file_path)
    except IOError:
        print(file_path, "File not found stoping the execution")
        sys.exit()
        
def get_students_from_file(FH):
    lines = FH.read().split("\n")
    students = list()
    for line in lines:
        if len(line) != 0:
            students.append(tuple(line.split()))
    print("Students fetched from file:", students)
    return students

def main():
    if __name__ == "__main__":
        FH = get_file_for_reading("students.txt")
        students = get_students_from_file(FH)
        FH.close()
        base.sort_students(students, True)
        print()
        base.sort_students(students)
        
main()


