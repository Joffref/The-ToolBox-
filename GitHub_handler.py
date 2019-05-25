'''
Project : The ToolBox
Module : GitHub 
Version : 0.1
Author : Mathis JOFFRE
Last update : 25/05/2019
'''
from os import system 

def github_push(documents, subtitles):
    for document in documents:
        for subtitle in subtitles:
            system('git add ' + document)
            system('git commit -m  "{}"'.format(subtitle))

def github_fetch(names):
    for name in names:
        system('git fetch ' + name)
 