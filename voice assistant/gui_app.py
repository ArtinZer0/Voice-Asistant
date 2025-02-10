import customtkinter as ctk
import speech_recognition as sr
from PIL import Image 
from time import sleep
from random import randint
import vosk
import threading
import sounddevice as sd
import queue
import order

qw=0
r=1
s=1
model_path = "D:\modelll"
model = vosk.Model(model_path)
q = queue.Queue()
def toggle_switch():
    global o_f
    if o_f.get() == 0:
        o_f.configure(state="normal")
        o_f.select()
        o_f.configure(state="disabled")
        
    else:
        o_f.configure(state="normal")
        o_f.deselect()
        o_f.configure(state="disabled")
def random_t():
    n=randint(1,20)
    x=''
    for i in range(n):
        d=chr(randint(97,122))
        x+=d
    return x
def plus():
    global qw
    qw+=1
    toggle_switch()
def speech_to_text():
        global qw
        qw+=1
        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',channels=1, callback=lambda indata, frames, time, status:q.put(bytes(indata))):
            print("Please speak...")
            rec = vosk.KaldiRecognizer(model, 16000)
            toggle_switch()
            while True:
                if rec.AcceptWaveform(q.get()):
                    result ="".join([char for char in rec.Result()[13:] if char not in '\n}'])
                    if result.strip()!='""':
                        order.choice(result)
                        print(result[::-1])
                if qw%2==0: 
                    break
ctk.set_appearance_mode("Dark") 
ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("D:\coder\code\cumputer_project\MoonlitSky.json")  
app = ctk.CTk()  
image1=Image.open("D:\coder\code\cumputer_project\\assets\mall.png")
image2=Image.open("D:\coder\code\cumputer_project\\assets\menu.png")
image3=Image.open("D:\coder\code\cumputer_project\\assets\microphon.png")
image4=Image.open("D:\coder\code\cumputer_project\\assets\log.png")
image = ctk.CTkImage(Image.open("D:\coder\code\cumputer_project\\assets\microphon.png"), size=(170, 170))
image5=Image.open("D:\coder\code\cumputer_project\\assets\Back.png")
image6=Image.open("D:\coder\code\cumputer_project\\assets\chat_gpt.png")
app.title("spheech to order")
content_frame = ctk.CTkFrame(app, corner_radius=10, fg_color="#000f51")
content_frame.pack(side="left", fill="both", expand=True,pady=148,padx=200)
text_e=ctk.CTkEntry(app,placeholder_text="start typing...",width=1100,height=30)
text_e.place(x=225,y=600)


def insert_text(event=None):
    for widget in content_frame.winfo_children():
        if widget=='.!ctkframe.!ctktextbox':
            continue
        widget.destroy()
    text=ctk.CTkTextbox(content_frame,state="disabled",width=1000,height=400,fg_color="#2a4f07",text_color="#0a0f70",font=("Arial",24))
    text.place(x=100,y=20)
    global text_e
    user_input = text_e.get() 
    gpt_text=random_t()
    text_e.delete(0,"end")
    text.configure(state="normal")
    text.insert("end",f"{user_input}\n........\n")
    text.configure(state="disabled")
    sleep(3)
    text.configure(state="normal")
    text.insert("end",f"{gpt_text}\n........\n")
    text.configure(state="disabled")  
text_e.bind("<Return>", insert_text)

