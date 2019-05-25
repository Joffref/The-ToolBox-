from os import popen

def ngrok(port):
    my_server = popen('ngrok http {} '.format(port)).read()
    print (my_server)
    