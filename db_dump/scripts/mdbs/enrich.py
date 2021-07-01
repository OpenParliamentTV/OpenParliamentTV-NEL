import json
import os
import sys
from urllib.request import urlopen

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import helpers

# How to query the licence data from images from wikidata? Stackoverflow post: 
# https://stackoverflow.com/questions/7453654/retrieving-image-license-and-author-information-in-wiki-commons

WIKIPEDIA_ASSET_API = "https://en.wikipedia.org/w/api.php?action=query&prop=imageinfo&iiprop=extmetadata&format=json&titles="
FILE_NAME = "File%3aBrad_Pitt_at_Incirlik2.jpg"

INFILE = 'db_dump/data/mdbs/mdbs-final.json'

with open(INFILE) as infile:
    data = json.load(infile)
    for e in data:
        if 'thumbnailURI' in e:
            print("Thumbnail yes!")
            response = urlopen(WIKIPEDIA_ASSET_API + FILE_NAME)
            data = json.loads(response.read())
            print(data)
        else:
            print("Thumbnail no")

