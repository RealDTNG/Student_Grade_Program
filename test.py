import os, time, msvcrt, sqlite3

def create_connection(db_file):
    #create a database connection to the SQLite database
    #return: Connection object or None
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn


def insert_db(conn,table, columns,data):
    col = ",".join(columns)
    fill = tuple(data)
    unknow=["?"]*len(columns)
    x=",".join(unknow)
    sql = f''' INSERT INTO {table} ({col}) VALUES({x})'''
    conn.execute(sql,fill)
    conn.commit()


def create_table(conn,table, columns):
    col = ",".join(columns)
    sql = f'''CREATE TABLE IF NOT EXISTS {table}( id INTEGER PRIMARY KEY, {col});'''
    conn.execute(sql)


def select_db(conn,table,columns_and_data=None):
    if not columns_and_data==None:
        col = " AND ".join(columns_and_data)
        sql=f'''SELECT * FROM {table} WHERE {col}'''
        #where 4 is the id i am looking for
        return conn.execute(sql)
    else:
        sql =f"SELECT * from {table}"
        return conn.execute(sql)
    
    
def select__db_f_l(conn,table,first_name,last_name):
    sql=f"SELECT * FROM {table} WHERE first=? AND last=?"
    return conn.execute(sql,(first_name,last_name)) 


def select__db_array(conn,table,name):
    sql=f"SELECT {name} FROM {table}"
    return conn.execute(sql) 

def tuple_list(list): 
    new_list = []
    for element in list:
        new_list.append(element[0])
    return new_list

def delete_db(conn,table,column,what_to_remove):
    sql=f'''DELETE FROM {table} WHERE {column} = ?''',(what_to_remove,)
    conn.execute(sql)
    conn.commit()  
    
    
connection = create_connection('list.db')
create_table(connection,"Students",["first TEXT", "last TEXT","grade1 INTEGER","grade2 INTEGER","grade3 INTEGER","grade4 INTEGER"])   


def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return
          
    
first_names = tuple_list(list(select__db_array(connection,"Students","first").fetchall()))
last_names = tuple_list(list(select__db_array(connection,"Students","last").fetchall()))
sortf = first_names.copy()
sortl = last_names.copy()
bubbleSort(sortf)
bubbleSort(sortl)


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x or arr[mid].startswith(x):
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
            
            
def find(blank, list):
    time.sleep(1)
    os.system('cls')
    running = True
    name = []
    while running:
        temp_name = ''.join(name)
        temp_letter = ""
        spots = []
        print(f"Press [Enter] to submit name\nSudents {blank} name: [{temp_name}]\n\nOr Select a name below with the number ascosiated with it")
        name_spots = {}
        times = -1
        for s in list:
            times += 1
            if (s.startswith(temp_name)):
                spots.append(times)
        for i in spots:
            try:
                if len(temp_name) != 0:
                    print(f"\n>{i}:{list[spots[i]]}")
                    name_spots[i]=spots[i]
            except:
                pass
        temp_letter = msvcrt.getche()
        os.system('cls')
        if temp_letter == (b'\x08'):
            try:
                name.pop()  
            except:
                os.system('cls')
                print(f"ERROR\nThere Are No More Characters")
                time.sleep(1)
                os.system('cls')
        elif temp_letter == (b'\r'):
            running = False
            print("Serching.")
            time.sleep(.25) 
            os.system('cls')
            print("Serching..")
            time.sleep(.25)
            os.system('cls')
            print("Serching...")
            time.sleep(.25)
            os.system('cls')
            result = binary_search(list, 0, len(list)-1,''.join(temp_name))
            if result == -1:
                print("That name is not in the database!")
                input("Press [Enter] to return to start")
            else:
                print("That student is in the database!")
                input("Press [Enter] to return to start")
            return temp_name.lower().capitalize()
        elif temp_letter.decode('ASCII') in name_spots:
            running = False
            temp_name = f"{list[spots[temp_letter.decode('ASCII')]]}"
        else:
            name.append(temp_letter.decode('ASCII'))
            
while True:
    os.system('cls')
    input("Press [Enter] to search for a student")
    first = find("First",sortf)