#/usr/local/bin/python3
import S13Q01 as base

def get_file_for_reading(file_path):
    try:
        return open(file_path)
    except IOError:
        print(file_path, "File not found stoping the execution")
        sys.exit()
        
def get_numList_from_file(FH):
    lines = FH.read().split("\n")
    num_list = []
    for line in lines:
        if line.isdigit():
            num_list.append(int(line))
    print("Numbers fetched from file:", num_list)
    return num_list


def main():
    if __name__ == "__main__":
        FH = get_file_for_reading("numbers.txt")
        nums = get_numList_from_file(FH)
        FH.close()
        nums_3digit = base.discard_non_3digit_nums(nums)
        prime_nums = base.get_prime_nums(nums_3digit)
        base.sort_numbers(prime_nums, True)
        base.sort_numbers(prime_nums)
main()
