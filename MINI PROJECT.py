#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Employee:
    employeelist=list()
    def __init__(self,empid,empName,empDes,empSal):
        self.empid=empid
        self.empName=empName
        self.empDes=empDes
        self.empSal=empSal
    def addNewEmployee(self):
        Employee.employeelist.append(self)
    def getEmplist(self):
        return Employee.employeelist
    def getEmpById(self,empid):
        for emp in Employee.employeelist:
            if(emp.getempid(empid)==empid):
                return emp
        return False
    def setempid(self,empid):
        self.empid=empid
    def getempid(self,empid):
        return self.empid
    def setempName(self,empName):
        self.empName=empName
    def getempName(self,empName):
        return self.empName
    def setempDes(self,empDes):
        self.empDes=empDes
    def getempDes(self,empDes):
        return self.empDes
    def setempSal(self,empSal):
        self.empSal=empSal
    def getempSal(self,empSal):
        return self.empSal
    def __str__(self):
        return "%d %s %s %d"%(self.empid,self.empName,self.empDes,self.empSal)
choice=1
employee=Employee(0,"","",0.0)
while choice>=1 and choice<=3:
    print("\n\n1.Add new employee\n 2.Get all employee list\n 3.Get Employee by Id\n\n")
    choice=int(input("Enter your choice"))
    if(choice==1):
        empid=int(input("Enter Employee id:"))
        empName=input("Enter Employee Name:")
        empDes=input("Enter Employee Designation:")
        empSal=float(input("Enter Employee Salary"))
        emp=Employee(empid,empName,empDes,empSal)
        emp.addNewEmployee()
    elif(choice==2):
        print("\n")
        for emp in employee.getEmplist():
            print(emp)
    elif(choice==3):
        empid=int(input("Enter Employee id:"))
        empid=employee.getEmpById(empid)
        if (emp==False):
            print("\n SORRY Employee not found for Id!!!",empid)
        else:
            print(emp) 


# In[ ]:





# In[ ]:




