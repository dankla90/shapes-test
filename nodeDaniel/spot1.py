from distutils.log import debug
import matplotlib.pyplot
from pyparsing import null_debug_action
import requests
import bs4
import rdflib
import spotlight 


textcontent = "my test text about Bergen city in Norway"

## THIS JUST TEST IF THE SITE IS UP AND SHOULD RETURN 200
## response = requests.get("https://www.dbpedia-spotlight.org/api")
## print(response.status_code)
## annotations = spotlight.annotate('https://api.dbpedia-spotlight.org/en/annotate',
##                                 textcontent,confidence=0.4,support=20)
## print(annotations)

url = input("Enter or Paste the URL: ")
url.strip()

response = requests.get(url)

try:
    print("Connecting To The Host .... " + url)
    res=requests.get(url)
    souped=bs4.BeautifulSoup(res.text,'lxml')
    
    ## FILTERING THE TEXT FROM WEBSITE      
    for a in souped(["script","style","link","img","nav","footer","title","meta"]):
        a.decompose()   

    text = souped.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    txtcontent = '\n'.join(chunk for chunk in chunks if chunk)
    
    ## ANNOTATION OF THE TEXT
    annotations = spotlight.annotate('https://api.dbpedia-spotlight.org/en/annotate',
                                 txtcontent,confidence=0.9,support=20)
    
    print(annotations)
    
except:
    print("Oops! An error has occurred or maybe you just entered an Invalid URL :D")

