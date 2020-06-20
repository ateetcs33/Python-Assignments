#/usr/local/bin/python3
import sys
import S10Q01 as base

def open_file_for_writing(file_name):
    try:
        return open(file_name,"w+")
    except IOError:
        print(file_name, "File not found")

def print_file_content(file_name):
    FH = base.get_file_for_reading(file_name)
    lines = FH.readlines()
    for line in lines:
        print(line)
    
def copy_to_new_file(src_file, dest_file):
    SRC_FH = base.get_file_for_reading(src_file)
    DEST_FH = open_file_for_writing(dest_file)
    while True:
        line = SRC_FH.readline()
        if line == "":
            break
        line = line.replace("\n", "")
        sentences = line.replace(". ", ".\n")
        DEST_FH.writelines(sentences)
    DEST_FH.close()
    print("Copied contents of ", src_file, "to", dest_file)
 


    
def main():
    if __name__ == "__main__":
        src_file = sys.argv[1]
        dest_file = sys.argv[2]
        #src_file = "sample.txt"
        #dest_file = "abc.txt"
        copy_to_new_file(src_file, dest_file)
        print_file_content(dest_file)
main()
