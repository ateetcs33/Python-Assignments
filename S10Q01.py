#/usr/local/bin/python3
import sys
def get_user_input(input_Msg):
    return input(input_Msg)

def get_file_for_reading(file_path):
    try:
        return open(file_path)
    except IOError:
        print(file_path, "File not found stoping the execution")
        sys.exit()

def check_sentences_starts_with_capital_letter(FH):
    sentences_starting_with_capital_letter = []
    sentences_starting_with_small_letter = []
    while True:
        line = FH.readline()
        if line == "":
            break;
        sentences = line.split(". ")
        for sent in sentences:
            if sent[0].isupper():
                #print("This Sentence Starts with capital letter:\n" + sent)
                sentences_starting_with_capital_letter.append(sent)
            else:
                sentences_starting_with_small_letter.append(sent)
                #print("This Sentence doesn't start with Capital lettere:\n", sent)
    print("Sentences which start with Capital letter are:\n" + str(sentences_starting_with_capital_letter))
    print("Sentences which doesn't start with Capital letter are:\n" + str(sentences_starting_with_small_letter))

def main():
    if __name__ == "__main__":
        file_name = get_user_input("Enter file name:")
        FH = get_file_for_reading(file_name)
        check_sentences_starts_with_capital_letter(FH)

main()
        
