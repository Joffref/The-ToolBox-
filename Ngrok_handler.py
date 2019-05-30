from os import popen
from shlex import quote

def ngrok(port):
    my_server = popen('ngrok http {} '.format(quote(port))).read()
    print(my_server)
    