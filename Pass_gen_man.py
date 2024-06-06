import Pass_gen_DB
from sys import exit
from os.path import exists
from secrets import choice
from string import ascii_letters, digits, punctuation

class User_papa:
    def __init__(self):
        self.pass_word = self.user_name = None
        self._item_name = self._item_log = self._item_pass = None
        self.user = [self.user_name, self.pass_word]
        self._item = [self._item_name, self._item_log, self._item_pass]

    def register(self):
        pass
    def login(self):
        pass
    def get_user_data(self):
        pass
    def push_user_data(self):
        pass
    def logout(self):
        pass
    def create_item(self):
        pass
    def delete_item(self):
        pass
    def generate_login(self):
        pass
    def generate_pass(self):
        pass
    def edit_data(self):
        pass

class User (User_papa):  # ______________________________________________________________ USER ________________________________________________________________
    def __init__(self):
        super().__init__()
        self.file_name = "Users.db"
    
    def register(self): 
        check = True
        print(f"{'-'*8}Welcome to Register screen{'-'*8}")
        while check:
            self.user_name = input("Enter Login: ")
            check = Pass_gen_DB.is_in_db(self.file_name, self.user_name)
            if check:
                print("This Name is taken, please, pick another one!")
        self.pass_word = input("Enter Password: ")
        self.user = [(self.user_name, self.pass_word),]
        self.push_user_data(self.user) 
        print(f"New User: {self.user[0]} is successfully registered \nNow You can login with your new Login and Password.")
        self.logout()
    
    def login(self):
        check = False
        Count = 3
        print(f"{'.'*8}Welcome to Login screen{'.'*8}")
        while not check:
            input_login = input ("Enter Login: ").capitalize()
            check = Pass_gen_DB.is_in_db(self.file_name, input_login)
            if not check:
                print("You are not registered, please, go to registration menu!")
                return False
            
        while Count > 0:
            temp = []
            input_pass =  input ("Enter Password: ")
            temp = Pass_gen_DB.get_from_db(self.file_name, input_login)
            if temp[0][0] != input_pass and Count > 0:
                 Count -=1
                 print(f"Incorrect password, {Count} tries left")
            else:
                self.user_name = input_login
                self.file_name = "Storage.db"
                print(f"Login successful! \n{'.'*39} ")
                return True
        print("You are out of tries!!")
        return False

    def push_user_data(self, data):                             
        Pass_gen_DB.push_to_db(self.file_name, data)
    
    def logout(self):                                           
        self.__init__()

    def check_me(self):
        return Pass_gen_DB.is_in_db(self.file_name, self.item_name)
    #-----------------------------------------Storage Item---------------------------------
    @property  # ---------------------Name---------
    def item_name(self):
        return self._item_name
    @item_name.setter
    def item_name(self, data):
        self._item_name = data

    @property # ----------------------Login---------
    def item_log(self):
        return self._item_log
    @item_log.setter
    def item_log(self, data):
        self._item_log = data

    @property #-----------------------Password-------
    def item_pass(self):
        return self._item_pass
    @item_pass.setter
    def item_pass(self, data):
        self._item_pass = data
    #---------------------------------------------------------------------------------------        
    def create_item(self):                                
        data = [(self.user_name, self.item_name, self.item_log, self.item_pass), ]
        Pass_gen_DB.push_to_db(self.file_name, data)
        print('Item added.')

    def generate_pass(self, length):
        password = ''.join(choice(ascii_letters+digits+punctuation) for _ in range(length))
        return password
    
    def show_items(self):
        Pass_gen_DB.prnt_db(Pass_gen_DB.show_storage_db(self.file_name, self.user_name))

    def edit_item(self):
        pass

    def delete_item(self):
        strg_list = []
        id_num = input("Please enter a Uniq ID numm for Storage item or '0' to cancel: ")
        get_lst = Pass_gen_DB.get_rowid_list(self.file_name, self.user_name)
        strg_list.extend(int(int_item) for item in get_lst for int_item in item)
        if id_num == '0':
            return False 
        while not id_num.isdigit() or int(id_num) not in strg_list:
            print("Incorrect input! Try again: ", end="")
            id_num = input()
            if id_num == '0':
                return False
        id_num = int(id_num)
        Pass_gen_DB.del_from_db(self.file_name, id_num)
        return True

class  Admin(User_papa): # ______________________________________________________________________ ADMIN ________________________________________________________
    def __init__(self):
        super().__init__()
        self.file_name = "Admins.db"

    def login(self):
        pass
    
    def register(self):
        pass
   
    def push_user_data(self, data):
        pass
    
    def logout(self):
        self.__init__()

class Super_user(User): # ___________________________________________________________ Super user _________________________________________________________________ when time comes
    def __init__(self):
        super().__init__()


def main():
    pass

if __name__ == "__main__":
    main()
