#/usr/local/bin/python3
import sys
import S10Q01 as base

def find_line_with_max_occurance_ofletter(FH, letter):
    max_occurance = 0
    line_with_max_occurance = 0
    line_num = 0
    while True:
        line = FH.readline()
        if line == "":
            break;
        count = line.count(letter)
        line_num += 1
        if max_occurance < count:
            max_occurance = count
            line_with_max_occurance = line_num
        print("Line Num :", str(line_num), "Occurance of '" + letter + "':", str(count))
        
    print("Line number :", str(line_with_max_occurance), "has the max occurance of '" +
          letter + "' with count of :", str(max_occurance))


    
def main():
    if __name__ == "__main__":
        file_name = sys.argv[1]
        letter = sys.argv[2]
        #base.get_user_input("Enter file name:")
        FH = base.get_file_for_reading(file_name)
        find_line_with_max_occurance_ofletter(FH, letter)

main()
