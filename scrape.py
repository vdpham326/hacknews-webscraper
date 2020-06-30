import requests
from bs4 import BeautifulSoup # import Beatifulsoup to scrape web pages
import pprint

res = requests.get('https://news.ycombinator.com/') #request information from hackernews website
res2 = requests.get('https://news.ycombinator.com/news?p=2') #request data from the 2nd page
soup = BeautifulSoup(res.text, 'html.parser') # convert into html format and assign to soup variable
soup2 = BeautifulSoup(res2.text, 'html.parser') # convert into html format and assign to soup variable

links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup.select('.storylink')
subtext2 = soup.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = [] # list to hold the titles of the links
    for idx, item in enumerate(links):
        title = item.getText() #get the title of each link
        href = item.get('href', None) #grab the links for each title, if no links then set to None
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points}) #append a dictionary which holds the title and the link 
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))