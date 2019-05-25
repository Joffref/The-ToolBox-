'''
Project : The ToolBox
Module : txt_handler 
Version : 0.1
Author : Mathis JOFFRE
Last update : 25/05/2019
'''

from global_variable import txt_menu #menu import 
import os #os import 

def txt_file(): #create the fct 

    print (txt_menu)

    try:    
        txt_choice =int(input("Your choice : ")) #menu user choice 
    except ValueError:
        print (" YOU ARE SUCH STUPID DUDE ! ")

    if txt_choice == 1: #Create a txt file    
        txt_location = input("Path to create the file (write nothing to create it in the current one): ") 
        txt_name = input("Name of the file you want to create : ") 
        txt_document = open(txt_location + txt_name + ".txt", 'w+' )
        txt_document.close()

    if txt_choice == 2: #write in a txt file (automatic launch of the used prog. )   
        txt_location = input("Path to write the file (write nothing to write it in the current one): ") 
        txt_name = input("Name of the file you want to write : ")      
        os.startfile( txt_location + txt_name + '.txt')

    if txt_choice == 3: #read a file    
        txt_location = input("Path to read the file (write nothing to read it in the current one): ")    
        txt_name = input("Name of the file you want to read : ") 
        txt_document = open(txt_location + txt_name + ".txt", 'r' )

        if txt_document.mode == 'r':
            txt_content = txt_document.read()
            txt_document.close()

        print (txt_content)
        txt_copy = input("You want to save make a copy ? Y/N : ") 
     

        if txt_copy == 'Y': #make a copy 
            txt_document = open(txt_location + txt_name + "_copy.txt", 'w+' )
            txt_document.write(txt_content)
            txt_document.close()
        else:
            pass
    
    if txt_choice != 1 and txt_choice != 2 and txt_choice !=3: #verification of user choice 
        print('Damn')