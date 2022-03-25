import requests
import bs4
import spotlight 
import sys

def main():

    ## url = input("Enter or Paste the URL: ")
    url = sys.argv[1:]
    url = ' '.join(url)
    url.strip()
    
    try:
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
                                    txtcontent,confidence=0.9,support=40)
        

        annotationsUpdated = []
        for dict_item in annotations:
                item = (dict_item['URI'])
                annotationsUpdated.append(item)

        annotationsUpdated = list(dict.fromkeys(annotationsUpdated))
        ## print(annotations)
        ## print(annotationsUpdated)
        return(annotationsUpdated)

    except:
        return ("Oops! An error has occurred or maybe you just entered an Invalid URL :D")

main()