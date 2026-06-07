class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedIn=False
        self.menu()

#creating Menu for users
    def menu(self):
        user_input=input("""Wellcome to ChatBook. How would you like to proced??
                         1. Press 1 for Signup
                         2. Press 2 for Signin
                         3.Press 3 for Write a Post
                         4. Press 4 for Message your friends
                         5.Press any other key to exit!!""")
        if user_input=="1":
            self.signup()
        elif  user_input=="2":
            self.signin()
        elif  user_input=="3":
            self.my_post()
        elif  user_input=="4":
            self.sent_msg()
        else:
            exit()
    
    #signup method
    def signup(self):
        email=input("Please Enter your valid Email ID -> ")
        pwd=input("Enter your Password ->")
        self.username=email
        self.password=pwd
        print("You have Signed Up Successfully.")
        print("\n")
        self.menu()
    
    #signin method
    def signin(self):
        if self.username=="" and self.password=="":
            print("Press 1 for Signup first!!")
        else:
            eid=input("Enter your Email Id -> ")
            pswd=input("Enter your Password -> ")
            if self.username ==eid and self.password ==pswd:
                print("You have Successfully Logged in.") 
                self.loggedIn=True   
            else:
                print("Please Enter Valid Credentials!!")
        print("\n")
        self.menu()   

    #user can post method
    def my_post(self):
        if self.loggedIn==True:
            txt=input("What's on your mind??")
            print(txt + "\nHas been published.")
        else:
            print("Please Press 1 for signup")
            print("Please Press 2 for signin") 
        self.menu() 

    #msg to friend

    def sent_msg(self):
        if self.loggedIn==True:
            txt=input("Enter your Message: ")
            friend=input("Enter your friend's Name: ")
            print(f"Message sent successfully to {friend}")
        else:
            print("Please Press 1 for signup")
            print("Please Press 2 for signin") 
        self.menu() 


        
    
obj=chatbook()
        