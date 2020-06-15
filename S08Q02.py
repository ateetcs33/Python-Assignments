#/usr/local/bin/python3
import S08Q01 as base
import math

def process_numbers():
    num = base.get_user_input("Enter the number :")
    #num_len = num.__len__()
    num_len = len(num)
    num = int(num)
    temp = 0
    if num_len == 1:
        temp = num + 7
        print("Numer after adding 7 is,", temp, "its unit place is", (temp % 10))
    elif num_len == 2:
        temp = int(math.pow(num, 5))
        print(str(num) + "^5 is,", temp, "its last 2 digits are", (temp % 100))
    elif num_len == 3:
        num2 = int(base.get_user_input("Enter another number :"))
        temp = num + num2
        print("Sum of 2 numbers is :", temp, "its last 3 digits are", (temp % 1000))
    else:
        print("Logic for length >", num_len, "is not implemented")

def main():
    if __name__ == "__main__":
        process_numbers()
main()
