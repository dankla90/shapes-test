import spotlight
import requests
import bs4



print("WEB SCRAPPER")
url = input("Enter or Paste the URL: ")
name = input("Save File As ? : ")
url.strip()

try:
    print("Connecting To The Host .... " + url)
    res=requests.get(url)
    souped=bs4.BeautifulSoup(res.text,'lxml')
        
    for a in souped(["script", "style","link","img","nav","footer","title","meta"]):
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


annotations = spotlight.annotate('https://api.dbpedia-spotlight.org/en/annotate',
'Test about Bergen',confidence=0.4,support=20)
## print(annotations)


##tagcloud with difference of with tags or not and tables
