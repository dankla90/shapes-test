from collections import UserString
import string
from typing import Tuple
from matplotlib.pyplot import annotate
## from pyparsing import null_debug_action
import requests
from bs4 import BeautifulSoup
## import bs4
## import rdflib
import spotlight 




## input = UserString
textcontent = "my test text about Bergen city in Norway"

## THIS JUST TEST IF THE SITE IS UP AND SHOULD RETURN 200
response = requests.get("https://www.dbpedia-spotlight.org/api")
print(response.status_code)


## THIS WAS MY FIRST TRY, AND IT SHOULD WORK, BUT I AM GETTING AN ERROR HERE TOO
## annotations = spotlight.annotate("https://www.dbpedia-spotlight.org/api",
##                                  textcontent,
##                                  confidence=0.4, support=20)
params = "my test text about Bergen city in Norway, confidence=0.5, support=20"

## THIS CODE I GOT FROM A GITHUB, AND SHOULD WORK
##annotations = spotlight.annotate('http://spotlight.dbpedia.org/rest/annotate', textcontent, confidence=0.5, support=20)

 

annotations = spotlight.annotate('https://api.dbpedia-spotlight.org/en/annotate',textcontent,confidence=0.4,

support=20)
## TESTING
## annotations2 = requests.get('http://spotlight.dbpedia.org/rest/annotate', params)
print(annotations)
## print(annotations2)
## extra code for safe keeping

url = input("Enter or Paste the URL: ")
name = input("Save File As ? : ")
url.strip()

try:
    print("Connecting To The Host .... " + url)
    res=requests.get(url)
    souped=bs4.BeautifulSoup(res.text,'lxml')
        
    for a in souped(["script","style","link","img","nav","footer","title","meta"]):
        a.decompose()   

    text = souped.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    txtcontent = '\n'.join(chunk for chunk in chunks if chunk)

    fname=str(name)+".txt"
    freader = open(fname, "w",encoding="utf-8")
    freader.write("*****Document Generated Using Web Scraper By Ishan Sharma(github.com/ishandeveloper)*****\n\n")
    freader.write(str(txtcontent))
    freader.close()
    print(fname + " File Successfully Created")  
  
except:
    print("Oops! An error has occurred or maybe you just entered an Invalid URL :D")

