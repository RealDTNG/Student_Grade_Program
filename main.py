# Dawson Hoyle
# Feb 21 2021
# Student grade program

import os
import time

Student_list = [["Dylan", "Baker", 98, 90, 92, 93], ["Dave", "Johnson", 67, 86, 74, 93],
                ["Jacob", "Kakowski", 73, 59, 64, 83], ["Josh", "Hotter", 51, 57, 53, 99],
                ["Erik", "Lagsaway", 100, 100, 100, 100]]


def grade_che(resu):
    l = range(0, 101)
    for i in resu:
        if int(i) not in l:
            return True
    return False


def grades():
    os.system('cls')
    global results
    things = True
    while things:
        try:
            new_grades = input(f"Please enter four grades  ex..[89,92,70,68]\n:")
            results = new_grades.split(",")
            print(results)
            if len(results) == 4:
                if grade_che(results):
                    raise Exception
                else:
                    things = False
                    return results
            else:
                raise Exception
        except:
            os.system('cls')
            print("ERROR Please enter a valid four grades (0-100)")


def add():
    time.sleep(1)
    os.system('cls')
    running = True
    while running:
        print("[First name,Last name]")
        new_name = input(f"\nPlease enter a new name\n:")
        time.sleep(.5)
        if new_name.isalpha():
            os.system('cls')
            print("Please enter name properly")
        else:
            new_name = new_name.split(",")
            grades()
            Student_list.append(
                [f"{new_name[0].lower().capitalize()}", f"{new_name[1].lower().capitalize()}", int(results[0]), int(results[1]), int(results[2]),
                    int(results[3])])
            os.system('cls')
            print("Successfully Added A Student\n")
            running = False
            time.sleep(2)
            os.system('cls')
            


def student_list():
    time.sleep(1)
    os.system('cls') 
    m_leng = 0
    for firstn, lastn, gr1, gr2, gr3, gr4 in Student_list:
        if len(firstn + lastn) > m_leng:
            m_leng = len(firstn + lastn)
    for firstn, lastn, gr1, gr2, gr3, gr4 in Student_list:
        print(f"{lastn}, {firstn}:{' ' * (m_leng + 5 - len(firstn + lastn))}{gr1}% {gr2}% {gr3}% {gr4}%")
    time.sleep(1)
    input("To Return To Menu Press [Enter]")
    time.sleep(1)
    os.system('cls')


def search(arr, x, y):
    global spot
    for i in range(len(arr)):
        if arr[i][0] == x and arr[i][1] == y:
            spot = i
            return  spot
    else:
        return -1 


def student_av():
    time.sleep(1)
    runing = True
    while runing:
        os.system('cls')
        in_name = input(f"Please enter the first name of the student that you would grades for.\n:").lower().capitalize()
        time.sleep(.5)
        os.system('cls')
        in_name2 = input(f"Please enter the last name of the student that you would grades for.\n{in_name},:").lower().capitalize()
        spot=search(Student_list,in_name, in_name2)
        if spot != -1:
            os.system('cls')
            print(f"{Student_list[spot][1]}, {Student_list[spot][0]}\n\nGrade #1: {Student_list[spot][2]}\nGrade #2: {Student_list[spot][3]}\nGrade #3: {Student_list[spot][4]}\nGrade #4: {Student_list[spot][5]}")
            total = (Student_list[spot][2] + Student_list[spot][3] + Student_list[spot][4] + Student_list[spot][5])/4
            print(f"\n{Student_list[spot][0]}'s Course average is {total}\n")
            time.sleep(1.5)
            input("press [ENTER] to return to menu")
            time.sleep(1.5)
            os.system('cls')
            runing = False
        else:
            print("ERROR, Student not found")
            time.sleep(1)
            print("Please try again")
            time.sleep(1.5)
        
        
def Course_av():
    time.sleep(1)
    os.system('cls')
    print("course average")
     

def exit_G():
    os.system('cls')
    print("See you next time")
    time.sleep(1)
    exit()


menus = {"1": add, "2": student_list, "3": student_av, "4": Course_av, "5": exit_G}
while True:
    print(" '1' | To Add Students")
    print(" '2' | To View The List")
    print(" '3' | To View The Student Averages")
    print(" '4' | To View The Course Average")
    print(" '5' | To Exit")
    choice = input(f"Please pick a menu option\n\n:")
    if choice in menus:
        menus[choice]()
    else:
        os.system('cls')
        print("ERROR, Please enter a valid choice")
        time.sleep(1)
