#/usr/local/bin/python3
def get_user_input(input_Msg):
    return input(input_Msg)

def close_file(FH):
    FH.close()

    
def get_file_for_reading(file_path):
    try:
        return open(file_path)
    except IOError:
        print(file_path, "File not found stoping the execution")
        sys.exit()

def get_numList_from_file(FH):
    lines = FH.readlines()
    num_list = []
    for line in lines:
        if line.replace("\n","").isdigit():
            num_list.append(int(line))
    print("Numbers fetched from file:", num_list)
    return num_list
        

def find_max_num(num_list):
    max_num = 0
    for num in num_list:
        if max_num < num:
            max_num = num
    print("Biggest number in the list is:", max_num)
    return max_num

def find_sum_of_numlist(num_list):
    total = 0
    for num in num_list:
        total = total + num
    print("Sum of all the numbers in the list is:", total)
    return total
    
 
def main():
    if __name__ == "__main__":
        file_name = get_user_input("Enter file name:")
        FH = get_file_for_reading(file_name)
        num_list = get_numList_from_file(FH)
        find_max_num(num_list)
        find_sum_of_numlist(num_list)
        close_file(FH)
main()
        
