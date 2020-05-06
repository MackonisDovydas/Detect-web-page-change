
import sys

def main():
    Template_URL = "https://is.vu.lt/pls/klevas/am$pd_reg_app.show?p_stud_id=219671&p_kalba_name=lt"
    f = open("Template.txt", "r")
    template = f.read()
    f.close()
    f = open("html.txt", "r")
    html = f.read()
    f.close()
    f = open("URL.txt", "r")
    URL = f.read()
    f.close()
    f = open("html_down.txt", "r")
    URL_down = f.read()
    f.close()
    f = open("output1.txt", "w+")
    if template == html:
        sys.exit(0)
    elif template == URL_down:
        print("VU is Down")
        f.write("VU is Down")
        f.close()
        sys.exit(1)
    elif URL != Template_URL:
        print("Wrong URL")
        f.write("Wrong URL")
        f.close()
        sys.exit(1)	
    else:
        print("Template wrong")
        f.write("VU PD page change")
        f.close()
        sys.exit(1)

if __name__ == '__main__':
    main()
