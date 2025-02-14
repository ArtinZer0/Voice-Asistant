from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import speech_recognition as sr
from selenium import webdriver
from datetime import datetime
from bs4 import BeautifulSoup
from word2number import w2n
import customtkinter as ctk
from random import randint
import sounddevice as sd
from time import sleep
from PIL import Image 
import webbrowser
import threading
import pyautogui
import requests
import pyttsx3
import sqlite3
import random
import queue
import vosk
import time
import os

class Order:

    """ serch only --> serch text in google chrome
        serch --> serch text and visit to top link 
        link --> open link (it's showld fix link)
        type --> write taxt with keyboard button
        press --> press some button in one time
        click --> click on pc with x(1,1900) and y(1,1000)
        scroll --> scroll x secend
        screenshot --> screenshot in real_time and save in screenshot folder
    """
    
    def __init__(self):
        self.__all__ = ["choice","serch_only","serch","link","type","press_key","click","scroll","screenshot"]
        self.directory_name = os.path.dirname(os.path.realpath(__file__))
        self.engin = pyttsx3.init()
        self.engin.setProperty('rate', 130)

    def tt(self,x):
        try:
            y=list(x)
            y.pop(0)
            if y[0] == 't' and y[1] == 'h' and y[2] == 'e':
                y.pop(0)
                y.pop(0)
                y.pop(0)
                y.pop(0)
            elif y[0] == 'a' and y[1] == ' ':
                y.pop(0)
                y.pop(0)
            y.pop()
            return "".join(y)
        except:
            pass
    
    def aa(self,x):
        try:
            y = list(x)
            if y[0] == 't' and y[1] == 'h' and y[2] == 'e':
                y.pop(0)
                y.pop(0)
                y.pop(0)
                y.pop(0)
            elif y[0] == 'a' and y[1] == ' ':
                y.pop(0)
                y.pop(0)
            return "".join(y)
        except:
            pass

    def check_conection(self):
        stutos=True
        try:
            x = requests.get("https://www.google.com")
        except:
            stutos = False
        return stutos
    
    def fix(self, x:str):
        try:
            y = x.split(' ')
            y.pop(0)
            return ' '.join(y)
        except:
            pass
    
    def foo2(self,text):
        try:
            x = text.split()
            n = 0
            a = None
            b = None
            for i in x:
                if i == 'and':
                    n += 1
                if i.isdigit() and n == 0:
                    a = int(i)
                elif i.isdigit() and n>0:
                    b = int(i)
            return [a,b]
        except:
            pass

    def foo(self,text):
        try:
            x = text.split()
            n = 0
            a = None
            for i in x:
                if i=='and':
                    n+=1
                if i.isdigit() and n==0:
                    a=int(i)
            return a
        except:
            pass

    def find_number_c(self,num_text):
        try:
            x = num_text.split('and')
            l = []
            try:
                for i in x:
                    l.append(w2n.word_to_num(i))
                return l
            except:
                l = self.foo2(num_text)
                return l
        except:
            pass 
    
    def find_s(self,text):
        try:
            try:
                a = w2n.word_to_num(text)
            except:
                try:
                    a = self.foo(text)
                except:
                    pass
            b = None 
            if "slow" in text:
                b = "slow"
            elif "advans" in text:
                b = "advans"
            elif "fast" in text:
                b = "fast"
            c = None
            if "down" in text:
                c = "d"
            elif "up" in text:
                c = "u"
            x2=[a,b,c]
            return x2
        except:
            pass
    
    def serch_only2(self,serch_text):
        try:
            serch_text = self.fix(serch_text)
            try:
                webbrowser.open(f"https://www.google.com/search?q={serch_text}")
            except:
                pass
        except:
            pass

    def serch_only(self,serch_text):
        try:
            serch_text = self.fix(self.fix(serch_text))
            try:
                webbrowser.open(f"https://www.google.com/search?q={serch_text}")
            except:
                pass
        except:
            pass

    def serch(self,x):
        try:
            search_text=self.fix(x)
            driver = webdriver.Chrome(ChromeDriverManager().install())
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
            
            time.sleep(5)
        except:
            pass

    def link(self,text):
        try:
            text = self.fix(text)
            try:
                webbrowser.open(f"https://{text}")
            except:
                pass
        except:
            pass

    def type(self,text):
        try:
            x = self.fix(text)
            for i in x: 
                pyautogui.write(i)
                time.sleep(0.07)
        except:
            pass

    def press_key2(self,keys):
        try:
            x = self.fix(self.fix(keys))
            y = x.split(' ')
            if len(y)!=1:
                try:
                    pyautogui.hotkey(*y)
                except:
                    pass
            else:
                try:
                    pyautogui.press(y)
                except:
                    pass
        except:
            pass

    def press_key(self,keys):
        try:
            x = self.fix(keys)
            y = x.split(' ')
            if len(y)!=1:
                try:
                    pyautogui.hotkey(*y)
                except:
                    pass
            else:
                try:
                    pyautogui.press(y[0])
                except:
                    pass
        except:
            pass

    def click2(self,text):
        try:
            c_t=self.fix(self.fix(text))
            a,b=self.find_number_c(c_t)
            try:
                pyautogui.click(a,b)
            except:
                pass
        except:
            pass

    def click(self,text):
        try:
            c_t=self.fix(text)
            a,b=self.find_number_c(c_t)
            if a and b:
                pyautogui.click(a,b)
            else:
                pass
        except:
            pass

    def scroll2(self,text):
        try:
            s = self.fix(self.fix(text))
            a,b,c = self.find_s(s)
            x = 1
            kind = "advans"
            u_d = "d"
            if b:
                kind = b
            if c:
                u_d = c
            if u_d == "d":
                x = -1
            if kind == "slow":
                scroll_amount = 20*x
            elif kind == "advans":
                scroll_amount = 50*x
            elif kind == "fast":
                scroll_amount = 100*x
            start_time = time.time()
            while time.time() - start_time < a:
                try:
                    pyautogui.scroll(scroll_amount)
                except:
                    pass
        except:
            pass

    def scroll(self,text):
        try:
            s = self.fix(text)
            a,b,c = self.find_s(s)
            x = 1
            kind = "advans"
            u_d = "d"
            if b:
                kind = b
            if c:
                u_d = c
            if u_d == "d":
                x = -1
            if kind == "slow":
                scroll_amount = 20*x
            elif kind == "advans":
                scroll_amount = 50*x
            elif kind == "fast":
                scroll_amount = 100*x
            start_time = time.time()
            while time.time() - start_time < a:
                try:
                    pyautogui.scroll(scroll_amount)
                except:
                    pass
        except:
            pass

    def screenshot(self):
        try:
            now = datetime.now()
            num = random.randint(100000,999999)
            date = now.strftime("%Y-%m-%d")
            username = os.getenv("USERNAME")
            screen = pyautogui.screenshot()
            screen.save(f"C:\\Users\\{username}\\OneDrive\\Pictures\\Screenshots\\Screenshot {date} {num}.png")
        except:
            pass

    def choice(self,text:str):
        x = self.check_conection()
        if not x:
            try:
                if text.startswith("search") or text.startswith("serch") :
                    self.engin.say("You are not connected to the Internet")
                    self.engin.runAndWait()
                if text.startswith("link") or text.startswith("lynch"):
                    self.engin.say("You are not connected to the Internet")
                    self.engin.runAndWait()
                if self.tt(text).startswith("type") or self.tt(text).startswith("right") or self.tt(text).startswith("hi"):
                    self.type(self.tt(text))
                if self.tt(text).startswith("police") or self.tt(text).startswith("price") or self.tt(text).startswith("press"):
                    self.press_key(self.tt(text))
                if self.tt(text).startswith("click")or self.tt(text).startswith("quick") or self.tt(text).startswith("greet") or self.tt(text).startswith("great") or self.tt(text).startswith("creek") or self.tt(text).startswith("blake") or self.tt(text).startswith("week") or self.tt(text).startswith("clique"):
                    self.click(self.tt(text))
                if self.tt(text).startswith("school") or self.tt(text).startswith("screw") or self.tt(text).startswith("scroll") or self.tt(text).startswith("is cool"):
                    if  self.tt(text).startswith("is cool") :
                        self.scroll2(self.tt(text))
                    else:
                        self.scroll(self.tt(text))
                if self.tt(text).startswith("screenshot") or self.tt(text).startswith("screen") or self.tt(text).startswith("screen shot"):
                    self.screenshot()
                else:
                    pass
            except:
                pass
        if x:
            try:
                text = self.aa(text.lower())
                if text.startswith("search") or text.startswith("serch") :
                    if self.fix(text).startswith("only") or self.fix(text).startswith("just"):
                        self.serch_only(text)
                        
                    else:
                        threading.Thread (target=self.serch(text)).start() 
                if text.startswith("link") or text.startswith("lynch"):
                    self.link(text)
                if text.startswith("type") or text.startswith("right") or text.startswith("hi"):
                    self.type(text)
                if text.startswith("police") or text.startswith("price") or text.startswith("press"):
                        self.press_key(text)
                if text.startswith("click") or text.startswith("quick") or text.startswith("greet") or text.startswith("blake") or text.startswith("kill it") or text.startswith("week") or text.startswith("create"):
                    if text.startswith("kill it"):
                        self.click2(text)
                    else:
                        self.click(text)
                if text.startswith("school") or text.startswith("screw") or text.startswith("scroll") or text.startswith("is cool"):
                    if  text.startswith("is cool") :
                        self.scroll2(text)
                    else:
                        self.scroll(text)
                if text.startswith("screenshot") or text.startswith("screen") or text.startswith("screen shot"):
                    self.screenshot()
                else:
                    pass
            except:
                pass
        

