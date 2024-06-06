import sqlite3
from os.path import exists

table_name_dict = {
    'Users' : {
        'create' : 'CREATE TABLE Users (login TEXT, password TEXT)',
        'insert' : '(?,?)',
        'get' : 'SELECT password FROM Users WHERE login = ? COLLATE NOCASE',
        'db_check' : 'login'
    },
    'Storage' : {
        'create' : 'CREATE TABLE Storage (user_name TEXT, stor_name TEXT, login TEXT, password TEXT)',
        'insert' : '(?,?,?,?)',
        'get' : 'SELECT * FROM Storage WHERE user_name = ?',
        'db_check' : 'stor_name'
    }
}

def push_to_db(db, data): # data --> List of tuples
    table_name = db[:-3]

    if table_name not in table_name_dict:
        raise ValueError(f"Unknown table name derived from db: {table_name}")
    
    if not exists(db):
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute(f"{table_name_dict[table_name]['create']}") 
        conn.commit()
        conn.close()
    
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    #if len(data) > 1:
    #    cursor.executemany(f"INSERT INTO {table_name} VALUES {table_name_dict[table_name]['insert']}", data)
    #else:
    cursor.execute(f"INSERT INTO {table_name} VALUES {table_name_dict[table_name]['insert']}", data[0])
    conn.commit()
    conn.close()
    
def edit_db(db, stor_name, login, upd_data):
    table_name = db[:-3]
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {table_name} SET password = ? WHERE stor_name = ? AND login = ?", (upd_data, stor_name, login))
    conn.commit()
    conn.close()

def get_from_db(db, data):
    table_name = db[:-3]
    query = f"{table_name_dict[table_name]['get']}"
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(query, (data, ))
    items = cursor.fetchall()
    conn.commit()
    conn.close()
    return items

def get_rowid_list(db,name):
    table_name = db[:-3]
    user_name = str(name)
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute (f" SELECT rowid FROM {table_name} WHERE user_name LIKE ? COLLATE NOCASE", (user_name, ))
    items = cursor.fetchall()
    conn.commit()
    conn.close()
    return items
#=================================================================================================================
def show_storage(db):
    table_name = db[:-3]
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute (f" SELECT * FROM {table_name}")
    items = cursor.fetchall()
    conn.commit()
    conn.close()
    return items
#=================================================================================================================   
def del_from_db(db, id_num):
    table_name = db[:-3]
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name} WHERE rowid = ?", (id_num, ))
    conn.commit()
    conn.close()
    
def show_storage_db(db, name):
    table_name = db[:-3]
    user_name = str(name)
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute (f" SELECT rowid, stor_name, login, password FROM {table_name} WHERE user_name LIKE ? COLLATE NOCASE", (user_name, ))
    items = cursor.fetchall()
    conn.commit()
    conn.close()
    return items

def prnt_db(data):
    table = data
    str_lng = 0
    titles = ['Uniq ID numm', 'Storage_Name', 'Login', 'Password']
    HEADER_COLOR = '\033[94m'  # Blue text
    RESET_COLOR = '\033[0m'    # Reset to default
    for item in table:
        for t_item in item:
            str_lng = len(str(t_item)) if len(str(t_item))>str_lng else str_lng
    
    print(*(HEADER_COLOR+str(title) + ' '*(str_lng-len(str(title)))+RESET_COLOR for title in titles), sep='\t')
    for item in table:
        print(*(str(t_item) + ' '*(str_lng-len(str(t_item))) for t_item in item), sep='\t')
        

    
def is_in_db(db,user_name):
    if not exists(db):
        return False
    else:
        table_name = db[:-3]
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute(f"Select name FROM sqlite_master Where type = 'table';")
        tables = cursor.fetchall()
        if len(tables) == 0:
            conn.close()
            return False
        else:
            cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {table_name_dict[table_name]['db_check']} = ? COLLATE NOCASE", (user_name, ))
            check = cursor.fetchone()
            conn.close()
            return check[0] > 0