def change_page(page_number):
    for widget in content_frame.winfo_children():
        widget.destroy() 
    if page_number == 1:
        global o_f
        o_f = ctk.CTkSwitch(content_frame, text="ON/OFF",font=("Arial",18),button_color="#3498db",button_hover_color="#3498db",switch_width=100,switch_height=40)
        o_f.configure(state='disabled')
        o_f.place(x=560-20,y=300+10)
        # def toggle_switch():
        #     if o_f.get() == 0:
        #         o_f.select()
        #     else:
        #         o_f.deselect()
        mic = ctk.CTkButton(content_frame, width=200,height=300,text="",image=image,fg_color="#000f51",border_width=0,corner_radius=1000,command=lambda :threading.Thread (target=speech_to_text).start() if qw%2==0 else plus())
        mic.place(x=350,y=5)
    # elif page_number == 2:
    #     btn_1=ctk.CTkButton(content_frame, width=1000,height=135,text="add_order",font=("Arial",40),command=lambda : add())
    #     btn_2=ctk.CTkButton(content_frame, width=1000,height=135,text="delete_order",font=("Arial",40),command=lambda : delete())
    #     btn_3=ctk.CTkButton(content_frame, width=1000,height=135,text="help",font=("Arial",40),command=lambda : help())
    #     btn_1.place(x=100,y=50-20)
    #     btn_2.place(x=100,y=170)
    #     btn_3.place(x=100,y=250+60)
    #     def add():
    #         for widget in content_frame.winfo_children():
    #             widget.destroy()  
    #         BTN=ctk.CTkButton(content_frame,width=10,height=20,text="",anchor="n",compound="left",image=ctk.CTkImage(dark_image=image5),fg_color="#000f51",border_color="#000f51",command=lambda : change_add())
    #         BTN.place(x=2,y=2)
    #         def change_add():
    #             for widget in content_frame.winfo_children():
    #                 widget.destroy() 
    #             btn_1=ctk.CTkButton(content_frame, width=1000,height=135,text="add_order",font=("Arial",40),command=lambda : add())
    #             btn_2=ctk.CTkButton(content_frame, width=1000,height=135,text="delete_order",font=("Arial",40),command=lambda : delete())
    #             btn_3=ctk.CTkButton(content_frame, width=1000,height=135,text="help",font=("Arial",40),command=lambda : help())
    #             btn_1.place(x=100,y=50-20)
    #             btn_2.place(x=100,y=170)
    #             btn_3.place(x=100,y=250+60)
    #         entery1=ctk.CTkEntry(content_frame,width=400,height=50,text_color="#c30f0f")
    #         entery2=ctk.CTkEntry(content_frame,width=400,height=50,text_color="#c30f0f")
    #         btn_s=ctk.CTkButton(content_frame,width=400,height=50, command=lambda : save(),text="Save_Order")
    #         entery1.place(x=500-400-10,y=100)
    #         entery2.place(x=500-400-10,y=150+20)
    #         btn_s.place(x=500-400-10,y=200+40)
    #         text_b=ctk.CTkTextbox(content_frame,state="disabled",width=500,height=300,font=("Arial",18),text_color="#24c630")
    #         text_b.place(x=500,y=100)
    #         def save():
    #             global r
    #             x=entery1.get()
    #             y=entery2.get()
    #             xy=f"{r}_{x} --> {y}"
    #             r+=1
    #             text_b.configure(state="normal")
    #             text_b.insert("end", xy + "\n")
    #             text_b.configure(state="disabled")
    #             entery2.delete(0,"end")
    #             entery1.delete(0,"end")
    #     def delete():
    #         for widget in content_frame.winfo_children():
    #             widget.destroy() 
    #         BTN=ctk.CTkButton(content_frame,width=10,height=20,text="",anchor="n",compound="left",image=ctk.CTkImage(dark_image=image5),fg_color="#000f51",border_color="#000f51",command=lambda : change_add())
    #         BTN.place(x=2,y=2)
    #         def change_add():
    #             for widget in content_frame.winfo_children():
    #                 widget.destroy() 
    #             btn_1=ctk.CTkButton(content_frame, width=1000,height=135,text="add_order",font=("Arial",40),command=lambda : add())
    #             btn_2=ctk.CTkButton(content_frame, width=1000,height=135,text="delete_order",font=("Arial",40),command=lambda : delete())
    #             btn_3=ctk.CTkButton(content_frame, width=1000,height=135,text="help",font=("Arial",40),command=lambda : help())
    #             btn_1.place(x=100,y=50-20)
    #             btn_2.place(x=100,y=170)
    #             btn_3.place(x=100,y=250+60)
    #         text_b=ctk.CTkTextbox(content_frame,state="disabled",width=1000,height=300,font=("Arial",24),text_color="#24c630")  
    #         en=ctk.CTkEntry(content_frame,width=600,height=90,placeholder_text="link gogle",font=("Arial",24),text_color="#c30f0f")
    #         btn=ctk.CTkButton(content_frame,width=400,height=90,text="DELETE",font=("Arial",20))
    #         text_b.place(x=100,y=100) 
    #         en.place(x=100,y=10)
    #         btn.place(x=700,y=10)
        # def help():
        #     for widget in content_frame.winfo_children():
        #         widget.destroy() 
        #     BTN=ctk.CTkButton(content_frame,width=10,height=20,text="",anchor="n",compound="left",image=ctk.CTkImage(dark_image=image5),fg_color="#000f51",border_color="#000f51",command=lambda : change_add())
        #     BTN.place(x=2,y=2)
        #     def change_add():
        #         for widget in content_frame.winfo_children():
        #             widget.destroy() 
        #         btn_1=ctk.CTkButton(content_frame, width=1000,height=135,text="add_order",font=("Arial",40),command=lambda : add())
        #         btn_2=ctk.CTkButton(content_frame, width=1000,height=135,text="delete_order",font=("Arial",40),command=lambda : delete())
        #         btn_3=ctk.CTkButton(content_frame, width=1000,height=135,text="help",font=("Arial",40),command=lambda : help())
        #         btn_1.place(x=100,y=50-20)
        #         btn_2.place(x=100,y=170)
        #         btn_3.place(x=100,y=250+60)   
        #     en=ctk.CTkEntry(content_frame,width=400,height=100,text_color="#c30f0f",font=("Arial",20))
        #     en.place(x=90,y=100)
        #     text_b=ctk.CTkTextbox(content_frame,state="disabled",width=500,height=300,font=("Arial",24),text_color="#24c630")
        #     text_b.place(x=500,y=100)
        #     btn=ctk.CTkButton(content_frame,width=400,height=70,text="send command",command=lambda : send())
        #     btn.place(x=90,y=210)
        #     def send():
        #         en.delete(0,"end")
        #     text_b.configure(state="normal")
        #     text_b.insert("end","link --> open link \n\n type --> write with keybord \n\ntype s --> press few button \n\nclick --> click on pc with x and y \n\nopen --> open app desktop \n\nopen f --> open file with place of file \n\nscroll --> scroll from x until y \n\nfind screen --> find a object in screen & click")
        #     text_b.configure(state="disabled")
    elif page_number == 3:
        label = ctk.CTkLabel(content_frame, text=" در دست تعمیر است!!", font=("Arial", 24),compound="center")
        label.pack(pady=10,padx=45)
    elif page_number == 4:
        label = ctk.CTkLabel(content_frame, text=" در دست تعمیر است!!", font=("Arial", 24))
        label.place(x=200,y=150)
    elif page_number == 5:
        text=ctk.CTkTextbox(content_frame,state="disabled",width=1000,height=400,fg_color="#2a4f07",text_color="#0a0f70",font=("Arial",24))
        text.place(x=100,y=20)


