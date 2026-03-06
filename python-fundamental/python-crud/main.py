from libs import welcome_message,exit_program
from game import cuypy
from tools import warung
def menu():
    while True:
        user_option = int(input(f'Menu Program:\n1.CUYPY Game\n2.Warung Mini\n3.Keluar program\n\nsilahkan pilih: '))

        if user_option == 1:
            cuypy.start()
        elif user_option == 2:
            warung.start()
        elif user_option == 3:
            exit_program()
        else:
            print("silahkan pilih yang tersedia di menu!")

def main():
    welcome_message()
    menu()

if __name__ == '__main__':
    main()
