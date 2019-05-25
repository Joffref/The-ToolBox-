from os import system 

def github_push(documents, subtitles):
    for document in documents:
        for subtitle in subtitles:
            system('git add ' + document)
            system('git commit -m  "{}"'.format(subtitle))

def github_fetch(names):
    for name in names:
        system('git fetch ' + name)
    

        
