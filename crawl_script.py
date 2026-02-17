import requests
from bs4 import BeautifulSoup
import pandas as pd
from playwright.sync_api import sync_playwright
# import nest_asyncio
# nest_asyncio.apply()

url = "https://m.blog.naver.com/thebigsun?tab=1"
titleList = []

def GetTitles(html):
    soup = BeautifulSoup(html,'lxml')
    titles = soup.select('strong > span')
    for title in titles:
        print(title.text)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(url)

    # JS 로딩 대기
    page.wait_for_load_state("networkidle")

    html = page.content()
    GetTitles(html)
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(1200)

    # 새로운 요소가 나타날 때까지 기다리기 (선택적)
    #page.wait_for_selector("div.card__reUkU", timeout=10000)  # 새 카드가 로드될 때까지
    html2 = page.content()
    print("\n\n\n\n")
    GetTitles(html2)

    browser.close()

    previous_height = 0

# 끝까지 스크롤하기
# while True:
#     # 현재 높이 가져오기
#     current_height = page.evaluate("document.body.scrollHeight")

#     # 더 이상 증가 안 하면 종료
#     if current_height == previous_height:
#         break

#     # 맨 아래로 스크롤
#     page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

#     # 로딩 대기
#     page.wait_for_timeout(1500)

#     previous_height = current_height

# print("스크롤 완료")





