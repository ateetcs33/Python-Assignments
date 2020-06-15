#/usr/local/bin/python3
import S08Q01 as base

def string_search_and_replace():
    main_str = base.get_user_input("Enter the main String :")
    search_str = base.get_user_input("Enter the String to be searched :")
    replace_str = base.get_user_input("Enter the new String to replace :")      
    if main_str.find(search_str) != -1:
        main_str = main_str.replace(search_str, replace_str)
        print("String after replacing \"" + search_str + "\" with \"" + replace_str +"\" is :\n", main_str)
    else:
        print("\"" + search_str + "\" is not present in main string :", main_str)

    
def main():
    if __name__ == "__main__":
        string_search_and_replace()
main()
