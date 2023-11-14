"""
This file works as a menu to go to the project the user wants to give a look to 
(both command line and GUI based projects), through the command line. 
"""
import os
import time
import pyfiglet
from Command_Line_Based_Projects import GuessTheWord_es

class Menu():
    
    def __init__(self):
        pass
    
    def wellcome():
        os.system("cls")
        print(f"{pyfiglet.figlet_format("Wellcome to my projects!  =)", font="big")}")
        time.sleep(1.5)
        os.system("cls")
        
    def main_menu(): #Asks user which type of project do they want to see
        print("\n------------------OPTIONS------------------\n")
        print("Would you like to see command line or GUI based projects?\n-1. Command Line Based Projects\n-2. GUI Based Projects\n-3. Exit")
        type_option = int(input("\nChoose an option ---> "))

        return type_option
    
    def choose_project(type_option):
        os.system("cls")
        print("\n------------------OPTIONS------------------\n")
        if type_option == 1:
            print("-1. Guess The Word (Spanish Version)\n-2. Exit main menu\n-3. Exit")
            project_option = int(input("\nChoose an option ---> "))
        elif type_option == 2:
            print("-1. Test\n-2. Exit main menu\n-3. Exit")
            project_option = int(input("\nChoose an option ---> "))

        return project_option
        
def main():
    
    main_menu_option = Menu.main_menu()
    end = False
    if main_menu_option == 3:
        end = True
    
    if not end:   
        if main_menu_option == 1:
            #CHOOSE PROJECT WITHIN CLB PROJECTS
            project_menu_option = Menu.choose_project(main_menu_option)
            if project_menu_option == 1:
                GuessTheWord_es.main()
            elif project_menu_option == 2:
                main()
            else:
                end = True
        
        if main_menu_option == 2:
            #CHOOSE PROJECT WITHIN GUIB PROJECTS
            project_menu_option = Menu.choose_project(main_menu_option)
            if project_menu_option == 1:
                print("Test")
            elif project_menu_option == 2:
                main()
            else:
                end = True
            
if __name__ == "__main__":
    Menu.wellcome()
    main()
