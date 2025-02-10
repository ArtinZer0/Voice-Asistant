from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime
import pyautogui
import webbrowser
import time
import os
import random

""" serch only --> serch text in google chrome
serch --> serch text and visit to top link 
link --> open link (it's showld fix link)
type --> write taxt with keyboard button
type s --> press some button in one time
click --> click on pc with x(1,1900) and y(1,1000)
open --> open app in desktop folder
scroll --> scroll x secend
screenshot --> screenshot in real_time and save in screenshot folder
find screen --> find a object in screen & click """

__all__=["choice","serch_only","serch","link","type","type_s","click","open","scroll","screenshot"]

def fix(words:list,x):
    first_word=None
    first_position = len(x)
    for i in words:
        position = x.find(i)
        if position != -1 and position < first_position:
            first_position = position
            first_word = i
    if x.find(first_word)!=1:
        return x[:x.find(first_word)] + x[x.find(first_word) + len(first_word):]
    else:
        return x.replace(first_word,"")
def tt(x):
    y=list(x)
    y.pop()
    y.pop(0)
    return y
def choice(text):
    if "جستوجو" in text or "سرچ" in text or "جستجو" in text or "serch" in text or "search" in text:
        if "فقط" in text or "only" in text:
            serch_only(tt(text))
        else:
            serch(tt(text))
    elif "لینک" in text or "link" in text:
        link(tt(text))
    elif "تایپ" in text or "بنویس" in text or "write" in text:
        type(tt(text))
    elif "کلید" in text or "press" in text or "type s" in text :
        type_s(tt(text))
    elif "کلیک" in text or "click" in text :
        click(tt(text))
    elif "اجرا" in text or "باز" in text or "open" in text or "run" in text:
        open(tt(text))
    elif "اسکرول" in text or "scroll" in text:
        scroll(tt(text))
    elif "اسکرینشات" in text or "اسکرین شات" in text or "عکس از صفحه" in text or "عکس بگیر" in text or "screen" in text or "screen shot" in text:
        screenshot()
    else:
        print("I can't understand what you are saying")
def serch_only(serch_text):
    words=["سرچ","جستجو","جستوجو","serch","search"]
    words2=["فقط","only","just"]
    search_text=fix(words,serch_text)
    serch_text=fix(search_text,words2)
    try:
        webbrowser.open(f"https://www.google.com/search?q={serch_text}")
    except:
        print("Error")
def serch(x):
    words=["سرچ","جستجو","جستوجو","serch","search"]
    search_text=fix(words,x)
    driver = webdriver.Chrome(executable_path='D:\\coder\\code\\cumputer_project\\chromdriver\\chromedriver.exe')
    driver.get("https://www.google.com")
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.send_keys(search_text + Keys.RETURN)
    while True:
        try:
            body_element = driver.find_element(By.TAG_NAME, 'body')
            if 'srp' in body_element.get_attribute('class'):
                break
        except:
            time.sleep(0.1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    first_result_div = soup.find("div", class_="yuRUbf")
    if first_result_div:
        first_link = first_result_div.find("a")
        if first_link and first_link.has_attr("href"):
            first_link_url = first_link["href"]
            driver.get(first_link_url)
        else:
            pass
    else:
        pass
    while True:
        time.sleep(1)
def link(text):
    words=["لینک","link"]
    text=fix(words,text).strip()
    try:
        webbrowser.open(f"https://{text}")
    except:
        print("Error")
def type(text):
    if "بنویس" not in text or "تایپ" not in text:
        words=["type","write"]
        x=fix(words,text)
        for i in x: 
            pyautogui.write(i)
            time.sleep(0.07)
    else:
        pass
def type_s(keys):
    words=["press","type s"]
    x=fix(words,keys)
    x=keys.split(' ')
    if len(x)!=1:
        pyautogui.hotkey(*x)
    else:
        pyautogui.press(x[0])
def click(text):
    try:
        x=text.split(' ')
        y=[]
        for i in x:
            if i.isdigit() :
                y.append(int(i))
        pyautogui.click(y[0],y[1])
    except:
        pass
def open(app):
    words=["باز","open","run"]
    app=fix(words,app)
    username=os.getenv("USERNAME")
    os.startfile(f"C:\\Users\{username}\\OneDrive\\Desktop\\{app.strip()}")
def scroll(text):
    words=["scroll","اسکرول"]
    s=int(fix(words,text).strip())
    x=1
    u_d="d"
    kind="advans"
    if u_d=="d":
        x=-1
    if kind=="slow":
        scroll_amount = 20*x
    elif kind=="advans":
        scroll_amount=50*x
    elif kind=="fast":
        scroll_amount=100*x
    start_time = time.time()
    while time.time() - start_time < s:
        try:
            pyautogui.scroll(scroll_amount)
        except:
            pass
def screenshot():
    now = datetime.now()
    num=random.randint(100000,999999)
    date=now.strftime("%Y-%m-%d")
    username=os.getenv("USERNAME")
    screen=pyautogui.screenshot()
    screen.save(f"C:\\Users\\{username}\\OneDrive\\Pictures\\Screenshots\\Screenshot {date} {num}.png")