#/usr/local/bin/python3
import sys
import S11Q01 as base

def create_new_file(src_file):
    dest_file = src_file[:-4] + "-new" + src_file[-4:]
    print("Creating new file", dest_file)
    try:
        return open(dest_file,"w+")
    except IOError:
        print("Exception")


def write_to_file(FH, file_content):
    FH.writelines(file_content)
    
    
def create_newfile_content(FH):
    count = 1
    temp = []
    while True:
        line = FH.readline()
        if line == "":
            break
        if (count % 2) == 0:
            temp.append((line * 2))
        else:
            temp.append(line)
        count += 1
    FH.seek(0,0)
    temp.append("\n" + FH.readline())
    print(str(temp))
    return temp




def main():
    if __name__ == "__main__":
        file_name = sys.argv[1]
        FH = base.get_file_for_reading(file_name)
        new_file_content = create_newfile_content(FH)
        base.close_file(FH)
        FH = create_new_file(file_name)
        write_to_file(FH, new_file_content)
        FH.seek(0,0)
        print(FH.read())
        base.close_file(FH)
main()
