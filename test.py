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


def delete_db(conn,table,column,what_to_remove):
    sql=f'''DELETE FROM {table} WHERE {column} = ?''',(what_to_remove,)
    conn.execute(sql)
    conn.commit()  
    
    
connection = create_connection('list.db')
create_table(connection,"Students",["first TEXT", "last TEXT","grade1 INTEGER","grade2 INTEGER","grade3 INTEGER","grade4 INTEGER"])   


def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return
        
        
first_names = select__db_array(connection,"Students","first")
last_names = select__db_array(connection,"Students","last")        
sortf =bubbleSort(first_names)
sortl = bubbleSort(last_names)

def binary_search(arr, low, high, x, output):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
            
            
def find(blank, list):
    time.sleep(1)
    os.system('cls')
    running = True
    name = []
    while running:
        temp_letter = ""
        spots = []
            if result == -1:
        print(f"Press [Enter] to submit name\nSudents {blank} name: [{''.join(name)}]\n\nOr Select a name below with the number ascosiated with it")
        for i in spots
            print(f"\n>i:{spots[i]}")
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
            print("Done")
            return ''.join(name).lower().capitalize()
        else:
            name.append(temp_letter.decode('ASCII'))
            
                
first = find("First")
last = find("Last")
os.system('cls')
print(f"First name: {first}\nLast name: {last}")