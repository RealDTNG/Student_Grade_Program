import os, time, msvcrt

def add():          # function to add students
    time.sleep(1)
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
            os.system('cls')
            print("Successfully Added A Student\n")
            running = False             # end loop to return to menu
            time.sleep(2)
            os.system('cls')
            
def find():
    time.sleep(1)
    os.system('cls')
    running = True
    fname = ""
    while running:
        print(f"Sudents first name:{fname}{fname = msvcrt.getch()}")
        
            
choice = msvcrt.getche()
if choice.decode('ASCII') in menus:
    menus[choice.decode('ASCII')]()            

add()