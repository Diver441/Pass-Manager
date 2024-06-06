import Pass_gen_man

Current_user = None     

def start_screen(): 
    print(f"{'-'*30}\nMain Menu")
    print("1 --> Login \n2 --> Register \n\n0 --> Exit")
    input_me([exit_me, log_in, register_user])

def input_me(command):
    global Current_user
    x = input('Command num1: __  ')
    while not x.isdigit() or int(x) not in range(len(command)):
            print("Incorrect input! Try again: ----  ", end="")
            x = input()
    x = int(x)
    chosen_command = command[x]()
    if isinstance(chosen_command, Pass_gen_man.User_papa) and chosen_command is not None:
        Current_user = chosen_command
    else:
        chosen_command
        
def del_my_storage():
    main_menu()

def exit_me():
    print("Programm exits now")
    Pass_gen_man.exit()
    
def log_in(): 
    print ("Your login options are: \n1 --> Admin \n2 --> User \n\n0 --> Back")
    input_me([start_screen, Pass_gen_man.Admin, Pass_gen_man.User])
    main_menu() if Current_user.login() else start_screen()
    
def register_user(): 
    print ("Your register options are: \n1 --> Admin \n2 --> User \n\n0 --> Back")
    input_me([start_screen, Pass_gen_man.Admin, Pass_gen_man.User])
    Current_user.register()
    start_screen()
    
def log_out(): 
    Current_user.logout()
    start_screen()
    
def main_menu(): 
    print("Main Menu: \n1 --> Add\Create a Password storage (1 item at a time) \n2 --> Goto my storage \n3 --> Delete my storage \n\n0 --> Log out and goto Startscreen")
    input_me([log_out, create_pass_item, stor_menu, del_my_storage])
    
def stor_menu():
    print(f"{'-*-'*43}\n {Current_user.user_name}, here are your storage options:\n1 --> Show my storage\n2 --> Edit item\n3 --> Delete Item\n\n0 --> Goto Main Menu")
    input_me([main_menu, show_item_list, edit_item, delete_item])

def show_item_list():
    Current_user.show_items()
    stor_menu()

def edit_item():
    Current_user.edit_item()
    print("Item changed")
    stor_menu()

def delete_item():
    check = Current_user.delete_item()
    if check:
        print("Item deleted")
        stor_menu()
    else:
        print("Operation cancelled!")
        stor_menu()
    
def create_pass_item(): 
    print("Please, enter a Name for Storage(website, creditcard, security-alarm, etc): ")
    Current_user.item_name = input(" ...")
    if perform_check():
        print("You are duplicating yor data - it is not allowed.\nRedirecting to beginning...")
        create_pass_item()
    print("Specify Login or other info: ")
    Current_user.item_log = input(" ...")
    print ("1 --> Generate Password \n2 --> Enter Password \n\n0 --> Go back to Main Menu")
    input_me([main_menu, generate_pass, enter_pass])
    print(f"Storage Name: {Current_user.item_name}  / Login: {Current_user.item_log}  / Password: {Current_user.item_pass}")
    print("Please, confirm your data: \n1 --> Yes \n2 --> No \n\n0 --> Cancel")
    input_me([main_menu, save_item, create_pass_item])

def perform_check():
    return Current_user.check_me()

def generate_pass(): 
    Check = False
    input_l = input('Please, enter the desirable length from 6 to 32 characters: ')
    while not Check:
        if input_l.isdigit():
            if int(input_l) in range(6,32):
                Check = True
            else:
                print('You must follow conditions, please, enter correct length:')
                input_l = input()
    length = int(input_l)
    Current_user.item_pass = Current_user.generate_pass(length)
    print(f"\nPassword: {Current_user.item_pass}")
    print("\nPlease confirm: \n1 --> Confirm \n2 --> Generate another \n\n0 --> Cancel\Main menu")
    input_me([main_menu, save_pass, generate_pass])

def save_pass():
    pass

def enter_pass():
    global pass_wrd
    print("Please Enter your Password: ", end="")
    Current_user.item_pass = input()
    
def save_item():
    Current_user.create_item()
    main_menu()
    
#admin
def ban_user():
    pass
def unban_user():
    pass

def main():
    print("Greeting msg!")
    start_screen()

if __name__ == "__main__":
    main()
