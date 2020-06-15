#/usr/local/bin/python3
def get_user_input(input_Msg):
    return input(input_Msg)

def get_full_name():
    name = get_user_input("Enter your name :")
    surname = get_user_input("Enter your surname :")
    return [name,surname]
    
def manipulate_strings():
    full_name = get_full_name()
    name = full_name[0]
    surname = full_name[1]
    print("Name :",name,", Surname :", surname)
    print(name.upper(), surname.upper())
    print(surname.capitalize(), name.capitalize())

def main():
    if __name__ == "__main__":
        manipulate_strings()
main()
