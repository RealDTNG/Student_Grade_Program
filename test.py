import os, time, msvcrt
            
def find():
    
    time.sleep(1)
    os.system('cls')
    
    running = True
    fname = []
    
    while running:
        temp_letter = ""
        
        print(f"Press [Enter] to submit name\nSudents first name: [{''.join(fname)}]\n")
        
        temp_letter = msvcrt.getche()
        
        os.system('cls')
        
        if temp_letter == (b'\x08'):
            try:
                fname.pop()  
            except:
                os.system('cls')
                print(f"ERROR\nThere Are No More Characters")
                time.sleep(1)
                os.system('cls')
        elif temp_letter == (b'\r'):
            running = False
            print("Done")
        else:
            fname.append(temp_letter.decode('ASCII'))
            
                  
find()