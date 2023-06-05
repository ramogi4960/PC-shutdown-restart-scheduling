import os


def shutdown():
    print("Enter 1 to shutdown computer immediately")
    print("Enter 2 to restart computer immediately")
    print("Enter 3 to shutdown computer after specified number of seconds")
    print("Enter 4 to restart computer after specified number of seconds")
    option = int(input("Enter option: "))
    if option == 1:
        os.system("shutdown /s /t 0")
    elif option == 2:
        os.system("shutdown /r /t 0")
    elif option == 3:
        t = input("Enter number of seconds after which to shutdown computer: ")
        os.system("shutdown /s /t " + t)
    elif option == 4:
        u = input("Enter number of seconds after which to restart computer: ")
        os.system("shutdown /r /t " + u)
    else:
        print("Wrong Option!!")


shutdown()
