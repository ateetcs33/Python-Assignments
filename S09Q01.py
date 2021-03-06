#/usr/local/bin/python3
import S08Q01 as base

def web_page_skeleton():
    web_template ='''
    <html>
        <head>
            <title>
                main heading
            </title>
        </head>
        <body>
            <h1>
                sub heading
            </h1>
            paragraphs           
        </body>
    </html>
    '''
    return web_template

def construct_paragrapghs(paragrapgs):
    para_template ="""
            <p>
                para
            </p>
            """
    actual_para = ""
    for para in paragrapgs:
        actual_para = actual_para + para_template.replace("para", para)
    return actual_para

def get_main_header():
    return base.get_user_input("Enter the main header :")

def get_sub_header():
    return base.get_user_input("Enter the sub header :")
    
def get_paragraphs():
    para_count = int(base.get_user_input("Enter Number of paragraphs :"))
    paragrapgs = []
    for para in range(1, (para_count + 1)):
        paragrapgs.append(base.get_user_input("Enter paragragh No"+ str(para) + ":"))
    return paragrapgs

def construct_web_page(main_header, sub_header, paragrapgs):
    #main_header = base.get_user_input("Enter the main header :")
    #sub_header = base.get_user_input("Enter the sub header :")
    #para_count = int(base.get_user_input("Enter Number of paragraphs :"))
    #paragrapgs = []
    #for para in range(1, (para_count + 1)):
    #    paragrapgs.append(base.get_user_input("Enter paragragh No"+ str(para) + ":"))        
    para_template = construct_paragrapghs(paragrapgs)
    web_template = web_page_skeleton()

    web_template = web_template.replace("main heading", main_header)
    web_template = web_template.replace("sub heading", sub_header)
    web_template = web_template.replace("paragraphs", para_template)
    return web_template

    
def main():
    if __name__ == "__main__":
        main_header = get_main_header()
        sub_header = get_sub_header()
        #para_count = int(base.get_user_input("Enter Number of paragraphs :"))
        paragrapgs = get_paragraphs()
        web_template = construct_web_page(main_header, sub_header, paragrapgs)
        print()
        print("*" * 15, "Printing constructed Web page" ,"*" * 15)
        print(web_template)
main()
