import os

def main():
    print("Hello Word")
    print("Empezando function")
    listfile()


def listfile():
    pwd:str = os.getcwd()
    print(pwd)
    print(__file__)

if __name__ == "__main__":
    main()  