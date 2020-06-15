#/usr/local/bin/python3
import S07Q01 as base

def find_initials():
    full_name = base.get_full_name()
    print(full_name)
    name = full_name[0]
    surname = full_name[1]
    position = -1
    possible_initials = ""
    for pos in range(1, surname.__len__()):
        possible_initials = name[:position] + " " + surname[:position]
        print(possible_initials)
        position += -1
    print("Best possible initials of \"" + name, surname +"\" is :", possible_initials)


def main():
    if __name__ == "__main__":
        find_initials()

main()
