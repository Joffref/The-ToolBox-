import requests  
import json
import webbrowser

def stackoverflow_question(article_title):

    continuer = True
    i = 0
    article_title_1 = article_title.replace(' ', '%20')
    url = 'https://api.stackexchange.com/2.2/similar?order=asc&sort=relevance&title=' + article_title_1 + '&site=stackoverflow'
    reponse = requests.get(url).json()

    while continuer:
        i += 1
        try:
            formated_reponse = reponse['items'][i]['accepted_answer_id']
        except KeyError:
            continue   

        if len(str(formated_reponse)) != 0:
            continuer = False

        if i > len(reponse['items']):
            print('TRY ANOTHER KEYWORDS')
            continuer = False 
        
    url_answer = 'https://api.stackexchange.com/2.2/posts/'+ str(formated_reponse) +'?order=desc&sort=activity&site=stackoverflow'
    reponse_answer = requests.get(url_answer).json()
    formated_reponse_answer = reponse_answer['items'][0]['link']
    webbrowser.open(formated_reponse_answer)
