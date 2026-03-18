from tkinter import*
from tkinter import messagebox
from mydb import Database
from myapi import Api

class NLPApp:
    def __init__(self):

        self.dbo = Database()
        self.api = Api()
        self.root = Tk()
        self.root.title("NLPApp")
        self.root.iconbitmap(r'D:\SACHIN RAWAL FILES\LAPTOP\GIT DEMO\NLPAPP\Resource\appIcon.png')
        self.root.geometry('400x600')
        self.root.configure(bg='#ab9f9d')
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()

        heading = Label(self.root,text="NLPApp",bg='#bc6c25',fg='#c4e2ed')
        heading.configure(font=('verdana',18,'bold'))
        heading.pack(pady=(30,30))

        label1 = Label(self.root,text="Enter Email",bg='#bc6c25')
        label1.configure(font=('verdana',12,'bold'))
        label1.pack(pady=(10,10))


        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(10,10),ipady=4)

        label2 = Label(self.root,text="Enter Password",bg='#bc6c25')
        label2.configure(font=('verdana',12,'bold'))
        label2.pack(pady=(10,10))


        self.password_input = Entry(self.root,width=50,show="*")
        self.password_input.pack(pady=(10,10),ipady=4)

        login_btn = Button(self.root,text="Login",width=40,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root,text='Not a Member?',bg='#bc6c25',width=40)
        label3.pack(pady=(10,10))
        label3.configure(font=('verdana',12,'bold'))
        
        redirect_button = Button(self.root,text='Register Now',width=40,height=2,command=self.register_gui)
        redirect_button.pack(pady=(10,10))
    def register_gui(self):
        self.clear()
        
        heading = Label(self.root,text="NLPApp",bg='#bc6c25',fg='#c4e2ed')
        heading.configure(font=('verdana',18,'bold'))
        heading.pack(pady=(30,30))

        label0 = Label(self.root,text="Enter Your Name ",height=1,bg='#bc6c25')
        label0.configure(font=('verdana',12,'bold'))
        label0.pack(pady=(10,10))

        self.name_input =Entry(self.root,width=40)
        self.name_input.pack(pady=(10,10),ipady=4)

        label1 = Label(self.root,text='Enter your email',height=1,bg='#bc6c25')
        label1.configure(font=('vardana',12,'bold'))
        label1.pack(pady=(10,10)) 

        self.input_email = Entry(self.root,width=40)
        self.input_email.pack(pady=(10,10),ipady=4)

        label2 = Label(self.root,text='Enter your Password',height=1,bg='#bc6c25')
        label2.configure(font=('vardana',12,'bold'))
        label2.pack(pady=(10,10)) 

        self.input_passward = Entry(self.root,width=40)
        self.input_passward.pack(pady=(10,10),ipady=4)

        register_button = Button(self.root,text="Register",width=30,height=2,command=self.perform_registration)
        register_button.pack(pady=(10,10))

        label4 = Label(self.root,text='Already a Member?',height=2,bg='#bc6c25')
        label4.configure(font=('vardara',12,'bold'))
        label4.pack(pady=(10,10))

        redirect_button = Button(self.root,text="Login Now",width=30,height=2,command=self.login_gui)
        redirect_button.pack(pady=(10,10))


    def perform_registration(self):
        name = self.name_input.get()
        email = self.input_email.get()
        password = self.input_passward.get()

        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success','Registration Succesfull. You can registar now !')
        else:
            messagebox.showerror('Error','Email already existed.......')


    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo("Succes","Login Succesfull")
            self.home_gui()
        else:
            messagebox.showerror("Error","Invalid Email/Passowrd")

    def home_gui(self):
        self.clear()

        heading = Label(self.root,text="NLPApp",bg='#bc6c25',fg='#c4e2ed')
        heading.configure(font=('verdana',18,'bold'))
        heading.pack(pady=(30,30))

        sentiment_btn = Button(self.root,text='Sentiment Analysis',width=30,height=4,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))

        ner_btn = Button(self.root,text='Named Entity Recognigation',width=30,height=4,command=self.ner_gui)
        ner_btn.pack(pady=(10,10))

        emotion_btn = Button(self.root,text='Emotion Prediction',width=30,height=4,command=self.emotion_gui)
        emotion_btn.pack(pady=(10,10))

        logout_button = Button(self.root,text="Login out",width=20,height=2,command=self.login_gui)
        logout_button.pack(pady=(10,10),padx=(5,10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root,text="NLPApp",bg='#bc6c25',fg='#c4e2ed')
        heading.configure(font=('verdana',18,'bold'))
        heading.pack(pady=(30,30))

        heading = Label(self.root,text="Sentiment Analysis",bg='#bc6c25',fg='#c4e2ed')
        heading.configure(font=('verdana',15))
        heading.pack(pady=(10,20))

        label1 = Label(self.root,text='Enter the Text : ',bg='#bc6c25')
        label1.pack(pady=(10,10))

        self.sentiment_input = Text(self.root,width=40,height=6)
        self.sentiment_input.pack(pady=(10,10))   

        Analysis_btn = Button(self.root,text='Analysis Sentiment',width=30,height=2,command=self.do_sentiment_analysis)
        Analysis_btn.pack(pady=(10,10))

        self.sentiment_result = Label(self.root,text="",bg='#bc6c25',width=40,height=3,font=('vardana',15,'bold'))
        self.sentiment_result.pack(pady=(10,10))


        go_back_btn = Button(self.root,text='Go Back',width=30,height=2,command=self.home_gui)
        go_back_btn.pack(pady=(10.10))


    def do_sentiment_analysis(self):
        text = self.sentiment_input.get("1.0", "end-1c")
        result = self.api.sentiment_analysis(text)
        self.sentiment_result['text'] = result

    def emotion_gui(self):
        self.clear()
        
        heading = Label(self.root,text="NLPApp",bg='#bc6c25',fg='#c4e2ed')
        heading.configure(font=('verdana',18,'bold'))
        heading.pack(pady=(30,30))

        heading = Label(self.root,text="Sentiment Analysis",bg='#bc6c25',fg='#c4e2ed')
        heading.configure(font=('verdana',15))
        heading.pack(pady=(10,20))
        
        label1 = Label(self.root,text='Enter the Text : ',bg='#bc6c25')
        label1.pack(pady=(10,10))
        
        self.emotion_input = Text(self.root,width=40,height=6)
        self.emotion_input.pack(pady=(10,10))   

        Analysis_btn = Button(self.root,text='Analysis Emotion',width=30,height=2,command=self.do_sentiment_analysis)
        Analysis_btn.pack(pady=(10,10))

        self.emotion_result = Label(self.root,text="",bg='#bc6c25',width=40,height=3,font=('vardana',15,'bold'))
        self.emotion_result.pack(pady=(10,10))


        go_back_btn = Button(self.root,text='Go Back',width=30,height=2,command=self.home_gui)
        go_back_btn.pack(pady=(10.10))
    
    def ner_gui(self):
        self.clear()
        
        heading = Label(self.root,text="NLPApp",bg='#bc6c25',fg='#c4e2ed')
        heading.configure(font=('verdana',18,'bold'))
        heading.pack(pady=(30,30))

        heading = Label(self.root,text="Sentiment Analysis",bg='#bc6c25',fg='#c4e2ed')
        heading.configure(font=('verdana',15))
        heading.pack(pady=(10,20))
        
        label1 = Label(self.root,text='Enter the Text : ',bg='#bc6c25')
        label1.pack(pady=(10,10))
        
        self.ner_input = Text(self.root,width=40,height=6)
        self.ner_input.pack(pady=(10,10))   

        Analysis_btn = Button(self.root,text='Analysis Emotion',width=30,height=2,command=self.do_sentiment_analysis)
        Analysis_btn.pack(pady=(10,10))

        self.ner_result = Label(self.root,text="",bg='#bc6c25',width=40,height=3,font=('vardana',15,'bold'))
        self.ner_result.pack(pady=(10,10))


        go_back_btn = Button(self.root,text='Go Back',width=30,height=2,command=self.home_gui)
        go_back_btn.pack(pady=(10.10))
        
        
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
        

    



nlp = NLPApp() 