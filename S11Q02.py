#/usr/local/bin/python3
import sys
import S11Q01 as base


def print_lines_with_word(FH, search_word):
    lines = FH.readlines()
    lines_with_searchword = []
    for line in lines:
        if line.find(search_word) > -1:
            lines_with_searchword.append(line)
    if lines_with_searchword.__len__() > 0:
        print("Lines which contain search word :", search_word)
        for line in lines_with_searchword:
            print(line.replace("\n",""))
    else:
        print("no lines contain the search word:", search_word)

    
def main():
    if __name__ == "__main__":
        file_name = sys.argv[1]
        search_word = sys.argv[2]
        FH = base.get_file_for_reading(file_name)
        print_lines_with_word(FH, search_word)
        base.close_file(FH)
main()
