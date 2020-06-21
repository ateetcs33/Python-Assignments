#/usr/local/bin/python3
import sys
from S09Q02 import string_search_and_replace as replace_string
import S08Q01 as base


def file_reader(file_name):
    try:
        return open(file_name)
    except IOError:
        print("Exception occured")

def read_file(FH):
    content = FH.read()
    print("File content:\n" + content)
    return content

def main():
    if __name__ == "__main__":
        file_name = sys.argv[1]        
        main_str = read_file(file_reader(file_name))
        search_str = base.get_user_input("Enter the String to be searched :")
        replace_str = base.get_user_input("Enter the new String to replace :") 
        replace_string(main_str, search_str, replace_str)

main()
