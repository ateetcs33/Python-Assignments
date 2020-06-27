#/usr/local/bin/python3
import random as rand 
def get_user_input(input_msg):
    return input(input_msg)

def get_nums_from_user():
    nums = list()
    for n in range(0, 10):
        nums.append(int(get_user_input("Enter number:")))
    print("Numbers are:", nums)
    return nums

def get_5_random_nums(nums):
    return rand.sample(nums, 5)

    
def main():
    if __name__ == "__main__":
        nums = get_nums_from_user()
        print(get_5_random_nums(nums))
main()
