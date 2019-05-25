import os 

def github_push(documents, subtitles):
    for document in documents:
        for subtitle in subtitles:
            os.system('git add ' + document)
            os.system('git commit -m  "{}"'.format(subtitle))

def github_fetch(names):
    for name in names:
        os.system('git fetch ' + name)
    

        