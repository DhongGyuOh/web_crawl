import requests
from bs4 import BeautifulSoup

response = requests.get('https://mroh1226.tistory.com/')
html = response.text
soup = BeautifulSoup(html, 'lxml')
print(response.text)

titles = soup.select("strong.tit_post")
for t in titles:
    print(t.get_text(strip=True))
    
cates = soup.select("a.link_cate").attrs['date']
for c in cates:
    print(c.get_text(strip=True))

