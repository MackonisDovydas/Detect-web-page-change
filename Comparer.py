import sys


def main():
    f = open("Template.txt", "r")
    template = f.read()
    f.close()
    f = open("html.txt", "r")
    html = f.read()
    f.close()
    if template == html:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
