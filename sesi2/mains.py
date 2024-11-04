
from libs import welcome_message, exit_program
from games import cece
from tools import warkop

def options():
    user_options = int(input(f'silahkan pilih programnya: \n1. Games CECE\n2. Games Warkop'))

def menu():
    welcome_message()
    user_options = options()
    if user_options == 1:
        cece.start()
    elif user_options == 2:
        warkop.start()
    else:
        print('hanya boleh pilih yang tersedia dimenu')
    
def main():
    welcome_message()
    menu()
    exit_program()

if __name__ == '__main__':
    main()