# Dawson Hoyle
# Feb 21 2021
# Student grade program

import time, os
Student_list = [[]]
    
    
def add():
    print("adding students")
    
def list():
    print("viewing list")
    
def Student_av():
    print("student averages")
    
def Course_av():
    print("course average")
    
def exit_G():
    print("See you next time")
    exit()
    

menus = {"1":add, "2":list, "3":Student_av, "4": Course_av, "5":exit_G}
while True:
    print("1 | To Add Or Remove Students")
    print("2 | To View The List")
    print("3 | To View The Student Averages")
    print("4 | To View The Course Average")
    print("5 | To Exit")
    choice = input(f"Please pick a menu option\n\n:")
    if choice in menus:
        os.system('cls')
        menus[choice]()
        break
    else:
        os.system('cls')
        print("ERROR, Please enter a valid choice")
        time.sleep(1)
