#/usr/local/bin/python3
import S08Q01 as base
import math

def generate_number():
    num = int(base.get_user_input("Enter the number :"))
    generated_num = ""
    for n in range(0, num):
        generated_num = generated_num + str(n) * (num-1)
    print(generated_num)
       
def main():
    if __name__ == "__main__":
        generate_number()
main()
