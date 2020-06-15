#/usr/local/bin/python3
import S07Q01 as base

def string_operations():
    sentence = base.get_user_input("Enter the long Sentence :")
    print("The last Character in the sentence is :", sentence[-1:])
    print("The last 5 Characters in the sentence is :", sentence[-5:])
    print("The Characters present in 2nd & 5th position of the sentence are :",
          sentence[1], ",", sentence[4])
    print("Character at the center of the sentence, along with its 2 adjoining characters:",
          sentence[((sentence.__len__()//2)-1):((sentence.__len__()//2)+2)])
    
def main():
    if __name__ == "__main__":
        string_operations()

main()
