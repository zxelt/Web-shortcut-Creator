import os

def urlshort():
    url = input("Please enter Url: ")
    url_template = f"""[InternetShortcut]
URL={url}"""
    file = open("shortcut.url", "a")
    file.write(url_template)
    file.close()
    print("File create with succes !")
    input("Press enter to restart...")
    system.os('cls')
    main()

    


def main():
    print("""What shortcut do you want to create ? 
[1] Url shortcut
    """)
    choise = input(">> ")
    if choise == "1":
        urlshort()
    elif choise == "2":
        appshortcut()


if __name__ == '__main__':
    main()