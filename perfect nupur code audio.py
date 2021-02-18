#!/usr/bin/env python
# coding: utf-8

# In[1]:
from tkinter import*
from tkinter import messagebox
import sqlite3
# import aptitude_test
import random
# import technical_test
from tkinter import messagebox
import pyttsx3
from tkinter import *
import tkinter as tk

def tech():
    global photoimage
    test = [
        {" What is the return type of function id?": ["int",
                                                      "float",
                                                      "bool",
                                                      "dict"],
         "answer": ["int"]},
        {
            "In order to store values in terms of key and value we use what core data type.": [
                "list", "tuple", "class", "dict"],
            "answer": ["dict"]},
        {"What is the return value of trunc()?": ["int",
                                                  "bool",
                                                  "float",
                                                  "None"],
         "answer": ["int"]},
        {
            "Which of the following is performed by Data Scientist?": [
                "Define the question", "Create reproducible code", "Challenge results", "All of the mentioned"],
            "answer": ["All of the mentioned"]},
        {"Which of the following is the most important language for Data Science?": ["Java", "Ruby", "R", "None"],
         "answer": ["R"]},
        {
            "Which of the following is characteristic of Processed Data?": [
                "Data is not ready for analysis", "All steps should be noted", "Hard to use for data analysis",
                "None of the mentioned"],
            "answer": ["All steps should be noted"]},
        {
            "ML is a field of AI consisting of learning algorithms that?": [
                " Improve their performance", "At executing some task", "Over time with experience",
                "All of the above"],
            "answer": ["All of the above"]},
        {"Which of the following are ML methods?": ["based on human supervision", "supervised Learning",
                                                    "semi-reinforcement Learning", "All of the above"],
         "answer": ["All of the above"]},
        {
            ". In Model based learning methods, an iterative process takes place on the ML models that are built based on various model parameters, called ?": [
                "mini-batches", "optimizedparameters", "hyperparameters", "superparameters"],
            "answer": ["hyperparameters"]},
        {"A model of language consists of the categories which does not include _______": ["System Unit",
                                                                                           "structural units",
                                                                                           "data units",
                                                                                           "empirical units"],
         "answer": ["structural units"]},

    ]

    random.shuffle(test)
    for i in test:
        for k, v in i.items():
            random.shuffle(v)
    qn = 0
    testScorelist = []

    def tes(t):
        nonlocal qn
        nonlocal testScorelist

        t.destroy()

        top = Tk()

        # Adjusting Window Open Size

        w = 1200  # width for the Tk root
        h = 650  # height for the Tk root

        # get screen width and height
        ws = top.winfo_screenwidth()  # width of the screen
        hs = top.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        top.geometry('%dx%d+%d+%d' % (w, h, x, y))
        top.title("Aptitude Test")

        def selection(ans):
            selection = "You selected the option " + str(radio.get())
            if radio.get() == ans[0]:
                testScorelist.append(1)
            label.config(text=selection)

        radio = StringVar()

        question = list(test[qn].keys())[0]
        print(type(question), question)
        a1 = test[qn][question][0]
        a2 = test[qn][question][1]
        a3 = test[qn][question][2]
        a4 = test[qn][question][3]
        ans = test[qn]["answer"]
        print(ans)

        def playAudioInputs():
            play(question)
            play(a1)
            play(a2)
            play(a3)
            play(a4)

        lbl = Label(text=question, font=('bold italic', 15, 'bold'), wraplength=550)
        lbl.pack()
        R1 = Radiobutton(top, text=a1, font=('bold italic', 15, 'bold'), variable=radio, value=a1,
                         command=lambda: selection(ans))
        R1.pack(anchor=W)

        R2 = Radiobutton(top, text=a2, font=('bold italic', 15, 'bold'), variable=radio, value=a2,
                         command=lambda: selection(ans))
        R2.pack(anchor=W)
        R3 = Radiobutton(top, text=a3, font=('bold italic', 15, 'bold'), variable=radio, value=a3,
                         command=lambda: selection(ans))
        R3.pack(anchor=W)
        R4 = Radiobutton(top, text=a4, font=('bold italic', 15, 'bold'), variable=radio, value=a4,
                         command=lambda: selection(ans))
        R4.pack(anchor=W)

        def score(top):
            finalScore = 0
            for i in testScorelist:
                finalScore += i
            message = "Your Technical Round Score: " + str(finalScore)
            play(message)
            messagebox.showinfo("Result", message)
            top.destroy()

        if qn == len(test) - 1:

            btn_12 = Button(top, text="Play", bg="#BC0024000000", command=lambda: playAudioInputs(), fg="white",
                            width=20, activebackground='red', bd=8)
            btn_12.pack()

            b = Button(top, padx=16, pady=8, bd=10, fg="yellow",
                       font=('ariel', 16, 'bold'), width=10,
                       text="submit", bg="red", command=lambda: score(top))
            b.pack()  # grid(row=5, column=5)
        else:

            btn_12 = Button(top, text="Play", bg="#BC0024000000", command=lambda: playAudioInputs(), fg="white",
                            width=20, activebackground='red', bd=8)
            btn_12.pack()

            b = Button(top, padx=16, pady=8, bd=10, fg="yellow",
                       font=('ariel', 16, 'bold'), width=10,
                       text="next", bg="red", command=lambda: tes(top))
            b.pack()  # grid(row=5, column=5)
            qn += 1

        label = Label(top)
        label.pack()
        top.mainloop()

    def play(input):
        # btn_2= Button(top, text="Play", bg="#BC0024000000", command =play ,fg="white",width=20,activebackground='red',bd=8)
        # btn_2.grid(row=4,column=2)

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 30)
        engine.say(input)
        engine.runAndWait()


    def main():
        top = Tk()

        # Adjusting Window Open Size

        w = 1000  # width for the Tk root
        h = 400  # height for the Tk root

        # get screen width and height
        ws = top.winfo_screenwidth()  # width of the screen
        hs = top.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        top.geometry('%dx%d+%d+%d' % (w, h, x, y))

        top.title("Technical Test Window")

        photo = PhotoImage(file="Frame.png")
        photoimage = photo.subsample(3, 3)

        l1 = Label(top, font=('bold italic', 15, 'bold'),
                   text="Technical Test", fg="Black",
                   bd=10)  # label data
        l1.grid(row=1, column=2)  # label location

        b3 = Button(top, image=photo, command=lambda: tes(top))
        b3.grid(row=2, column=2)

        l2 = Label(top, padx=160, font=('bold italic', 15, 'bold'),
                   text="In this test you have given 10 questions out of which 7 should be right", fg="Black",
                   bd=10)
        l2.grid(row=3, column=2)

        l = ["In this test you have given 10 questions out of which 7 should be right"]

        btn_2 = Button(top, text="Play", bg="#BC0024000000", command=lambda: play(l[0]), fg="white", width=20,
                       activebackground='red', bd=8)
        btn_2.grid(row=4, column=2)

        top.mainloop()
    main()

