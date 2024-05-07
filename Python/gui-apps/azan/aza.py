from pywebio.output import *
from pywebio.input import *
from pywebio.input import input as put_input
from pywebio import start_server
from pywebio.session import *
import requests as req

user = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
def l():
    url = 'http://api.aladhan.com/v1/timingsByCity?city=cairo&country=eygpt&method=5'

    response = req.get(url,headers=user)
    info = response.json()
    if "data" in info:
        timings = info["data"]["timings"]
        return timings
    else :

        return None
        
def web():
    time= l()
    
    # put_html('<head><title>مواقيت الصلاة في مصر </title></head>')
    put_html('<h1><strong><center>مواقيت الصلاة في مصر</center></strong></h1>')
    put_text('\n')
    put_html('<center><img src= "https://repository-images.githubusercontent.com/73611561/c6331a00-ff38-11e9-96eb-6cc244479c28" width=1000></center>')
    put_text('\n\n\n')
    # put_input("Select an option", type=put_input.SELECT, options=['sdfhal'])

start_server(web , port=8080,debug=True)
