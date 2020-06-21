#/usr/local/bin/python3
import S09Q01 as web_template_creater

def open_file_for_writing(file_name):
    try:
        return open(file_name, "w+")
    except IOError:
        print("Exception occured")

def write_to_file(FH, content):
    FH.write(content)

def main():
    if __name__ == "__main__":
        file_name = web_template_creater.base.get_user_input("Enter file name:")
        FH = open_file_for_writing(file_name)
        main_header = web_template_creater.get_main_header()
        sub_header = web_template_creater.get_sub_header()
        paragrapgs = web_template_creater.get_paragraphs()
        content = web_template_creater.construct_web_page(main_header, sub_header, paragrapgs)
        print("*" * 15, "Writing constructed Web page to file" ,"*" * 15)
        print(content)
        write_to_file(FH, content)
        FH.close()
main()
