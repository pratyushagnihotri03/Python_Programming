import random
import urllib.request #Get data from web

def download_web_image(url):
    name = random.randrange(1, 1000) # It will download and store image with name from 1 to 1000
    full_name = str(name) + ".jpg"
    # url: Url of the website to download images.
    # full_name: name of file to save
    urllib.request.urlretrieve(url, full_name)

download_web_image("http://comicsalliance.com/files/2011/08/league00.jpg")