from collections import UserString
from typing import Tuple
from matplotlib.pyplot import annotate
from pyparsing import null_debug_action
import requests
from bs4 import BeautifulSoup
import bs4
import rdflib
import spotlight

## input = UserString

response = requests.get("https://www.dbpedia-spotlight.org/api")
print(response.status_code)
## annotate('test Bergen is a great city', Tuple[0.5, 0.7])

annotations = spotlight.annotate('https://www.dbpedia-spotlight.org/api',
                                  'Your test text',
                                  confidence=0.4, support=20)