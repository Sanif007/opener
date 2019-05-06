""" This tool is basically just a file opener. By using this you can open and read or write text in files. """

import os, re 
def menu():
          print(" 1. Read  ")
          print(" 2. Write ")
          print(" 3. Erase")
          print(" 4. Search word ")

def conrols():
     op = int(input(">>> "))
     if op ==  1 :
       file_opening = open(filename , "rb")
       print("Got your file.. ")
       print()
       for line in file_opening : print(line)
       print()
       print(" File ends here ! ")
       file_opening.close()
     elif op == 2 :
       file_opening = open(filename , "w")
       print("Got your file ")
       print()
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
     elif op == 3 :
       file_opening = open(filename , "w")
       file_opening.truncate()
       print(" Erased !!! ")
       file_opening.close()
     elif op == 4 :
       word = input("Type word here : ")
       file = str(filename)
       print(re.split(word, file))
     else :
       print("Not valid option. choose 1 or 2 or 3 ")


filename = input(" Enter filename : ")
if os.path.exists(filename) :
     menu()
     conrols()
else:
     print("\033[31m File not found!! \033[0m")