class App():
    def __init__(self):
        self.order = Order()
        self.q = queue.Queue()
        self.recognizer = sr.Recognizer()
        self.directory_name = os.path.dirname(os.path.realpath(__file__))
        ctk.set_default_color_theme(f"{self.directory_name}\MoonlitSky.json")
        self.app = ctk.CTk()
        self.image1 = Image.open(f"{self.directory_name}\\assets\mall.png")
        self.image2 = Image.open(f"{self.directory_name}\\assets\menu.png")
        self.image3 = Image.open(f"{self.directory_name}\\assets\microphon.png")
        self.image4 = Image.open(f"{self.directory_name}\\assets\log.png")
        self.image = ctk.CTkImage(Image.open(f"{self.directory_name}\\assets\microphon.png"), size=(170, 170))
        self.switch_var = ctk.StringVar(value="off")
        self.rectangle = ctk.CTkLabel(self.app, width=2000, height=1100, text="", fg_color="#000f51")
        self.bt1 = ctk.CTkButton(self.app,width=200,height=80,text="Menu",anchor="n",compound="left",image=ctk.CTkImage(dark_image=self.image2),border_color="#000044",command=lambda p=1: self.change_page(p))
        self.btn3 = ctk.CTkButton(self.app,width=200,height=80,text="login/singin",anchor="n",compound="left",image=ctk.CTkImage(dark_image = self.image4),border_color="#000044",command=lambda p=3: self.change_page(p))
        self.btn4 = ctk.CTkButton(self.app,width=200,height=80,text="Settings",anchor="n",compound="left",image=ctk.CTkImage(dark_image=self.image1),border_color="#000044",command=lambda p=4: self.change_page(p))
        self.model = vosk.Model(f"{self.directory_name}\\model")
        self.bt1.place(x=0,y=280-140+10)
        self.btn3.place(x=0,y=360-140+10)
        self.btn4.place(x=0,y=440-140+10)
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 130)
        self.app.title("speech to order")
        ctk.set_appearance_mode("Dark")
        self.gpt_text = self.random_t()
        self.qw = 0
        self.r = 1
        self.s = 1 

    def random_t(self):
        n=randint(1,20)
        x=''
        for i in range(n):
            d=chr(randint(97,122))
            x+=d
        return x
    
    def toggle_switch(self):
        if self.switch_var.get() == "off":
            self.switch_var.set("on")
        else:
            self.switch_var.set("off")

    def plus(self):
        self.qw+=1
        self.toggle_switch()

    def insert_text(self,event=None):
        x=self.text_e.get()
        self.text_e.delete(0,"end")
        if self.order.check_conection() :
            self.order.choice(x)
        else:
            self.order.choice(f'"{x}"')

    def stt_of(self):
        self.qw+=1
        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',channels=1, callback=lambda indata, frames, time, status:self.q.put(bytes(indata))):
            self.engine.say("Please speech")
            self.engine.runAndWait()
            rec = vosk.KaldiRecognizer(self.model, 16000)
            while True:
                if rec.AcceptWaveform(self.q.get()):
                    result ="".join([char for char in rec.Result()[13:] if char not in '\n}'])
                    if result.strip()!='""':
                        self.order.choice(result)
                if self.qw % 2 == 0:
                    self.engine.say("Done listening")
                    self.engine.runAndWait()
                    break
                
    def stt_on(self):
        self.qw+=1
        self.engine.say("Please speech")
        self.engine.runAndWait()
        while True:
            if self.qw%2==0: 
                    break
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                audio = recognizer.listen(source,0,4)
                try:
                    text = recognizer.recognize_google(audio,language="en-us")
                    print(text)
                    self.order.choice(text)
                except :
                    pass
    def Exchange(self):
        self.toggle_switch()
        if self.order.check_conection()==False:
            if self.qw%2==0 :
                threading.Thread (target=self.stt_of).start()
            else:
                self.plus()
        else:
            if self.qw%2==0 :
                threading.Thread (target=self.stt_on).start() 
            else:
                self.plus()

    def change_page(self,page_number):
        for widget in self.content_frame.winfo_children():
            widget.destroy() 
        if page_number == 1:
            mic = ctk.CTkButton(self.content_frame, width=200,height=300,text="",image=self.image,fg_color="#000f51",border_width=0,corner_radius=1000,command=lambda :self.Exchange())
            mic.place(x=350,y=5)
            o_f = ctk.CTkSwitch(self.content_frame,state="disabled", onvalue="on", offvalue="off", text="ON/OFF",font=("Arial",18),button_color="#3498db",button_hover_color="#3498db",switch_width=100,switch_height=40,variable=self.switch_var)
            o_f.place(x=560-20,y=300+10)
            o_f.configure(state='disabled')
        elif page_number == 3:
            label = ctk.CTkLabel(self.content_frame, text=" 😉coming soon!😊", font=("Arial", 60),compound="center",text_color="green")
            label.place(x=320,y=150)
            self.engine.say("cooming soon!")
            self.engine.runAndWait()
        elif page_number == 4:
            label_s = ctk.CTkLabel(self.content_frame, text=" 😊coming soon!😉", font=("Arial", 60),compound="center",text_color="blue")
            label_s.place(x=320,y=150)
            self.engine.say("cooming soon!")
            self.engine.runAndWait()

    def main(self):
        self.content_frame = ctk.CTkFrame(self.app, corner_radius=10, fg_color="#000f51")
        self.content_frame.pack(side="left", fill="both", expand=True,pady=148,padx=200)
        self.change_page(1)
        self.text_e = ctk.CTkEntry(self.app,placeholder_text="start typing...",width=1100,height=30)
        self.text_e.place(x=225,y=600)
        self.text_e.bind("<Return>", self.insert_text)
        self.app.mainloop()

if __name__=="__main__":
    app = App()
    try:
        app.main()
    except:
        pass
    