photoimage = None

def aptitude(r):
    r.destroy()
    global photoimage
    test = [
        {"Two numbers are respectively 20% and 50% more than a third number. The ratio of the two numbers is:": [
            "2 : 5", "3 : 5", "4 : 5", "6 : 7"],
            "answer": ["4 : 5"]},
        {
            "A sum of money is to be distributed among A, B, C, D in the proportion of 5 : 2 : 4 : 3. If C gets Rs. 1000 more than D, what is B's share?": [
                "Rs. 500", "Rs. 1500", "Rs. 2000", "None of these"],
            "answer": ["Rs. 2000"]},
        {"Find the greatest number that will divide 43, 91 and 183 so as to leave the same remainder in each case.": [
            "4", "7", "9", "13"],
            "answer": ["4"]},
        {
            "Six bells commence tolling together and toll at intervals of 2, 4, 6, 8 10 and 12 seconds respectively. In 30 minutes, how many times do they toll together ?": [
                "4", "10", "15", "16"],
            "answer": ["16"]},
        {"The greatest number of four digits which is divisible by 15, 25, 40 and 75 is:": ["9000", "9400", "9600",
                                                                                            "9800"],
         "answer": ["9600"]},
        {
            "Let N be the greatest number that will divide 1305, 4665 and 6905, leaving the same remainder in each case. Then sum of the digits in N is:": [
                "4", "5", "6", "8"],
            "answer": ["4"]},
        {
            "The cost price of 20 articles is the same as the selling price of x articles. If the profit is 25%, then the value of x is:": [
                "15", "16", "18", "25"],
            "answer": ["16"]},
        {"A vendor bought toffees at 6 for a rupee. How many for a rupee must he sell to gain 20%?": ["3", "4", "5",
                                                                                                      "6"],
         "answer": ["5"]},
        {
            "A grocer has a sale of Rs. 6435, Rs. 6927, Rs. 6855, Rs. 7230 and Rs. 6562 for 5 consecutive months. How much sale must he have in the sixth month so that he gets an average sale of Rs. 6500?": [
                "Rs. 4991", "Rs. 5991", "Rs. 6001", "Rs. 6991"],
            "answer": ["Rs. 4991"]},
        {"The average of 20 numbers is zero. Of them, at the most, how many may be greater than zero?": ["0", "1", "10",
                                                                                                         "19"],
         "answer": ["19"]},

    ]

    # ----------------------------------------------------------------------------------------------------------------------

    # Answers=[3,3,1,4]
    # Answers=[
    #     {"Two numbers are respectively 20% and 50% more than a third number. The ratio of the two numbers is:":"4 : 5",
    #      "answer": "4 : 5"
    #      },
    #     {"A sum of money is to be distributed among A, B, C, D in the proportion of 5 : 2 : 4 : 3. If C gets Rs. 1000 more than D, what is B's share?":"Rs. 2000",
    #     "answer": "Rs. 2000"
    #      },
    #     {"Find the greatest number that will divide 43, 91 and 183 so as to leave the same remainder in each case.":"4",
    #      "answer": "4"},
    #     {"Six bells commence tolling together and toll at intervals of 2, 4, 6, 8 10 and 12 seconds respectively. In 30 minutes, how many times do they toll together ?":"16",
    #     "answer": "16"
    #      }
    # ]

    # Answers = ["4 : 5","Rs. 2000","4","16"]

    # ----------------------------------------------------------------------------------------------------------------------

    random.shuffle(test)  # shuffle Quetions

    for i in test:  # Shuffle options
        for k, v in i.items():
            random.shuffle(v)
    qn = 0
    testScorelist = []

    def tes(t):
        nonlocal qn
        nonlocal testScorelist

        t.destroy()

        top = Tk()
        top.configure(bg='#b3c9bb')
        # Adjusting Window Open Size

        w = 1200  # width for the Tk root
        h = 650  # height for the Tk root

        # get screen width and height
        ws = top.winfo_screenwidth()  # width of the screen
        hs = top.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        top.geometry('%dx%d+%d+%d' % (w, h, x, y))
        top.title("Aptitude Test")

        def selection(ans):

            selection = "You selected the option: " + str(radio.get())
            if radio.get() == ans[0]:
                testScorelist.append(1)
            label.config(text=selection)

        radio = StringVar()

        question = list(test[qn].keys())[0]
        a1 = test[qn][question][0]
        a2 = test[qn][question][1]
        a3 = test[qn][question][2]
        a4 = test[qn][question][3]
        ans = test[qn]["answer"]
        print(ans)

        def playAudioInputs():
            play(question)
            play(a1)
            play(a2)
            play(a3)
            play(a4)

        lbl = Label(text=question, font=('bold italic', 15, 'bold'), wraplength=550)
        lbl.pack()
        R1 = Radiobutton(top, text=a1, font=('bold italic', 15, 'bold'), variable=radio, value=a1,
                         command=lambda: selection(ans))
        R1.pack(anchor=W)
        R2 = Radiobutton(top, text=a2, font=('bold italic', 15, 'bold'), variable=radio, value=a2,
                         command=lambda: selection(ans))
        R2.pack(anchor=W)
        R3 = Radiobutton(top, text=a3, font=('bold italic', 15, 'bold'), variable=radio, value=a3,
                         command=lambda: selection(ans))
        R3.pack(anchor=W)
        R4 = Radiobutton(top, text=a4, font=('bold italic', 15, 'bold'), variable=radio, value=a4,
                         command=lambda: selection(ans))
        R4.pack(anchor=W)

        def score(top):
            finalScore = 0
            for i in testScorelist:
                finalScore += i
            if finalScore >= 1:
                message = "you are pass\nYour Score: " + str(finalScore)
                play(message)
                messagebox.showinfo("Result", message)
                print("you are pass")
                print("aptitude score: ", finalScore)
                print("Aptitude test is submitted")
                top.destroy()
                tech()
            else:
                print("You Are Fail")
                message = "you are Fail... :(\nYou Are Not Eligible For Next Round\nYour Score: " + str(finalScore)
                play(message)
                messagebox.showinfo("Result", message)
                top.destroy()

        if qn == len(test) - 1:

            btn_12 = Button(top, text="Play", bg="#BC0024000000", command=lambda: playAudioInputs(), fg="white",
                            width=20, activebackground='red', bd=8)
            btn_12.pack()

            b = Button(top, padx=16, pady=8, bd=10, fg="yellow",
                       font=('ariel', 16, 'bold'), width=10,
                       text="submit", bg="red", command=lambda: score(top))
            b.pack()  # grid(row=5, column=5)
        else:
            btn_12 = Button(top, text="Play", bg="#BC0024000000", command=lambda: playAudioInputs(), fg="white",
                            width=20, activebackground='red', bd=8)
            btn_12.pack()

            b = Button(top, padx=16, pady=8, bd=10, fg="yellow",
                       font=('ariel', 16, 'bold'), width=10,
                       text="next", bg="red", command=lambda: tes(top))
            b.pack()  # grid(row=5, column=5)
            qn += 1

        label = Label(top)
        label.pack()
        top.mainloop()

    def play(input):
        # btn_2= Button(top, text="Play", bg="#BC0024000000", command =play ,fg="white",width=20,activebackground='red',bd=8)
        # btn_2.grid(row=4,column=2)

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 30)
        engine.say(input)
        engine.runAndWait()

    top = Tk()

    # Adjusting Window Open Size

    w = 1000  # width for the Tk root
    h = 400  # height for the Tk root

    # get screen width and height
    ws = top.winfo_screenwidth()  # width of the screen
    hs = top.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    top.geometry('%dx%d+%d+%d' % (w, h, x, y))

    top.title("Aptitude Test Window")

    photo = PhotoImage(file="Frame.png")
    photoimage = photo.subsample(3, 3)

    l1 = Label(top, padx=160, font=('bold italic', 30, 'bold'),
               text="Aptitude Test", fg="Black",
               bd=10)
    # label data
    l1.grid(row=1, column=2)  # label location

    b3 = Button(top, image=photo, command=lambda: tes(top))
    b3.grid(row=2, column=2)
    l2 = Label(top, padx=160, font=('bold italic', 15, 'bold'),
               text="In this test you have given 10 questions out of which 7 should be right", fg="Black",
               bd=10)
    l2.grid(row=3, column=2)

    l = ["In this test you have given 10 questions out of which 7 should be right"]

    btn_2 = Button(top, text="Play", bg="#BC0024000000", command=lambda: play(l[0]), fg="white", width=20,
                   activebackground='red', bd=8)
    btn_2.grid(row=4, column=2)

    top.mainloop()


