'''
Project : The ToolBox
Module : open_project
Version : 0.1
Author : Mathis JOFFRE
Last update : 25/05/2019
'''
import subprocess
from WEBKIT import WebKitConfig
from global_variable import open_project_menu

def open_project():
    print (open_project_menu)
    try:
        open_project_choice = int(input("WHAT DO YOU WANT :"))
    except ValueError:
        print (" YOU ARE SUCH STUPID DUDE ! ")

    if open_project_choice == 1:
        open_project_path = input("PATH (C:\\test\\ect) :")
        try:
            subprocess.Popen((WebKitConfig.editor_path, open_project_path))
        except subprocess.CalledProcessError:
            print ('YOU MUST CONFIGURE WebKitConfig.py IN WEBKIT FOLDER')
        

    elif open_project_choice == 2:
        try:
            subprocess.Popen((WebKitConfig.editor_path))
        except subprocess.CalledProcessError:
            print ('YOU MUST CONFIGURE WebKitConfig.py IN WEBKIT FOLDER')
    
    else:
        print('INVALID ARGUMENT')
        