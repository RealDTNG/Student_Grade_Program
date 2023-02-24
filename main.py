# Dawson Hoyle
# Feb 21 2021
# Student grade program

import time, os
Student_list = [["Dylan","Baker", 98, 90, 92, 93],["Dave","Johnson",67,86,74,93],["Jacob","Kakowski",73,59,64,83],["JOsh","Hotter",51,57,53,99],["Erik","Lagsaway",100,100,100,100]]
    
    
def add():
    while True:
        print("[first name, last name]")
        new_name = input("Please enter a new name")
        if new_name.isalpha():
            print("Please add a comma between first and last name")
        else:
            for i, j in enumerate(new_name):
                if "," in j:
                    Student_list.append([new_name[:i], new_name[i:]])
                    print("Sucssesfully Added A Student")
                    break
                    list()
            else:
                print("Please add a comma between first and last name")
                break
            break
    
def list():
    m_leng = 0
    for firstn, lastn, gr1, gr2, gr3, gr4 in Student_list:
        if len(firstn + lastn)> m_leng:
            m_leng = len(firstn + lastn)
    for firstn, lastn, gr1, gr2, gr3, gr4 in Student_list:
        print(f"{lastn}, {firstn}:{' '*(m_leng + 5 - len(firstn + lastn))}{gr1:03}% {gr2:03}% {gr3:03}% {gr4:03}%")
    time.sleep(1)
    input("To Return To Menu Press [Enter]")
    
def Student_av():
    print("student averages")
    
def Course_av():
    print("course average")
    
def exit_G():
    print("See you next time")
    exit()
    

menus = {"1":add, "2":list, "3":Student_av, "4": Course_av, "5":exit_G}
while True:
    os.system('cls')
    print(" '1' | To Add Students")
    print(" '2' | To View The List")
    print(" '3' | To View The Student Averages")
    print(" '4' | To View The Course Average")
    print(" '5' | To Exit")
    choice = input(f"Please pick a menu option\n\n:")
    if choice in menus:
        os.system('cls')
        menus[choice]()
    else:
        os.system('cls')
        print("ERROR, Please enter a valid choice")
        time.sleep(1)
