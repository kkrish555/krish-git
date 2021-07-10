class Emp:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def display(self):
        print("\n Name {} of employee,\n employee ID is {}, \n Salary of employee is {}".format(self.name,self.id,self.salary))
#Program to display staticmethods
class Myclass:
    @staticmethod
    def mymethod(e):
       e.salary+=1000;
       e.display()

e=Emp("i572077","gopi",25000)
e.display()
Myclass.mymethod(e)