
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

    if template == html:
        sys.exit(0)
    else:
        print("Template wrong")
        sys.exit(1)

if __name__ == '__main__':
    main()
