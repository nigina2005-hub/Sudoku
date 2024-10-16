#22222222222222222222222222222
from tkinter import *
from tkinter import ttk
import random
root1=Tk()
root1.title('Пятнашки')
root1.iconbitmap(default='iconca.ico')
root1.geometry('1350x800')
root1['bg']='pink'
python_logo=PhotoImage(file='play.png')
lb=ttk.Label(image=python_logo)
lb.place(x=500,y=200)
def p2():
    #root.destroy()
    root1.destroy()
bt1 = Button(root1, text='Выйти', command=p2, bg="cyan", font=("Times New Roman", 13, 'bold'), width=15, height=2)
bt1.place(x=1150, y=220)
label = Label(root1, text="ПЯТНАШКИ", fg='blue', font=("Times New Roman", 30, 'bold'))
label.place(x=525, y=100)
def p1():
    global al1,b1,al2,b2,al3,b3,al4,b4,al5,b5,al6,b6,al7,b7,al8,b8,al9,b9,al10,b10,al11,b11,al12,b12,al13,b13,al14,b14,al15,b15,dx,dy,r,q
    root1.withdraw()
    #root.deiconify()
    root=Tk()
    root.title('Пятнашки')
    root.iconbitmap(default='iconca.ico')
    root.geometry('1350x800')
    root['bg'] = 'pink'
    canvas = Canvas(root,bg="white", width=290, height=330)
    canvas.place(x=150,y=90)
    '''canvas = Canvas(root,bg="white", width=400, height=400)
    canvas.pack(anchor=CENTER, expand=1)'''
    '''from tkinter import messagebox
    import random
    def no():
        messagebox.showinfo(' ','Спасибо за ...')
    def motionMouse(event):
        btnYes.place(x=random.randint(0,500),y=random.randint(0,500))
    label=Label(root,text='Вы хотите выйти',font=("Arial",13,'bold'),bg='white').pack()
    btnYes=Button(root,text='Да',font=('Arial 13 bold'))
    btnYes.place(x=330,y=100)
    btnYes.bind('<Enter>',motionMouse)
    btnNo=Button(root,text='Нет',font='Arial 13 bold',command=no).place(x=350,y=100) #этот код создает избегающую кнопку'''
    '''def on_close():
        if messagebox.askokcancel('Выход из приложения','Хотите выйти из приложения?'):
            root.destroy() этот код спрашшивает выйти или нет'''
    al1=160;b1=100
    al2=230;b2=100
    al3=300;b3=100
    al4=370;b4=100
    al5=160;b5=180
    al6=230;b6=180
    al7=300;b7=180
    al8=370;b8=180
    al9=160;b9=260
    al10=230;b10=260
    al11=300;b11=260
    al12=370;b12=260
    al13=160;b13=340
    al14=230;b14=340
    al15=300;b15=340
    #370 and 340
    dx=370
    dy=340
    #l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    l=[]
    k=0
    while len(l)<15:
        k = random.randint(1, 15)
        if k not in l:
            l.append(k)
    q=0
    def x():
        global q
        q+=1
        label['text']=f'Ходов {q}'

    label = Label(root, text="Ходов", fg='red', font=("Times New Roman", 20, 'bold'))
    label.place(x=500, y=600)
    def a1():
        global dx,dy,al1,b1
        if dx == al1 + 70 and dy == b1 or dx == al1 and dy == b1 + 80 or dx==al1-70 and dy==b1 or dx==al1 and dy==b1-80:
            btn1.place(x=dx, y=dy)
            al1=al1+dx
            dx=al1-dx
            al1=al1-dx

            b1=b1+dy
            dy=b1-dy
            b1=b1-dy
            x()

    def a2():
        global dx,dy,al2,b2
        if dx == al2 + 70 and dy == b2 or dx == al2 and dy == b2 + 80 or dx==al2-70 and dy==b2 or dx==al2 and dy==b2-80:
            btn2.place(x=dx, y=dy)
            al2=al2+dx
            dx=al2-dx
            al2=al2-dx

            b2=b2+dy
            dy=b2-dy
            b2=b2-dy
            x()
    def a3():
        global dx,dy,al3,b3
        if dx == al3 + 70 and dy == b3 or dx == al3 and dy == b3 + 80 or dx==al3-70 and dy==b3 or dx==al3 and dy==b3-80:
            btn3.place(x=dx, y=dy)
            al3=al3+dx
            dx=al3-dx
            al3=al3-dx

            b3=b3+dy
            dy=b3-dy
            b3=b3-dy
            x()
    def a4():
        global dx,dy,al4,b4
        if dx == al4 + 70 and dy == b4 or dx == al4 and dy == b4 + 80 or dx==al4-70 and dy==b4 or dx==al4 and dy==b4-80:
            btn4.place(x=dx, y=dy)
            al4=al4+dx
            dx=al4-dx
            al4=al4-dx

            b4=b4+dy
            dy=b4-dy
            b4=b4-dy
            x()
    def a5():
        global dx,dy,al5,b5
        if dx == al5 + 70 and dy == b5 or dx == al5 and dy == b5 + 80 or dx==al5-70 and dy==b5 or dx==al5 and dy==b5-80:
            btn5.place(x=dx, y=dy)
            al5=al5+dx
            dx=al5-dx
            al5=al5-dx

            b5=b5+dy
            dy=b5-dy
            b5=b5-dy
            x()
    def a6():
        global dx,dy,al6,b6
        if dx == al6 + 70 and dy == b6 or dx == al6 and dy == b6 + 80 or dx==al6-70 and dy==b6 or dx==al6 and dy==b6-80:
            btn6.place(x=dx, y=dy)
            al6=al6+dx
            dx=al6-dx
            al6=al6-dx

            b6=b6+dy
            dy=b6-dy
            b6=b6-dy
            x()
    def a7():
        global dx,dy,al7,b7
        if dx == al7 + 70 and dy == b7 or dx == al7 and dy == b7 + 80 or dx==al7-70 and dy==b7 or dx==al7 and dy==b7-80:
            btn7.place(x=dx, y=dy)
            al7=al7+dx
            dx=al7-dx
            al7=al7-dx

            b7=b7+dy
            dy=b7-dy
            b7=b7-dy
            x()
    def a8():
        global dx,dy,al8,b8
        if dx == al8 + 70 and dy == b8 or dx == al8 and dy == b8 + 80 or dx==al8-70 and dy==b8 or dx==al8 and dy==b8-80:
            btn8.place(x=dx, y=dy)
            al8=al8+dx
            dx=al8-dx
            al8=al8-dx

            b8=b8+dy
            dy=b8-dy
            b8=b8-dy
            x()
    def a9():
        global dx,dy,al9,b9
        if dx == al9 + 70 and dy == b9 or dx == al9 and dy == b9 + 80 or dx==al9-70 and dy==b9 or dx==al9 and dy==b9-80:
            btn9.place(x=dx, y=dy)
            al9=al9+dx
            dx=al9-dx
            al9=al9-dx

            b9=b9+dy
            dy=b9-dy
            b9=b9-dy
            x()
    def a10():
        global dx,dy,al10,b10
        if dx == al10 + 70 and dy == b10 or dx == al10 and dy == b10 + 80 or dx==al10-70 and dy==b10 or dx==al10 and dy==b10-80:
            btn10.place(x=dx, y=dy)
            al10=al10+dx
            dx=al10-dx
            al10=al10-dx

            b10=b10+dy
            dy=b10-dy
            b10=b10-dy
            x()
    def a11():
        global dx,dy,al11,b11
        if dx == al11 + 70 and dy == b11 or dx == al11 and dy == b11 + 80 or dx==al11-70 and dy==b11 or dx==al11 and dy==b11-80:
            btn11.place(x=dx, y=dy)
            al11=al11+dx
            dx=al11-dx
            al11=al11-dx

            b11=b11+dy
            dy=b11-dy
            b11=b11-dy
            x()
    def a12():
        global dx,dy,al12,b12
        if dx == al12 + 70 and dy == b12 or dx == al12 and dy == b12 + 80 or dx==al12-70 and dy==b12 or dx==al12 and dy==b12-80:
            btn12.place(x=dx, y=dy)
            al12=al12+dx
            dx=al12-dx
            al12=al12-dx

            b12=b12+dy
            dy=b12-dy
            b12=b12-dy
            x()
    def a13():
        global dx,dy,al13,b13
        if dx == al13 + 70 and dy == b13 or dx == al13 and dy == b13 + 80 or dx==al13-70 and dy==b13 or dx==al13 and dy==b13-80:
            btn13.place(x=dx, y=dy)
            al13=al13+dx
            dx=al13-dx
            al13=al13-dx

            b13=b13+dy
            dy=b13-dy
            b13=b13-dy
            x()
    def a14():
        global dx,dy,al14,b14
        if dx == al14 + 70 and dy == b14 or dx == al14 and dy == b14 + 80 or dx==al14-70 and dy==b14 or dx==al14 and dy==b14-80:
            btn14.place(x=dx, y=dy)
            al14=al14+dx
            dx=al14-dx
            al14=al14-dx

            b14=b14+dy
            dy=b14-dy
            b14=b14-dy
            x()
    def a15():
        global dx,dy,al15,b15
        if dx == al15 + 70 and dy == b15 or dx == al15 and dy == b15 + 80 or dx==al15-70 and dy==b15 or dx==al15 and dy==b15-80:
            btn15.place(x=dx, y=dy)
            al15=al15+dx
            dx=al15-dx
            al15=al15-dx

            b15=b15+dy
            dy=b15-dy
            b15=b15-dy
            x()
    btn1=Button(root,text=str(l[0]),command=a1,bg="cyan",font=("Times New Roman",13,'bold'),width=5,height=3)
    btn1.place(x=160,y=100)
    #btnId1 = canvas.create_window(60, 40, window=btn1, width=100, height=50)
    btn2=Button(root,text=str(l[1]),command=a2,bg="cyan",font=("Times New Roman",13,'bold'),width=5,height=3)
    btn2.place(x=230,y=100)
    #btnId2 = canvas.create_window(170, 40, window=btn2, width=100, height=50)
    btn3=Button(root,text=str(l[2]),command=a3,bg="cyan",font=("Times New Roman",13,'bold'),width=5,height=3)
    btn3.place(x=300,y=100)
    btn4=Button(root,text=str(l[3]),command=a4,bg="cyan",font=("Times New Roman",13,'bold'),width=5,height=3)
    btn4.place(x=370,y=100)
    btn5=Button(root,text=str(l[4]),command=a5,bg="cyan",font=("Times New Roman",13,'bold'),width=5,height=3)
    btn5.place(x=160,y=180)
    btn6=Button(root,text=str(l[5]),command=a6,bg="cyan",font=("Times New Roman",13,'bold'),width=5,height=3)
    btn6.place(x=230,y=180)
    btn7=Button(root,text=str(l[6]),command=a7,bg="cyan",font=("Times New Roman",13,'bold'),width=5,height=3)
    btn7.place(x=300,y=180)
    btn8=Button(root,text=str(l[7]),command=a8,bg="cyan",font=("Times New Roman",13,'bold'),width=5,height=3)
    btn8.place(x=370,y=180)
    btn9=Button(root,text=str(l[8]),command=a9,bg="cyan",font=("Times New Roman",13,'bold'),width=5,height=3)
    btn9.place(x=160,y=260)
    btn10=Button(root,text=str(l[9]),command=a10,bg="cyan",font=("Times New Roman",13,'bold'),width=5,height=3)
    btn10.place(x=230,y=260)
    btn11=Button(root,text=str(l[10]),command=a11,bg="cyan",font=("Times New Roman",13,'bold'),width=5,height=3)
    btn11.place(x=300,y=260)
    btn12=Button(root,text=str(l[11]),command=a12,bg="cyan",font=("Times New Roman",13,'bold'),width=5,height=3)
    btn12.place(x=370,y=260)
    btn13=Button(root,text=str(l[12]),command=a13,bg="cyan",font=("Times New Roman",13,'bold'),width=5,height=3)
    btn13.place(x=160,y=340)
    btn14=Button(root,text=str(l[13]),command=a14,bg="cyan",font=("Times New Roman",13,'bold'),width=5,height=3)
    btn14.place(x=230,y=340)
    btn15=Button(root,text=str(l[14]),command=a15,bg="cyan",font=("Times New Roman",13,'bold'),width=5,height=3)
    btn15.place(x=300,y=340)
    r=0
    def p():
        global r
        d = l.index(1)
        s = 'btn' + str(d + 1)
        if s=='btn1' and al1==160 and b1==100 or s=='btn2' and al2==160 and b2==100 or s=='btn3' and al3==160 and b3==100 or s=='btn4' and al4==160 and b4==100 or s=='btn5' and al5==160 and b5==100 or s=='btn6' and al6==160 and b6==100 or s=='btn7' and al7==160 and b7==100 or s=='btn8' and al8==160 and b8==100 or s=='btn9' and al9==160 and b9==100 or s=='btn10' and al10==160 and b10==100 or s=='btn11' and al11==160 and b11==100 or s=='btn12' and al12==160 and b12==100 or s=='btn13' and al13==160 and b13==100 or s=='btn14' and al14==160 and b14==100 or s=='btn15' and al15==160 and b15==100:
            r+=1
        d = l.index(2)
        s = 'btn' + str(d + 1)
        if s=='btn1' and al1==230 and b1==100 or s=='btn2' and al2==230 and b2==100 or s=='btn3' and al3==230 and b3==100 or s=='btn4' and al4==230 and b4==100 or s=='btn5' and al5==230 and b5==100 or s=='btn6' and al6==230 and b6==100 or s=='btn7' and al7==230 and b7==100 or s=='btn8' and al8==230 and b8==100 or s=='btn9' and al9==230 and b9==100 or s=='btn10' and al10==230 and b10==100 or s=='btn11' and al11==230 and b11==100 or s=='btn12' and al12==230 and b12==100 or s=='btn13' and al13==230 and b13==100 or s=='btn14' and al14==230 and b14==100 or s=='btn15' and al15==230 and b15==100:
            r+=1
        d = l.index(3)
        s = 'btn' + str(d + 1)
        if s=='btn1' and al1==300 and b1==100 or s=='btn2' and al2==300 and b2==100 or s=='btn3' and al3==300 and b3==100 or s=='btn4' and al4==300 and b4==100 or s=='btn5' and al5==300 and b5==100 or s=='btn6' and al6==300 and b6==100 or s=='btn7' and al7==300 and b7==100 or s=='btn8' and al8==300 and b8==100 or s=='btn9' and al9==300 and b9==100 or s=='btn10' and al10==300 and b10==100 or s=='btn11' and al11==300 and b11==100 or s=='btn12' and al12==300 and b12==100 or s=='btn13' and al13==300 and b13==100 or s=='btn14' and al14==300 and b14==100 or s=='btn15' and al15==300 and b15==100:
            r+=1
        d = l.index(4)
        s = 'btn' + str(d + 1)
        if s=='btn1' and al1==370 and b1==100 or s=='btn2' and al2==370 and b2==100 or s=='btn3' and al3==370 and b3==100 or s=='btn4' and al4==370 and b4==100 or s=='btn5' and al5==370 and b5==100 or s=='btn6' and al6==370 and b6==100 or s=='btn7' and al7==370 and b7==100 or s=='btn8' and al8==370 and b8==100 or s=='btn9' and al9==370 and b9==100 or s=='btn10' and al10==370 and b10==100 or s=='btn11' and al11==370 and b11==100 or s=='btn12' and al12==370 and b12==100 or s=='btn13' and al13==370 and b13==100 or s=='btn14' and al14==370 and b14==100 or s=='btn15' and al15==370 and b15==100:
            r+=1
        d = l.index(5)
        s = 'btn' + str(d + 1)
        if s=='btn1' and al1==160 and b1==180 or s=='btn2' and al2==160 and b2==180 or s=='btn3' and al3==160 and b3==180 or s=='btn4' and al4==160 and b4==180 or s=='btn5' and al5==160 and b5==180 or s=='btn6' and al6==160 and b6==180 or s=='btn7' and al7==160 and b7==180 or s=='btn8' and al8==160 and b8==180 or s=='btn9' and al9==160 and b9==180 or s=='btn10' and al10==160 and b10==180 or s=='btn11' and al11==160 and b11==180 or s=='btn12' and al12==160 and b12==180 or s=='btn13' and al13==160 and b13==180 or s=='btn14' and al14==160 and b14==180 or s=='btn15' and al15==160 and b15==180:
            r+=1
        d = l.index(6)
        s = 'btn' + str(d + 1)
        if s=='btn1' and al1==230 and b1==180 or s=='btn2' and al2==230 and b2==180 or s=='btn3' and al3==230 and b3==180 or s=='btn4' and al4==230 and b4==180 or s=='btn5' and al5==230 and b5==180 or s=='btn6' and al6==230 and b6==180 or s=='btn7' and al7==230 and b7==180 or s=='btn8' and al8==230 and b8==180 or s=='btn9' and al9==230 and b9==180 or s=='btn10' and al10==230 and b10==180 or s=='btn11' and al11==230 and b11==180 or s=='btn12' and al12==230 and b12==180 or s=='btn13' and al13==230 and b13==180 or s=='btn14' and al14==230 and b14==180 or s=='btn15' and al15==230 and b15==180:
            r+=1
        d = l.index(7)
        s = 'btn' + str(d + 1)
        if s=='btn1' and al1==300 and b1==180 or s=='btn2' and al2==300 and b2==180 or s=='btn3' and al3==300 and b3==180 or s=='btn4' and al4==300 and b4==180 or s=='btn5' and al5==300 and b5==180 or s=='btn6' and al6==300 and b6==180 or s=='btn7' and al7==300 and b7==180 or s=='btn8' and al8==300 and b8==180 or s=='btn9' and al9==300 and b9==180 or s=='btn10' and al10==300 and b10==180 or s=='btn11' and al11==300 and b11==180 or s=='btn12' and al12==300 and b12==180 or s=='btn13' and al13==300 and b13==180 or s=='btn14' and al14==300 and b14==180 or s=='btn15' and al15==300 and b15==180:
            r+=1
        d = l.index(8)
        s = 'btn' + str(d + 1)
        if s=='btn1' and al1==370 and b1==180 or s=='btn2' and al2==370 and b2==180 or s=='btn3' and al3==370 and b3==180 or s=='btn4' and al4==370 and b4==180 or s=='btn5' and al5==370 and b5==180 or s=='btn6' and al6==370 and b6==180 or s=='btn7' and al7==370 and b7==180 or s=='btn8' and al8==370 and b8==180 or s=='btn9' and al9==370 and b9==180 or s=='btn10' and al10==370 and b10==180 or s=='btn11' and al11==370 and b11==180 or s=='btn12' and al12==370 and b12==180 or s=='btn13' and al13==370 and b13==180 or s=='btn14' and al14==370 and b14==180 or s=='btn15' and al15==370 and b15==180:
            r+=1
        d = l.index(9)
        s = 'btn' + str(d + 1)
        if s=='btn1' and al1==160 and b1==260 or s=='btn2' and al2==160 and b2==260 or s=='btn3' and al3==160 and b3==260 or s=='btn4' and al4==160 and b4==260 or s=='btn5' and al5==160 and b5==260 or s=='btn6' and al6==160 and b6==260 or s=='btn7' and al7==160 and b7==260 or s=='btn8' and al8==160 and b8==260 or s=='btn9' and al9==160 and b9==260 or s=='btn10' and al10==160 and b10==260 or s=='btn11' and al11==160 and b11==260 or s=='btn12' and al12==160 and b12==260 or s=='btn13' and al13==160 and b13==260 or s=='btn14' and al14==160 and b14==260 or s=='btn15' and al15==160 and b15==260:
            r+=1
        d = l.index(10)
        s = 'btn' + str(d + 1)
        if s=='btn1' and al1==230 and b1==260 or s=='btn2' and al2==230 and b2==260 or s=='btn3' and al3==230 and b3==260 or s=='btn4' and al4==230 and b4==260 or s=='btn5' and al5==230 and b5==260 or s=='btn6' and al6==230 and b6==260 or s=='btn7' and al7==230 and b7==260 or s=='btn8' and al8==230 and b8==260 or s=='btn9' and al9==230 and b9==260 or s=='btn10' and al10==230 and b10==260 or s=='btn11' and al11==230 and b11==260 or s=='btn12' and al12==230 and b12==260 or s=='btn13' and al13==230 and b13==260 or s=='btn14' and al14==230 and b14==260 or s=='btn15' and al15==230 and b15==260:
            r+=1
        d = l.index(11)
        s = 'btn' + str(d + 1)
        if s=='btn1' and al1==300 and b1==260 or s=='btn2' and al2==300 and b2==260 or s=='btn3' and al3==300 and b3==260 or s=='btn4' and al4==300 and b4==260 or s=='btn5' and al5==300 and b5==260 or s=='btn6' and al6==300 and b6==260 or s=='btn7' and al7==300 and b7==260 or s=='btn8' and al8==300 and b8==260 or s=='btn9' and al9==300 and b9==260 or s=='btn10' and al10==300 and b10==260 or s=='btn11' and al11==300 and b11==260 or s=='btn12' and al12==300 and b12==260 or s=='btn13' and al13==300 and b13==260 or s=='btn14' and al14==300 and b14==260 or s=='btn15' and al15==300 and b15==260:
            r+=1
        d = l.index(12)
        s = 'btn' + str(d + 1)
        if s=='btn1' and al1==370 and b1==260 or s=='btn2' and al2==370 and b2==260 or s=='btn3' and al3==370 and b3==260 or s=='btn4' and al4==370 and b4==260 or s=='btn5' and al5==370 and b5==260 or s=='btn6' and al6==370 and b6==260 or s=='btn7' and al7==370 and b7==260 or s=='btn8' and al8==370 and b8==260 or s=='btn9' and al9==370 and b9==260 or s=='btn10' and al10==370 and b10==260 or s=='btn11' and al11==370 and b11==260 or s=='btn12' and al12==370 and b12==260 or s=='btn13' and al13==370 and b13==260 or s=='btn14' and al14==370 and b14==260 or s=='btn15' and al15==370 and b15==260:
            r+=1
        d = l.index(13)
        s = 'btn' + str(d + 1)
        if s=='btn1' and al1==160 and b1==340 or s=='btn2' and al2==160 and b2==340 or s=='btn3' and al3==160 and b3==340 or s=='btn4' and al4==160 and b4==340 or s=='btn5' and al5==160 and b5==340 or s=='btn6' and al6==160 and b6==340 or s=='btn7' and al7==160 and b7==340 or s=='btn8' and al8==160 and b8==340 or s=='btn9' and al9==160 and b9==340 or s=='btn10' and al10==160 and b10==340 or s=='btn11' and al11==160 and b11==340 or s=='btn12' and al12==160 and b12==340 or s=='btn13' and al13==160 and b13==340 or s=='btn14' and al14==160 and b14==340 or s=='btn15' and al15==160 and b15==340:
            r+=1
        d = l.index(14)
        s = 'btn' + str(d + 1)
        if s=='btn1' and al1==230 and b1==340 or s=='btn2' and al2==230 and b2==340 or s=='btn3' and al3==230 and b3==340 or s=='btn4' and al4==230 and b4==340 or s=='btn5' and al5==230 and b5==340 or s=='btn6' and al6==230 and b6==340 or s=='btn7' and al7==230 and b7==340 or s=='btn8' and al8==230 and b8==340 or s=='btn9' and al9==230 and b9==340 or s=='btn10' and al10==230 and b10==340 or s=='btn11' and al11==230 and b11==340 or s=='btn12' and al12==230 and b12==340 or s=='btn13' and al13==230 and b13==340 or s=='btn14' and al14==230 and b14==340 or s=='btn15' and al15==230 and b15==340:
            r+=1
        d = l.index(15)
        s = 'btn' + str(d + 1)
        if s=='btn1' and al1==300 and b1==340 or s=='btn2' and al2==300 and b2==340 or s=='btn3' and al3==300 and b3==340 or s=='btn4' and al4==300 and b4==340 or s=='btn5' and al5==300 and b5==340 or s=='btn6' and al6==300 and b6==340 or s=='btn7' and al7==300 and b7==340 or s=='btn8' and al8==300 and b8==340 or s=='btn9' and al9==300 and b9==340 or s=='btn10' and al10==300 and b10==340 or s=='btn11' and al11==300 and b11==340 or s=='btn12' and al12==300 and b12==340 or s=='btn13' and al13==300 and b13==340 or s=='btn14' and al14==300 and b14==340 or s=='btn15' and al15==300 and b15==340:
            r+=1
        if r==15:
            label = Label(root, text="Вы отлично справились!", fg='green', font=("Times New Roman", 20,'bold'))
            label.place(x=500, y=500)
            btn1['bg']='green'
            btn2['bg'] = 'green'
            btn3['bg'] = 'green'
            btn4['bg'] = 'green'
            btn5['bg'] = 'green'
            btn6['bg'] = 'green'
            btn7['bg'] = 'green'
            btn8['bg'] = 'green'
            btn9['bg'] = 'green'
            btn10['bg'] = 'green'
            btn11['bg'] = 'green'
            btn12['bg'] = 'green'
            btn13['bg'] = 'green'
            btn14['bg'] = 'green'
            btn15['bg'] = 'green'
    def k1():
        root.destroy()
        p1()
    def k2():
        root.destroy()
        root1.destroy()
    btn=Button(root,text='Проверка!',command=p,bg="red",font=("Times New Roman",13,'bold'),width=15,height=2)
    btn.place(x=1150,y=100)
    bt=Button(root,text='Начать заново',command=k1,bg="cyan",font=("Times New Roman",13,'bold'),width=15,height=2)
    bt.place(x=1150,y=160)
    bt1=Button(root,text='Выйти',command=k2,bg="cyan",font=("Times New Roman",13,'bold'),width=15,height=2)
    bt1.place(x=1150,y=220)
    root.mainloop()
n=Button(root1,text='Начать игру',command=p1,bg="cyan",font=("Times New Roman",13,'bold'),width=15,height=2)
n.place(x=1150,y=160)
root1.mainloop()

