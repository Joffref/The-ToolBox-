'''
Project : Webkit
Module : Main prog. 
Version : 0.1
Author : Mathis JOFFRE
Last update : 24/05/2019
'''
import argparse
import subprocess 
import os
from WebKitRessources import * #import menu 
from WebKitConfig import editor_path #import config 

def webkit(): #create the webkit fct 

    #parse the arguments entries

    parser = argparse.ArgumentParser()
    parser.add_argument("-O", "--output",  type=str, action="store", help="output of the project : 'C:\\path\\test'" )
    parser.add_argument("-T", "--title",  type=str, help="title of the project")
    parser.add_argument('-php', action="store_true", help="create php page in the project")
    parser.add_argument('-js', action="store_true", help="create js page in the project")
    args = parser.parse_args()

    if args.output: #check output true 
        try:
            path = str(args.output) + "\\" + str(args.title)
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:  
            print ("Successfully created the directory %s " % path)
        
    
    else: #if not 
        current_directory = str(os.getcwd()) + "\\" + str(args.title)
        try:
            path = current_directory
            os.mkdir(current_directory) 
        except OSError:   
            print ("Creation of the directory %s failed" % path)
        else:  
            print ("Successfully created the directory %s " % path)

    
    html_page = open(path + "\\" + args.title + ".html", 'w+')
    html_page.write(html_sample_page)
    html_page.close()
    

    if args.php: #check php arg and create 
        php_page = open(path +  "\\" + args.title +  ".php", 'w+')
        php_page.write(php_sample_page)
        php_page.close()
        
        
    if args.js: #check js arg and create
        js_page = open(path + "\\" +args.title + ".js", 'w+')
        js_page.write(js_sample_page)
        js_page.close()
        
    
    subprocess.Popen((editor_path, path)) #open project with the user editor (need to fill WebKitconfig.py)


    
if __name__ == '__main__':
    webkit()