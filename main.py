"""
This file works as a menu to go to the project the user wants to give a look to 
(both command line and GUI based projects), through the command line. 
"""
import os
import pyfiglet
import time

def main():
    os.system("cls")
    print(f"{pyfiglet.figlet_format("Wellcome to my projects!  =)", font="big")}")
    time.sleep(3)
    os.system("cls")
      
    print("------------------------------------------------------------------\nWould you like to see the command line or the GUI based projects?")
    
    end = False
    
    while end == False:
        print("------------------------------------------------------------------\n1. Command line projects\n2. GUI based projects\n3. Exit")
        option = input("------------------------------------------------------------------\nChoose an option: ")
        
        if option == "1":
            print("------------------------------------------------------------------\n1. Test\n2. Exit")
            end = True
        elif option == "2":
            print("------------------------------------------------------------------\nNo uploaded projects yet, sorry. =(")
            end = True
        elif option == "3":
            end = True
        else:
            print("------------------------------------------------------------------\nInvalid option, try again.")
            time.sleep(2)
            os.system("cls")
main()
