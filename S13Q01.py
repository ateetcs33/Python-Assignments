#/usr/local/bin/python3


def get_user_input(input_msg):
    return input(input_msg)

def get_nums_from_user():
    nums = list()
    while True:
        num = int(get_user_input("Enter 3 digit number :"))
        if num == 0:
            break
        nums.append(num)
        
    print("Numbers entered by the user:", str(nums))
    return nums

def discard_non_3digit_nums(nums):
    new_nums = list()
    for num in nums:
        if num > 99 and num < 1000:
           new_nums.append(num)
    print("Extracted Three digit numbers from user input are :", new_nums) 
    return new_nums

def get_prime_nums(nums):
    prime_nums = list()
    for num in nums:
        if num % 2 == 0:
            prime_nums.append(num)
    print("Extracted Prime numbers :", prime_nums)
    return prime_nums

def sort_numbers(nums, desc = False):
    if desc == True:
        nums.sort(reverse = True)
        print("Numbers sorted in Desc order:", nums)
    else:
        nums.sort()
        print("Numbers sorted in Asc order:", nums)
    return nums


def main():
    if __name__ == "__main__":
        nums = get_nums_from_user()
        nums_3digit = discard_non_3digit_nums(nums)
        prime_nums = get_prime_nums(nums_3digit)
        sort_numbers(prime_nums, True)
        sort_numbers(prime_nums)
main()
