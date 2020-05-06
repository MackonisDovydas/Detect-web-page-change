import sys


def main():
    f = open("html.txt", "r")
    html = f.read().replace('\n', '')
    f.close()

    if html.find("Šiuo metu registracija nevyksta") >= 0:
        sys.exit(0)
    else:
        print("Words not found")
        sys.exit(1)


if __name__ == '__main__':
    main()
