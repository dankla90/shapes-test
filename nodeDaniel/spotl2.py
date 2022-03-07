import spotlight

annotations = spotlight.annotate('https://api.dbpedia-spotlight.org/en/annotate',
'Test about Bergen',confidence=0.4,support=20)
print(annotations)