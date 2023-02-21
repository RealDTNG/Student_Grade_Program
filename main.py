
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
    
def menu():
    menus = {0:add, 1:list, 2:Student_av, 3: Course_av, 4:exit_G}
    while True:
        print("1 | To Add Or Remove Students")
        print("2 | To View The List")
        print("3 | To View The Student Averages")
        print("4 | To View The Course Average")
        print("5 | To Exit")
        choice = int(input(f"Please pick a menu option\n\n:"))-1
        #while choice not in menus:
        #    print("ERROR, Please enter a valid choice")
        #    choice = input(f"Please pick a menu option\n\n:")
        menus[choice]



menu()
