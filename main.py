class Employee:
    count = 0
    def __init__(self, name, number, designation, salary):
        self.name = name
        self. number = number
        self. designation = designation
        self. salary = salary
        Employee.count = Employee .count + 1
    def displaycount(self):
        print("Number of Employees in the Company are:")

    def displaydetails(self):
        print("Emp Name:", self.name, "Emp Number:", self.number , "Emp Designation:", self.designation, "Emp Salary:", self.salary )
        #print("Employee number is", self.number)
        #print("Employee designation is", self.designation)
        #print("Employee salary is", self.salary)
e1= Employee ("Mohan", "Pyb-01","TeamLead", "35000")
e2= Employee ("Prashanth", "Pyb-02","Programmer 1", "20000")
e3= Employee ("Pavan kumar", "Pyb-03","Programmer 2","20000")
e4= Employee ("Monika", "Pyb-04","Programmer 3", "20000")
print("Details of all employee:")

e1.displaydetails()
e2.displaydetails()
e3.displaydetails()
e4.displaydetails()