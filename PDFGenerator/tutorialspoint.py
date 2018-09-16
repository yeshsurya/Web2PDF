import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import pdfkit
next_urls=[]
def get_next_route(next_button):
    ret = ''
    next_soups=[]
    for va in next_button:
       next_soups.append(BeautifulSoup(str(va),features='html.parser'))
    for el in next_soups[0].findChildren('a'):
        ret = el['href']
    return ret
def get_next_url(any_location,next_button):
    next_route = get_next_route(next_button)
    u_parse_result = urlparse(any_location)
    base_url = u_parse_result.scheme + "://" + u_parse_result.netloc
    return base_url+next_route

def list_all_urls(any_url):
    global next_urls
    page = requests.get(any_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    next_button =soup.find_all('div', class_='nxt-btn')
    next_url = get_next_url(any_url,next_button)
    if(next_url not in next_urls):
        next_urls.append(next_url)
        list_all_urls(next_url)
    else:
        return


list_all_urls("https://www.tutorialspoint.com/django/django_apps_life_cycle.htm")
outile = open('result.txt','w')
for var in next_urls:
    outile.write(str(var))

pdfkit.from_url("https://www.tutorialspoint.com/django/django_apps_life_cycle.htm", 'django.pdf')
#pdfkit.from_file(['file1.html', 'file2.html'], 'out.pdf')
#pdfkit.from_url('https://www.google.co.in/','shaurya.pdf')
# u_parse_result = urlparse("https://www.tutorialspoint.com/django/django_apps_life_cycle.htm")
# base_url = u_parse_result.scheme+"://"+u_parse_result.netloc #u_parse_result.netloc
# page = requests.get("https://www.tutorialspoint.com/django/django_apps_life_cycle.htm")
# soup = BeautifulSoup(page.content, 'html.parser')
#[print(type(item)) for item in list(soup.children)]