rectangle = ctk.CTkLabel(app, width=2000, height=1100, text="", fg_color="#000f51")
bt1=ctk.CTkButton(app,width=200,height=80,text="Menu",anchor="n",compound="left",image=ctk.CTkImage(dark_image=image2),border_color="#000044",command=lambda p=1: change_page(p))
# bt2=ctk.CTkButton(app,width=200,height=80,text="Add_Order",anchor="n",compound="left",image=ctk.CTkImage(dark_image=image3),border_color="#000044",command=lambda p=2: change_page(p))
btn3=ctk.CTkButton(app,width=200,height=80,text="login/singin",anchor="n",compound="left",image=ctk.CTkImage(dark_image=image4),border_color="#000044",command=lambda p=3: change_page(p))
btn4=ctk.CTkButton(app,width=200,height=80,text="Settings",anchor="n",compound="left",image=ctk.CTkImage(dark_image=image1),border_color="#000044",command=lambda p=4: change_page(p))
btn5=ctk.CTkButton(app,width=200,height=80,text="Chat_GPT",anchor="n",compound="left",image=ctk.CTkImage(dark_image=image6),border_color="#000044",command=lambda p=5: change_page(p))
bt1.place(x=0,y=280-140+10)
# bt2.place(x=0,y=360-140+10)
btn5.place(x=0,y=360-140+10)#x=0,y=440-140+10
btn3.place(x=0,y=440-140+10)#x=0,y=500-120+10
btn4.place(x=0,y=500-120+10)#x=0,y=470

change_page(1)
app.mainloop()