def nupur():

    con=sqlite3.connect("my.db")
    cur=con.cursor()


    main=Tk()
    main.geometry("2500x2500+0+0")
    main.title("WELCOME")
    #--------------------------------------------login-window------------------------------------------------
    def login(main):
        main.destroy()
        lg=Tk()
        lg.geometry("2500x2500+0+0")
        lg.title("WELCOME")

        #global iid,pd
        iid=StringVar()
        pd=StringVar()

        def func(lg):

            lg.destroy()

            i=iid.get()
            p=pd.get()
            #print(i)
            def view():
                cur.execute("select* from data where Username=?",(i,))
                c1=cur.fetchone()
                root1 = Tk()
                root1.geometry("2500x2500+0+0")
                root1.title("Dashboard")
                #root.geometry("890x580+0+0")
                datn = Label(root1, text="Candidate Dashboard", font=('ariel', 10, "bold"), fg="black", bd=10)
                datn.grid(row=0, column=1)
                data = Label(root1, text="User Name :", font=('ariel', 10, "italic"), fg="black", bd=10)
                data.grid(row=1, column=1)
                datau = Label(root1, text=c1[0], font=('ariel', 10, "italic"), fg="black", bd=10)
                datau.grid(row=1, column=2)
                datn = Label(root1, text="Password :", font=('ariel', 10, "italic"), fg="black", bd=10)
                datn.grid(row=2, column=1)
                datan = Label(root1, text=c1[1], font=('ariel', 10, "italic"), fg="black", bd=10)
                datan.grid(row=2, column=2)
                datn = Label(root1, text="Full Name :", font=('ariel', 10, "italic"), fg="black", bd=10)
                datn.grid(row=3, column=1)
                name=c1[2]+" " +c1[3]
                datan = Label(root1, text=name, font=('ariel', 10, "italic"), fg="black", bd=10)
                datan.grid(row=3, column=2)
                datn = Label(root1, text="Address :", font=('ariel', 10, "italic"), fg="black", bd=10)
                datn.grid(row=4, column=1)
                adrs=c1[4]+" "+c1[5]
                datan = Label(root1, text=adrs, font=('ariel', 10, "italic"), fg="black", bd=10)
                datan.grid(row=4, column=2)

                datn = Label(root1, text="Job Prefrence", font=('ariel', 10, "bold"), fg="black", bd=10)
                datn.grid(row=5, column=1)

                datn = Label(root1, text="Region :", font=('ariel', 10, "italic"), fg="black", bd=10)
                datn.grid(row=6, column=1)
                datan = Label(root1, text=c1[6], font=('ariel', 10, "italic"), fg="black", bd=10)
                datan.grid(row=6, column=2)
                datn = Label(root1, text="City :", font=('ariel', 10, "italic"), fg="black", bd=10)
                datn.grid(row=7, column=1)
                datan = Label(root1, text=c1[7], font=('ariel', 10, "italic"), fg="black", bd=10)
                datan.grid(row=7, column=2)
                datn = Label(root1, text="Experience :", font=('ariel', 10, "italic"), fg="black", bd=10)
                datn.grid(row=8, column=1)
                datan = Label(root1, text=c1[8], font=('ariel', 10, "italic"), fg="black", bd=10)
                datan.grid(row=8, column=2)
                datn = Label(root1, text="Skills :", font=('ariel', 10, "italic"), fg="black", bd=10)
                datn.grid(row=9, column=1)
                datan = Label(root1, text=c1[9], font=('ariel', 10, "italic"), fg="black", bd=10)
                datan.grid(row=9, column=2)

                datan = Label(root1, text="Ready to take assgment!!", font=('ariel', 10, "italic"), fg="black", bd=10)
                datan.grid(row=10, column=1)

                u_bttn=Button(root1,width=20,fg="black",text="Take Assignment",command=lambda :aptitude(root1))
                u_bttn.grid(row=10,column=2)

                mainloop()
            try:
                cur.execute("select password from data where Username=?",(i,))
                c=cur.fetchone()
                print(c,p)
                if(p==c[0]):
                    view()
                else:
                    lbl.config(text="Wrong ID/Password")

            except:
                lbl.config(text="Wrong ID")
                au(l1)
        def ToggleToRegister(event=None):
            signup(lg)

        userl=Label(lg,text="User Name :",font=("ariel",10,"italic"),fg="black",bd=8)
        userl.grid(row=1,column=1)
        pssl=Label(lg,text="Password :",font=('ariel',10,"italic"),fg="black",bd=10)
        pssl.grid(row=3,column=1)

        userle=Entry(lg,font=('ariel',10),textvariable=iid,fg="black",justify="left")
        userle.grid(row=1,column=4)
        pssle=Entry(lg,font=('ariel',10),textvariable=pd,fg="black",justify="left",show="*")
        pssle.grid(row=3,column=4)

        lbl=Label(lg,text="",font=("ariel",10,"bold"),fg="green")
        lbl.grid(row=6,column=4)


        u_bttn=Button(lg,width=10,fg="black",text="Login",command=lambda : func(lg))
        u_bttn.grid(row=7,column=1)
        lbl_login = Label(lg, text="Create Account!", fg="green", font=('arial', 10))
        lbl_login.grid(row=8, column=1)
        lbl_login.bind('<Button-1>', ToggleToRegister)


        lg.mainloop()
    #----------------------------------------------------------signup-window------------------------------



    def signup(main):
        main.destroy()
        root=Tk()
        root.geometry("2500x2500+0+0")
        root.title("WELCOME")

        sender_id=StringVar()
        password=StringVar()
        c_pass=StringVar()
        nme=StringVar()
        iid=StringVar()
        pd=StringVar()
        f_name=StringVar()
        l_name=StringVar()
        address=StringVar()
        city=StringVar()
        c_name=StringVar()
        cty_name=StringVar()
        experience=StringVar()
        checkvar1 = IntVar()
        checkvar2 = IntVar()
        checkvar3 = IntVar()



        con=sqlite3.connect("my.db")
        cur=con.cursor()

        skl=[]
        a_score=0
        t_score=0

        """def final():
                    cur.execute("CREATE TABLE IF NOT EXISTS  final_data (username text,country text,City text,Experience text,skill text,score text)")
                    cur.execute("INSERT INTO final_data values(?,?,?,?,?,?)",(sender_id.get(),c_name.get(),cty_name.get(),experience.get(),str(skl),score))
                    con.commit()
                    #print("final some issues here")
        """

        def save():
            try:
                cur.execute("""CREATE TABLE IF NOT EXISTS  data (Username text PRIMARY KEY,password text,firstname text NOT Null,lastname text NOT NULL,
                            adress text NOT NULL,city text NOT NULL,country text NOT NULL,cty_prefrence text NOT NULL,Experience text NOT NULL,skills text,a_score text,t_score text)""")
                cur.execute("INSERT INTO data values(?,?,?,?,?,?,?,?,?,?,?,?)",
                            (sender_id.get(),password.get(),f_name.get(),l_name.get(),address.get(),city.get(),c_name.get(),
                            cty_name.get(),experience.get(),str(skl),a_score,t_score))
                con.commit()
                sender_id.set("")
                password.set("")
                c_pass.set("")
                f_name.set("")
                l_name.set("")
                address.set("")
                city.set("")
                c_name.set("")
                cty_name.set("")
                experience.set("")
                messagebox.showinfo("showinginfo","Successfully Register! Go to home page")
            except:
                messagebox.showinfo("showinginfo","Not Register! Try again")

        def data(n,x):
            if int(x.get())==1:
                skl.append(n)
            return skl

        lbl1=Label(root,text="",font=("ariel",10,"bold"),fg="green")
        lbl1.grid(row=0,column=0)
        user=Label(root,text="User Name :",font=("ariel",10,"italic"),fg="black",bd=8)
        user.grid(row=1,column=1)
        pss=Label(root,text="Password :",font=('ariel',10,"italic"),fg="black",bd=10)
        pss.grid(row=3,column=1)
        c_pss=Label(root,text="CONFIRM Password :",font=('ariel',10,"italic"),fg="black",bd=10)
        c_pss.grid(row=4,column=1)

        lbl2=Label(root,text="Personal Infomation",font=("ariel",20,"bold"),fg="black")
        lbl2.grid(row=5,column=0)
        lbl3=Label(root,text="",font=("ariel",10,"bold"),fg="green")
        lbl3.grid(row=6,column=0)
        fullname=Label(root,text="First Name :",font=("ariel",10,"italic"),fg="black",bd=8)
        fullname.grid(row=7,column=1)
        lastname=Label(root,text="Last Name :",font=('ariel',10,"italic"),fg="black",bd=10)
        lastname.grid(row=8,column=1)
        adress=Label(root,text="Adress :",font=('ariel',10,"italic"),fg="black",bd=10)
        adress.grid(row=9,column=1)
        cty=Label(root,text="City :",font=('ariel',10,"italic"),fg="black",bd=10)
        cty.grid(row=10,column=1)

        lbl2=Label(root,text="Job Prefrence",font=("ariel",20,"bold"),fg="black")
        lbl2.grid(row=11,column=0)
        lbl1=Label(root,text="",font=("ariel",10,"bold"),fg="green")
        lbl1.grid(row=12,column=0)
        count=Label(root,text="Region you like to work in (country) :",font=("ariel",10,"italic"),fg="black",bd=8)
        count.grid(row=13,column=1)
        cityp=Label(root,text="City you prefer :",font=('ariel',10,"italic"),fg="black",bd=10)
        cityp.grid(row=14,column=1)
        exp=Label(root,text="Years of Experience(0 to 10 yrs) :",font=('ariel',10,"italic"),fg="black",bd=10)
        exp.grid(row=15,column=1)
        skills=Label(root,text="skills :",font=('ariel',10,"italic"),fg="black",bd=10)
        skills.grid(row=16,column=1)



        usere=Entry(root,font=('ariel',10),textvariable=sender_id,fg="black",justify="left")
        usere.grid(row=1,column=4)
        psse=Entry(root,font=('ariel',10),textvariable=password,fg="black",justify="left",show="*")
        psse.grid(row=3,column=4)
        c_psse=Entry(root,font=('ariel',10),textvariable=c_pass,fg="black",justify="left",show="*")
        c_psse.grid(row=4,column=4)

        fullnamee=Entry(root,font=('ariel',10),textvariable=f_name,fg="black",justify="left")
        fullnamee.grid(row=7,column=4)
        lastnamee=Entry(root,font=('ariel',10),textvariable=l_name,fg="black",justify="left")
        lastnamee.grid(row=8,column=4)
        adresse=Entry(root,font=('ariel',10),textvariable=address,fg="black",justify="left")
        adresse.grid(row=9,column=4)
        ctye=Entry(root,font=('ariel',10),textvariable=city,fg="black",justify="left")
        ctye.grid(row=10,column=4)

        counte=Entry(root,font=('ariel',10),textvariable=c_name,fg="black",justify="left")
        counte.grid(row=13,column=4)
        ctye=Entry(root,font=('ariel',10),textvariable=cty_name,fg="black",justify="left")
        ctye.grid(row=14,column=4)
        expe=Entry(root,font=('ariel',10),textvariable=experience,fg="black",justify="left")
        expe.grid(row=15,column=4)
        chkbtn1 = Checkbutton(root, text = "Python", variable = checkvar1,
                      onvalue = 1, offvalue = 0, height = 1,
                      width = 7,command=lambda :data("Python",checkvar1))
        chkbtn1.grid(row=16,column=4)
        chkbtn2 = Checkbutton(root, text = "Data science", variable = checkvar2,
                              onvalue = 1, offvalue = 0, height = 1,width = 7,
                              command=lambda :data("Data sci",checkvar2))
        chkbtn2.grid(row=17,column=4)
        chkbtn3 = Checkbutton(root, text = "ML", variable = checkvar3,
                              onvalue = 1, offvalue = 0, height = 1,width = 7,
                              command=lambda :data("ML",checkvar3))
        chkbtn3.grid(row=18,column=4)

        lbl2=Label(root,text="Review once before submitting, Data will not change after submission",font=("ariel",10),fg="Black")
        lbl2.grid(row=19,column=0)


        def log():
            si=sender_id.get()
            p=password.get()
            cp=c_pass.get()
            try:
                cur.execute("select Username from data where Username= ?",(si,))
                if(cur.fetchone() is  None):
                    print("i'm in")
                    if sender_id.get()=="":

                        lbl.config(text="Invalid Input", fg="orange")
                    else:
                        if(p==cp):
                            print(experience.get())
                            if f_name.get == "" or l_name.get() == "" or address.get() == "" or c_name.get()=="" or experience.get() == "":
                                lbl.config(text="Please complete the required field!", fg="orange")
                            else:
                                save()
                        else:
                            lbl.config(text="sorry retype your password",fg="red")
                else:
                    au(l6)
                    lbl.config(text="Username already taken",fg="red")
            except:
                if sender_id.get()=="":
                        au(l3)
                        lbl.config(text="Invalid Input!", fg="orange")

                else:
                    if(p==cp):
                        print(experience.get())
                        if f_name.get == "" or l_name.get() == "" or address.get() == "" or c_name.get()=="" or experience.get() == "":
                            au(l4)
                            lbl.config(text="Please complete the required field!", fg="orange")

                        else:
                            save()
                    else:
                        au(l5)
                        lbl.config(text="sorry retype your password",fg="red")

        def ToggleToLogin(event=None):
            #root.destroy()
            login(root)

        lbl=Label(root,text="",font=("ariel",10,"bold"),fg="green")
        lbl.grid(row=20,column=4)

        u_bttn=Button(root,width=14,fg="black",text="Final submission",command=log)
        u_bttn.grid(row=21,column=3)
        u_bttn=Button(root,width=14,fg="black",text="Play",command=lambda: au(l2))
        u_bttn.grid(row=21,column=4)
        lbl_login = Label(root, text="Already have an aaccount", fg="green", font=('arial', 10))
        lbl_login.grid(row=0, sticky=W)
        lbl_login.bind('<Button-1>', ToggleToLogin)

        root.mainloop()
        print("yoo")


    #----------------------------------Main-window------------------------------------
    def loggin():
        login(main)

    def logup():
        signup(main)

    lbl=Label(main,text="",font=("ariel",10,"bold"),fg="green")
    lbl.grid(row=0,column=0)
    u_bttn=Button(main,width=14,fg="black",text="Register",command=logup)
    u_bttn.grid(row=1,column=1)
    lbl1=Label(main,text="Or",font=("ariel",10,"bold"),fg="green")
    lbl1.grid(row=1,column=2)
    u_bttn=Button(main,width=14,fg="black",text="Sign in",command=loggin)
    u_bttn.grid(row=1,column=3)
    u_bttn=Button(main,width=14,fg="black",text="Play",command=lambda:au(l))
    u_bttn.grid(row=3,column=1)



    def au(input):
        import pyttsx3
        engine =pyttsx3.init()
        voices =engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-20)
        engine.say(input)
        engine.runAndWait()
    l="wellcome to Interview Process, please choose one option, sign in or registration"

    l1= "wrong id"
    l2="Personal infomation, Job prefrence, Review once before submitting, Data will not change after submission, Final submission"
    l3="Invalid Input"
    l4="Please complete the required field"
    l5="sorry retype your password"
    l6="Username already taken"
    main.mainloop()

nupur()





    # In[ ]:




