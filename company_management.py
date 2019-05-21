class Employee():
  def __init__(self,name,salary):
    self.n=name;
    self.s=salary;
    self.leaves=30;
    self.pay=2000;
  def DisplayEmployee(self):
    print("Name:",self.n,"salary:",self.s)
  def CalcTax(self,s,rate):
    tax = self.s*rate
    print("Your tax payable is",tax);
  def Experiance(self,exp):
    self.exp=exp
    print("The Experiance of",self.n,"is",self.exp,"years")
  def UpdateLeaves(self,num):
    self.leaves=self.leaves-num
    if self.leaves>0:
        print("You have ",self.leaves,"leaves still")
    elif self.leaves==0:
        print("You no longer take leave, because further salary will be deduted")
    else:
        print("Your are exhausded of all the leaves")
        print("You have ",-(self.leaves),"leaves still")
        print("Rs.",self.pay*(-(self.leaves))," will be deducted from the salary")
        self.s=self.s-(self.pay*(-(self.leaves)))
        print("Remaining Amount:",self.s)
emp1=Employee("sudeep",7000)
emp2=Employee("Vibha",50000)

emp1.CalcTax(0,1)
emp2.CalcTax(0,1)

emp1.Experiance(10)
emp2.Experiance(25)

emp1.UpdateLeaves(4)
emp1.UpdateLeaves(25)
emp1.UpdateLeaves(3)
