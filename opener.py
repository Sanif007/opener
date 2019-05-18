""" This tool is basically just a file opener. By using this you can open and read or write text in files. """

import os, time, re, sys
def banner():
     print("   ▄████▄   ██▄███▄    ▄████▄   ██▄████▄   ▄████▄    ██▄████")
     print("  ██▀  ▀██  ██▀  ▀██  ██▄▄▄▄██  ██▀   ██  ██▄▄▄▄██   ██▀")
     print("  ██    ██  ██    ██  ██▀▀▀▀▀▀  ██    ██  ██▀▀▀▀▀▀   ██")
     print("  ▀██▄▄██▀  ███▄▄██▀  ▀██▄▄▄▄█  ██    ██  ▀██▄▄▄▄█   ██")
     print("    ▀▀▀▀    ██ ▀▀▀      ▀▀▀▀▀   ▀▀    ▀▀    ▀▀▀▀▀    ▀▀")
     print("            ██  \033[91m V. 2.0 \033[0m ")
     print("                          \033[1;92mCoded by github.com/Sanif007 \033[0m ")

def menu():
          print(" 1. Read  ")
          print(" 2. Write ")
          print(" 3. Erase")
          print(" 4. Delete ")
          print(" 5. Search word ")

def controls():
     op = int(input(">>> "))
     if op ==  1 :
       file_opening = open(filename, "rb")
       print("Got your file.. \n ")
       time.sleep(2)
       for line in file_opening : print(line)
       time.sleep(1)
       print(" \nFile ends here ! ")
       file_opening.close()
       f.close()
     elif op == 2 :
       file_opening = open(filename , "w")
       print("Got your file \n ")
       time.sleep(2)
       print(" By default you can write 3 lines only ")
       line1 = input("Line 1. ")
       line2 = input("Line 2. ")
       line3 = input("Line 3. ")
       file_opening.write(line1)
       file_opening.write("\n")
       file_opening.write(line2)
       file_opening.write("\n")
       file_opening.write(line3)
       print(" Completed !! ")
       file_opening.close()
       f.close()
     elif op == 3 :
       file_opening = open(filename , "w")
       print("Do you really want to erase? (Default: no) ")
       q = input(">>>")
       if q == "yes" or q == "Yes" or q == "y" :
          file_opening.truncate()
          time.sleep(2)
          print(" Erased !!! ")
          file_opening.close()
       else :
          print("Going back to menu \n ")
          time.sleep(1)
          banner()
          menu()
          controls()
       f.close()
     elif op == 4 :
       print("Do you really want to delete this file? (default:no)  ")
       q = input(">>> ")
       if q == "yes" or q == "Yes" or q == "y" : 
            os.remove(filename)
            time.sleep(2)
            print("Done!!!")
       else :
            print("going back to menu \n ")
            time.sleep(1)
            banner()
            menu()
            controls()
       f.close()
     elif op == 5 :
       word = input("Enter word : ")
       time.sleep(1)
       print(" Your word would be seen in form of ( , ) ")
       time.sleep(2)
       print(re.split(word, str))
       f.close()
     else :
       print("\033[1;91mInvalid option. \033[0m ")

banner()
filename = input("Enter filename : " )
if os.path.exists(filename) :
     menu()
     f = open(filename, "rb")
     str = str(f.read())
     controls()
else:
     print("\033[31m File not found!! \033[0m")