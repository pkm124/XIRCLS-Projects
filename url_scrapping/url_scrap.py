import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.xircls.com/")
soup = BeautifulSoup(page.content, 'html.parser')

page_title = soup.title.text

text = page.text
status = page.status_code

page_head = soup.head
page_body = soup.body

#first_h1 = soup.select('h1')[0].text
set_url=set()
for i in soup.select('a'):
    if i.get('href')[0] == '/' and i.get('href') != '/':
        set_url.add(i.get('href'))

# print(set_url)

for i in list(set_url):
    print(i)
# print(first_h1)
# print(page_head, page_body)
# print(text, status)
# print(page_title)

