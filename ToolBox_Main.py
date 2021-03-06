'''
Project : The ToolBox
Module : Main prog. 
Version : 0.1
Author : Mathis JOFFRE
Last update : 25/05/2019
'''
from global_variable import titlescreen, webkit_menu, github_menu #menus import 
from txt_handler import txt_file #import of txt_file
from open_project import open_project #import of open_project 
from GitHub_handler import *
from Ngrok_handler import ngrok
from StackOverflow import stackoverflow_question
from shlex import quote
from os import system #import os to make some commands

def main_program(): #main 
    continue_ = True 
    while continue_:
        print(titlescreen)
        try:    
            main_choice = int(input("Your choice : ")) #choice of module
        except ValueError:
            print (" YOU ARE SUCH STUPID DUDE ! ")

        if main_choice == 1: 
            txt_file() #refers to txt_handler.py
        
        elif main_choice == 2:
            print (webkit_menu) 
            web_choice = input("args : ") #use to get the args 
            system("py WEBKIT\\WebKit.py " + quote(web_choice)) #launch script as commands with arguments
        
        elif main_choice == 3:
            open_project() #refers to open_project.py

        elif main_choice == 4:

            print(github_menu)

            try:
                git_choice = int(input('WHAT YOU WANT ?'))
            except ValueError:
                print (" YOU ARE SUCH STUPID DUDE ! ")

            if git_choice == 1:
                documents = []
                subtitles = []
                finished = False 
                while not finished:
                    document = input('Name of the Document (if there are all in memories type : finish): ')
                    subtitle = input('Subtitle of the Document : ')               
                    if document == "finish":
                        finished = True
                    else:
                        documents.append(document)
                        subtitles.append(subtitle)
                github_push(documents, subtitles)

            elif git_choice == 2:
                names = []
                finish = False 
                while not finish: 
                    name = input('Name of the Repository (if there are all in memories type : finish): ')  
                    if name == 'finish':
                        finish = True
                    else:
                        names.append(name)
                        
                github_fetch(names)


            else:
                print('YOU ARE SUCH STUPID DUDE !')
        
        elif main_choice == 5:
            try:    
                port = int(input("port : ")) #use to get the port
            except ValueError:
                print (" YOU ARE SUCH STUPID DUDE ! ")
            ngrok(port)

        elif main_choice == 6:
            article = input('WHAT IS YOUR PROBLEM : ')
            stackoverflow_question(article)

        else:
            print('SEE YOU LATER !')
            continue_ = False

        
if __name__ == '__main__':
    main_program()