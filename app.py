from flask import Flask, redirect,render_template,request, url_for
import urllib.request, urllib.parse, urllib.error
import ssl
import json
from bs4 import BeautifulSoup

#ignore ssl certifications
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#manifest function
def getman(name):
  url='https://api.nasa.gov/mars-photos/api/v1/manifests/'+name+'/?api_key=nYwrcNmkss4hgGyMnI2I9TYwcWkshu4MRlOACIy3'
  html = urllib.request.urlopen(url, context=ctx).read()

  soup = BeautifulSoup(html, 'html.parser')
# Retrieve all the info
  maintext=soup.prettify()
  info=json.loads(maintext)
  return info

def getpics(name,sol):
  url="https://api.nasa.gov/mars-photos/api/v1/rovers/"+name+"/photos?sol="+sol+"&api_key=nYwrcNmkss4hgGyMnI2I9TYwcWkshu4MRlOACIy3"  
  html = urllib.request.urlopen(url, context=ctx).read()

  soup = BeautifulSoup(html, 'html.parser')
# Retrieve all the info
  maintext=soup.prettify()
  pics=json.loads(maintext)
  return pics
 

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
  info=""
  if request.method=='POST':
    ans=request.form['rover']
    sol_val=request.form['sol']
    # print(ans)
    # print(sol_val)
    info=getpics(ans,sol_val)
    # print(info)
    
  return render_template('index.html',info=info)


  
if __name__ == '__main__':
    app.run(debug=True)