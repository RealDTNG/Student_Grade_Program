# Dawson Hoyle
# Feb 21 2021
# Student grade program

import os
import time

Student_list = [["Dylan", "Baker", 98, 90, 92, 93], ["Dave", "Johnson", 67, 86, 74, 93],
                ["Jacob", "Kakowski", 73, 59, 64, 83], ["JOsh", "Hotter", 51, 57, 53, 99],
                ["Erik", "Lagsaway", 100, 100, 100, 100]]


def grade_che(resu):
    l = range(0,101)
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
           # os.system('cls')
            print("ERROR Please enter a valid four grades (0-100)")


def add():
    os.system('cls')
    runing = True
    while runing:
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
                [new_name[1], f" {new_name[0]}", int(results[0]), int(results[1]), int(results[2]),
                    int(results[3])])
            os.system('cls')
            print("Successfully Added A Student\n")
            time.sleep(2)
            os.system('cls')
            runing = False
            #else:
               # os.system('cls')
               # print("Please add a comma between first and last name")


def list():
    os.system('cls')
    m_leng = 0
    for firstn, lastn, gr1, gr2, gr3, gr4 in Student_list:
        if len(firstn + lastn) > m_leng:
            m_leng = len(firstn + lastn)
    for firstn, lastn, gr1, gr2, gr3, gr4 in Student_list:
        print(f"{lastn}, {firstn}:{' ' * (m_leng + 5 - len(firstn + lastn))}{gr1}% {gr2}% {gr3}% {gr4}%")
    time.sleep(1)
    input("To Return To Menu Press [Enter]")
    os.system('cls')


def student_av():
    os.system('cls')
    print("student averages")


def Course_av():
    os.system('cls')
    print("course average")


def exit_G():
    os.system('cls')
    print("See you next time")
    exit()


menus = {"1": add, "2": list, "3": student_av, "4": Course_av, "5": exit_G}
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
