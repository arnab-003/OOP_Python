class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedIn=False
        self.menu()

    def menu(self):
        user_input=input("""Wellcome to ChatBook. How would you like to proced??
                         1. Press 1 for Signup
                         2. Press 2 for Signin
                         3.Press 3 for Write a Post
                         4. Press 4 for Message your friends
                         5.Press any other key to exit!!""")
    
obj=chatbook()
        