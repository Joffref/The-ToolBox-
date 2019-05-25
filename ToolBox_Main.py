'''
Project : The ToolBox
Module : Main prog. 
Version : 0.1
Author : Mathis JOFFRE
Last update : 24/05/2019
'''
from global_variable import titlescreen, webkit_menu, github_menu #menus import 
from txt_handler import txt_file #import of txt_file
from open_project import open_project #import of open_project - WIP
from GitHub_handler import *
from Ngtok_handler import ngrok
import os #import os to make some commands

def main_program(): #main 

    print(titlescreen)

    try:    
        main_choice = int(input("Your choice : ")) #choice of module
    except ValueError:
        print (" YOU ARE SUCH STUPID DUDE ! ")

    if main_choice == 1: 
        txt_file() #refers to txt_handler.py
    
    if main_choice == 2:
        print (webkit_menu)
        try:    
            web_choice =str(input("args : ")) #use to get the args 
        except ValueError:
            print (" YOU ARE SUCH STUPID DUDE ! ")

        os.system("py WEBKIT\\WebKit.py " + web_choice) #launch script as commands with arguments
    
    if main_choice == 3:
        open_project() #refers to open_project.py

    if main_choice == 4:

        print(github_menu)

        try:
            git_choice = int(input('WHAT YOU WANT ?'))
        except ValueError:
            print (" YOU ARE SUCH STUPID DUDE ! ")

        if git_choice == 1:
            documents = []
            subtitles = []
            finish = False 
            while finish is False:
                try: 
                    document = str(input('Name of the Document (if there are all in memories type : finish): '))
                    subtitle = str(input('Subtitle of the Document : '))
                except ValueError:
                    print (" YOU ARE SUCH STUPID DUDE ! ")
                
                if document == 'finish':
                    finish = True
                else:
                    documents.append(document)
                    subtitles.append(subtitle)
            github_push(documents, subtitles)

        if git_choice == 2:
            names = []
            finish = False 
            while finish is False:
                try: 
                    name = str(input('Name of the Repository (if there are all in memories type : finish): '))       
                except ValueError:
                    print (" YOU ARE SUCH STUPID DUDE ! ")
                
                if name == 'finish':
                    finish = True
                else:
                    names.append(name)
                    
            github_fetch(names)


        if git_choice !=1 and git_choice!=2:
            print('YOU ARE SUCH STUPID DUDE !')
    
    if main_choice == 5:
        try:    
            port = int(input("port : ")) #use to get the port
        except ValueError:
            print (" YOU ARE SUCH STUPID DUDE ! ")
        ngrok(port)

        

        
        

if __name__ == '__main__':
    main_program()