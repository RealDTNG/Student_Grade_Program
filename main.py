# Dawson Hoyle
# Feb 21 2021
# Student grade program
#one new sort and binary search

import os, time, sqlite3, search_and_sort   # imports


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


def grade_che(resu):            # check if grades are between 0-100
    l = range(0, 101)
    for i in resu:
        if int(i) not in l:
            return True
    return False

def grades():           # user adds 4 valid grades
    os.system('cls')
    global results
    things = True
    while things:           # loop
        try:
            new_grades = input(f"Please enter four grades  ex..[89,92,70,68]\n:")               # user input
            results = new_grades.split(",")
            if len(results) == 4:           # check for 4 grades
                if grade_che(results):           #check if grades are valid
                    raise Exception
                else:
                    things = False          #end loop
                    return results          # return results to add()
            else:
                raise Exception
        except:
            os.system('cls')
            print("ERROR Please enter a valid four grades (0-100)")


def add():          # function to add students
    time.sleep(.5)
    os.system('cls')
    running = True
    while running:          #loop
        print("[First name,Last name]")
        new_name = input(f"\nPlease enter a new name\n:").replace(" ", "")
        time.sleep(.5)
        new_name = new_name.split(",")          #make new_name into a list of first name and last name
        if len(new_name) != 2:          #check if it has a first name and last name
            os.system('cls')
            print("Please enter name properly")
            pass
        else:
            grades()            # add students grades if name is valid
            insert_db(connection,"Students",["first","last","grade1","grade2","grade3","grade4"],[f"{new_name[0].lower().capitalize()}", f"{new_name[1].lower().capitalize()}", int(results[0]), int(results[1]), int(results[2]), int(results[3])])
            os.system('cls')
            print("Successfully Added A Student\n")
            running = False             # end loop to return to menu
            time.sleep(2)
            os.system('cls')
            


def student_list():              #view student list
    time.sleep(.5)
    os.system('cls') 
    m_leng = 0
    Student_list =select_db(connection,"Students").fetchall()
    for id, firstn, lastn, gr1, gr2, gr3, gr4 in Student_list:          #things in student list
        if len(firstn + lastn) > m_leng:
            m_leng = len(firstn + lastn)
    for id, firstn, lastn, gr1, gr2, gr3, gr4 in Student_list:
        print(f"{lastn}, {firstn}:{' ' * (m_leng + 5 - len(firstn + lastn))}{gr1}% {gr2}% {gr3}% {gr4}%")       #print each thing in list
    time.sleep(1)
    input("To Return To Menu Press [Enter]")
    time.sleep(.5)
    os.system('cls')


def search(x, y):          #search funtion
    cursor = select__db_f_l(connection,"Students",x,y)
    temp=cursor.fetchall()
    if not temp:
        return -1
    else:
        return temp


def student_av():           #check for student average
    time.sleep(.5)
    runing = True
    while runing:
        os.system('cls')
        in_name = input(f"Please enter the first name of the student that you would grades for. Or press [Enter] to return to the menu.\n:").lower().capitalize()
        time.sleep(.5)
        os.system('cls')
        if in_name == "":
            runing = False
            break
        in_name2 = input(f"Please enter the last name of the student that you would grades for.\n{in_name},:").lower().capitalize()  #format inputs
        try:
            spot = list(map(list, search(in_name, in_name2)))
        except:
             spot = search(in_name, in_name2)
        
        if spot != -1:
            os.system('cls')
            print(f"{spot[0][1]}, {spot[0][2]}\n\nGrade #1: {spot[0][3]}\nGrade #2: {spot[0][4]}\nGrade #3: {spot[0][5]}\nGrade #4: {spot[0][6]}")
            total = (spot[0][3] + spot[0][4] + spot[0][5] + spot[0][6])/4
            print(f"\n{spot[0][1]}'s Course average is {total}\n")
            time.sleep(1)
            input("press [ENTER] to return to menu")
            time.sleep(1)
            os.system('cls')
            runing = False
        else:
            print("ERROR, Student not found")
            time.sleep(1)
            print("Please try again")
            time.sleep(1)
        
        
def Course_av():            # course averages function
    grad1, grad2, grad3, grad4 = [],[],[],[]
    Student_list = list(map(list,select_db(connection,"Students").fetchall()))
    time.sleep(.5)
    os.system('cls')
    for students in range(len(Student_list)):
        grad1.append(Student_list[students][3])
        grad2.append(Student_list[students][4])     #adding grades to course lists
        grad3.append(Student_list[students][5])
        grad4.append(Student_list[students][6])
    print(f"Course Averages:\n\n Course 1 av:      {'{0:.1f}'.format(sum(grad1)/len(grad1))}\nGrades: {', '.join(str(e) for e in grad1)}")
    print(f"\n\n Course 2 av:      {'{0:.1f}'.format(sum(grad2)/len(grad2))}\nGrades: {', '.join(str(e) for e in grad2)}")
    print(f"\n\n Course 3 av:      {'{0:.1f}'.format(sum(grad3)/len(grad3))}\nGrades: {', '.join(str(e) for e in grad3)}")     #printing grades and average
    print(f"\n\n Course 4 av:      {'{0:.1f}'.format(sum(grad4)/len(grad4))}\nGrades: {', '.join(str(e) for e in grad4)}")
    input("Press [Enter] to return to menu")
    os.system('cls')
    
    
def search():
    time.sleep(0.5)
    os.system('cls')
    search_and_sort.find()
    time.sleep(0.5)
    os.system('cls')


def exit_G():       #exit program function
    os.system('cls')
    print("See you next time")      
    time.sleep(1)
    exit()
    

menus = {"1": add, "2": student_list, "3": student_av, "4": Course_av,"5":search, "6": exit_G}             #dictonary to call functions
while True:         # menu loop
    print(" '1' | To Add Students")
    print(" '2' | To View The List")
    print(" '3' | To View The Student Averages")        #option of functions
    print(" '4' | To View The Course Average")
    print(" '5' | To Serch For Students")
    print(" '6' | To Exit")
    choice = input(f"Please pick a menu option:\n")
    if choice in menus:
        menus[choice]()     #use imput to call functions via dictonarry
    else:
        os.system('cls')
        print("ERROR, Please enter a valid choice")     #check for valid choices
        time.sleep(1)
