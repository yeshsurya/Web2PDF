import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
u_parse_result = urlparse("https://www.tutorialspoint.com/django/django_apps_life_cycle.htm")
base_url = u_parse_result.scheme+"://"+u_parse_result.netloc #u_parse_result.netloc
page = requests.get("https://www.tutorialspoint.com/django/django_apps_life_cycle.htm")
soup = BeautifulSoup(page.content, 'html.parser')
mid_content = soup.find_all('div',class_="col-md-7 middle-col")
test = open('test.html','w')
test.write(str(mid_content[0].encode("utf-8")))