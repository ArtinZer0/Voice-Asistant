from turtle import *
from PIL import Image
import os

dir=os.listdir()[0]
def image_size(x):
    img = Image.open(f"{dir}/assets/{x}.gif")
    new_size = (40, 40)
    img_resized = img.resize(new_size)
    img_resized.save(f"{x}_resized.gif")
image_size("R_W")
ss=0
o=['P_W','KN_W','B_W','Q_W','K_W','P_B','R_B','KN_B','B_B','Q_B','K_B']
ox=['R_W','Kn_W','B_W','Q_W','K_W','B_W','KN_W','R_W','P_W','P_W','P_W','P_W','P_W','P_W','P_W','P_W',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'P_B','P_B','P_B','P_B','P_B','P_B','P_B','P_B','R_B','KN_B','B_B','Q_B','K_B','B_B','KN_B','R_B']
for i in o:
    image_size(i)
screensize(100,100)
screen = Screen()
screen.register_shape("P_W_resized.gif")
screen.register_shape("R_W_resized.gif")
screen.register_shape("KN_W_resized.gif")
screen.register_shape("B_W_resized.gif")
screen.register_shape("Q_W_resized.gif")
screen.register_shape("K_W_resized.gif")
screen.register_shape("P_B_resized.gif")
screen.register_shape("R_B_resized.gif")
screen.register_shape("KN_B_resized.gif")
screen.register_shape("B_B_resized.gif")
screen.register_shape("Q_B_resized.gif")
screen.register_shape("K_B_resized.gif")

a=[]
for n in range(64):
    a.append([[(((n % 8 * 80 + 64 ) - 512)+150)/1.6,(((n // 8 * 80 ) - 512)+225)/1.6],[((((n % 8 * 80 + 64 ) - 512)+150)/1.6)+50,(((n // 8 * 80 ) - 512)+225)/1.6],[(((n % 8 * 80 + 64 ) - 512)+150)/1.6,((((n // 8 * 80 ) - 512)+225)/1.6)+50]])
def place_image(image, x, y):
    t = Turtle()
    t.shape(image)
    t.penup()
    t.goto(x, y) 
    t.pendown()
    return t
def number_to_point(n):
    x = (((n % 8 * 80 + 64 ) - 512)+150)/1.6
    y = (((n // 8 * 80 ) - 512)+225)/1.6
    return x,y
def bw(n,c):
    goto(number_to_point(n))
    pendown()
    fillcolor(c)
    begin_fill()
    for i in range(4):
        forward(50)
        left(90)
    end_fill()
    penup()
global w
def point_to_number(x, y):
    global w
    global ss
    for i in range(64):
        if x>a[i][0][0] and x<a[i][1][0] and y>a[i][0][1] and y<a[i][2][1]:
            if ss==0 :
                if ox[i]!=0 and ox[i].endswith('W'):
                    if (i//8)%2==0:
                        if i%2==0:
                            c='chocolate'
                        else:
                            c='bisque'
                    else:
                        if i%2==0:
                            c='bisque'
                        else:
                            c='chocolate'
                    bw(i,c)
                    w=ox[i]
                    ox[i]=0
                    ss+=1
                    onscreenclick(move)
            else:
                if ox[i]!=0 and ox[i].endswith('B'):
                    if (i//8)%2==0:
                        if i%2==0:
                            c='chocolate'
                        else:
                            c='bisque'
                    else:
                        if i%2==0:
                            c='bisque'
                        else:
                            c='chocolate'
                    bw(i,c)
                    w=ox[i]
                    ox[i]=0
                    ss=0
                    onscreenclick(move)
                
def move(x,y):
    for i in range(64):
        if x>a[i][0][0] and x<a[i][1][0] and y>a[i][0][1] and y<a[i][2][1]:
            place_image(f"{w}_resized.gif",((((i % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((i // 8 * 80 ) - 512)+225)/1.6)+25)
            ox[i]=w
            onscreenclick(point_to_number)

speed(0)
pensize(1)
ht()
penup()
for i in range(64):
    if (i//8)%2==0:
        if i%2==0:
            c='chocolate'
        else:
            c='bisque'
    else:
        if i%2==0:
            c='bisque'
        else:
            c='chocolate'
    bw(i,c)

place_image("R_W_resized.gif",((((0 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((0 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("KN_W_resized.gif",((((1 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((1 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("B_W_resized.gif",((((2 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((2 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("Q_W_resized.gif",((((3 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((3 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("K_W_resized.gif",((((4 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((4 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("B_W_resized.gif",((((5 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((5 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("KN_W_resized.gif",((((6 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((6 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("R_W_resized.gif",((((7 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((7 // 8 * 80 ) - 512)+225)/1.6)+25)

place_image("P_W_resized.gif",((((8 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((8 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("P_W_resized.gif",((((9 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((9 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("P_W_resized.gif",((((10 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((10 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("P_W_resized.gif",((((11 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((11 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("P_W_resized.gif",((((12 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((12 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("P_W_resized.gif",((((13 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((13 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("P_W_resized.gif",((((14 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((14 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("P_W_resized.gif",((((15 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((15 // 8 * 80 ) - 512)+225)/1.6)+25)

place_image("R_B_resized.gif",((((56 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((56 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("KN_B_resized.gif",((((57 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((57 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("B_B_resized.gif",((((58 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((58 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("Q_B_resized.gif",((((59 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((59// 8 * 80 ) - 512)+225)/1.6)+25)
place_image("K_B_resized.gif",((((60 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((60// 8 * 80 ) - 512)+225)/1.6)+25)
place_image("B_B_resized.gif",((((61 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((61// 8 * 80 ) - 512)+225)/1.6)+25)
place_image("KN_B_resized.gif",((((62 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((62// 8 * 80 ) - 512)+225)/1.6)+25)
place_image("R_B_resized.gif",((((63 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((63// 8 * 80 ) - 512)+225)/1.6)+25)

place_image("P_B_resized.gif",((((48 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((48 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("P_B_resized.gif",((((49 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((49 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("P_B_resized.gif",((((50 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((50 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("P_B_resized.gif",((((51 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((51 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("P_B_resized.gif",((((52 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((52 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("P_B_resized.gif",((((53 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((53 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("P_B_resized.gif",((((54 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((54 // 8 * 80 ) - 512)+225)/1.6)+25)
place_image("P_B_resized.gif",((((55 % 8 * 80 + 64 ) - 512)+150)/1.6)+25,((((55 // 8 * 80 ) - 512)+225)/1.6)+25)

onscreenclick(point_to_number)
mainloop()