#/usr/local/bin/python3
def get_user_input(input_Msg):
    return input(input_Msg)

def find_num_digits():
    num = get_user_input("Enter the number :")
    print("The number entered has", (num.__len__()), "digits.")

def main():
    if __name__ == "__main__":
        find_num_digits()
main()
