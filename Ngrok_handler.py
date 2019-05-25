import os 

def ngrok(port):
    my_server = os.popen('ngrok http {} '.format(port)).read()
    print (my_server)
    
