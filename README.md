아래는 **GitHub 저장소 › web_crawl** ([https://github.com/DhongGyuOh/web_crawl)를](https://github.com/DhongGyuOh/web_crawl%29를) 기준으로 만든 **README.md** 예시입니다. 이 저장소는 파이썬／Playwright를 이용한 간단한 웹 크롤링 스크립트들을 포함하고 있습니다.

---

# web_crawl

Python 기반 웹 크롤링 예제 모음 프로젝트입니다.
간단한 웹 요청 크롤러와 Playwright 기반 웹 브라우저 크롤러를 포함하고 있습니다.

---

## 📦 프로젝트 구조

```
web_crawl/
├── crawl_script.py      # requests + BeautifulSoup 기반 간단 크롤링
├── test.py              # Playwright 기반 브라우저 크롤링 테스트
├── level1.ipynb         # Naver 크롤링 예제 노트북
└── README.md            # 프로젝트 설명 (이 문서)
```

---

## 🧠 소개

이 저장소는 웹 크롤링 학습 및 테스트를 위한 간단한 코드 모음입니다.
파이썬 `requests`, `BeautifulSoup`, 그리고 `Playwright`를 활용한 크롤링 예제를 담고 있습니다.

---

## 🧪 예제 코드 설명

### 🔹 crawl_script.py (requests + BeautifulSoup)

```python
import requests
from bs4 import BeautifulSoup

response = requests.get('https://mroh1226.tistory.com/')
html = response.text
soup = BeautifulSoup(html, 'lxml')
print(response.text)

titles = soup.select("strong.tit_post")
for t in titles:
    print(t.get_text(strip=True))

cates = soup.select("a.link_cate")
for c in cates:
    print(c.get_text(strip=True))
```

➡ 특정 블로그 페이지를 받아와서 **title**과 **category**를 추출하는 간단한 크롤러입니다.
(BeautifulSoup 셀렉터는 페이지 구조에 맞춰 변경해야 함)

---

### 🔹 test.py (Playwright)

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()
```

➡ Playwright를 통해 브라우저를 띄워서 웹 페이지의 제목(title)을 출력하는 예제입니다.

---

### 📓 level1.ipynb (Jupyter Notebook)

Notebook에서는 **네이버 메인 페이지 제목**을 출력하는 간단한 BeautifulSoup 크롤러 예제가 포함되어 있습니다.

---

## 🚀 시작하기

### 📌 필수 설치

```bash
pip install requests beautifulsoup4 lxml
```

Playwright 환경 설치 (브라우저 포함):

```bash
pip install playwright
playwright install
```

---

## 💡 사용 방법

1. 저장소를 로컬로 클론합니다.

```bash
git clone https://github.com/DhongGyuOh/web_crawl.git
cd web_crawl
```

2. 스크립트를 실행합니다.

```bash
python crawl_script.py
python test.py
```

3. 크롤링할 대상 URL, 선택자(selector) 등을 본인 목적에 맞게 수정해서 활용하세요.

---

## 📝 주의사항

* 웹 크롤링 시 **robots.txt**와 웹사이트 이용 약관을 준수하세요.
* 많은 요청을 동시에 보내면 서비스에 부담을 줄 수 있으므로 적절한 딜레이를 사용하세요.

---

## 🔧 참고

웹 크롤링은 “HTML 파싱 → 데이터 추출”의 반복입니다.
크롤링과 스크레이핑(web scraping)의 기본은 비슷하며, 라이브러리 선택에 따라 기능과 성능이 달라집니다. ([github.com][1])

---

원하면 **기능별 확장 예제** (이미지 다운로드, 동적 컨텐츠 크롤링, 데이터 저장 등)도 추가로 만들어줄 수 있어!

[1]: https://github.com/topics/web-crawling?utm_source=chatgpt.com "web-crawling · GitHub Topics · GitHub"
