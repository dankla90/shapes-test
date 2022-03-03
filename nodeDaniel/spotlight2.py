import spotlight
import matplotlib
import requests
from spotlight import annotate

annotations = spotlight.annotate('https://api.dbpedia-spotlight.org/en/annotate',
'Test about Bergen',confidence=0.4,support=20)
print(annotations)