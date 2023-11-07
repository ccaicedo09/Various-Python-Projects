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
      
    print(f"""#----------------------------------------------------------------------------------#
# Would you like to see the command line based projects or the GUI based projects? #
#----------------------------------------------------------------------------------#""")
    
    end = False
    while not end:
        print(f"# OPTIONS:                                                                         #\n# 1. Command line based projects                                                   #\n# 2. GUI based projects                                                            #\n# 3. Exit                                                                          #")
        option = input("# Choose an option: ")
        if option == "1":
            print(f"Hi")
            end = True
        elif option == "2":
            print("\nThis option isn't available yet, sorry! =(")
            end = True
        elif option == "3":
            print("\nSee you soon!")
            end = True        
            
main()
