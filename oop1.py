class employee:
    def __init__(self): #this is called magic method
        self.id=123
        self.salary=50000
        self.designation="SDE"
    
    def travel(self, destination):# creating method inside the class
        print(f"Travel destination is {destination}")

 #creating the object of that class
arnab=employee()
print(arnab.id)
arnab.travel("Puri")
