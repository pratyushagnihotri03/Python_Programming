import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('a', {'class': 'index_singleListingTitles'}):
        content = post_text.string  # only string and removing all the crap
        words = content.lower.spilt()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)

start('https://buckysroom.org/tops.php?type=text&period=this-month')
