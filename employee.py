#  File: employee.py
#  Description:
#  Student Name: Tyler Smedley
#  Student UT EID: tws933
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number: 52020
#  Date Created: 02/02/2023
#  Date Last Modified: 02/02/2023

import sys

class Employee:
    # All employees have atributes of name, id, and salary
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.id = kwargs.get('id')
        self.salary = kwargs.get('salary')
        self.title = "Employee"

    def __str__(self):
    # returns the employee's job title, name, id, and salary
        return self.title + "\n{},{},{}".format(self.name, self.id, self.salary)

############################################################
############################################################
############################################################

class Permanent_Employee(Employee):
    # Permanent employees also have an atribute of benefits
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.benefits = kwargs.get('benefits')
        self.title = "Permanent_Employee"

    def cal_salary(self):
        # having benefits modifies salary ammount
        if 'retirement' in self.benefits and 'health_insurance' in self.benefits:
            return self.salary * 0.7
        elif 'health_insurance' in self.benefits:
            return self.salary * 0.9
        elif 'retirement' in self.benefits:
            return self.salary * .8
        else:
            return round(float(self.salary), 1)

    def __str__(self):
        # Adds the value for benefits to the general employee string
        return format(super().__str__() + ',' + str(self.benefits))

############################################################
############################################################
############################################################

class Manager(Employee):
    # Managers also get a bonus
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus = kwargs.get('bonus')
        self.title = "Manager"

    def cal_salary(self):
        # bonus is added to base pay to get salary
        salary  = float(self.salary + self.bonus)
        return round(salary, 1)

    def __str__(self):
        # adds the value of bonus to the general employee string
        return super().__str__() + ',' + str(self.bonus)


############################################################
############################################################
############################################################

class Temporary_Employee(Employee):
    # temporary employees have an additional atribute of hours worked
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = kwargs.get('hours')
        self.title = "Temporary_Employee"

    def cal_salary(self):
        # temp employee salary is num of hours worked * hourly pay
        salary = float(self.salary * self.hours)
        return round(salary, 1)

    def __str__(self):
        # adds hours worked to the general employee string
        return super().__str__() + ',' + str(self.hours)


############################################################
############################################################
############################################################


class Consultant(Temporary_Employee):
    # consultants are a subclass of temporary employee with an additional attribute of travel
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = kwargs.get('travel')
        self.title = "Consultant"

    def cal_salary(self):
        # consultant salary is calculated like a temp employee's plus num of times traveled * 1000
        travel_pay = self.travel * 1000
        salary = float(super().cal_salary() + travel_pay)
        return round(salary, 1)

    def __str__(self):
        # adds value for travel to the string for temporary employees
        return format(super().__str__() + ',' + str(self.travel))


############################################################
############################################################
############################################################


class Consultant_Manager(Manager, Consultant):
    # consultant managers have attribues of both managers and consultants
    def __init__(self,  **kwargs):
        Manager.__init__(self, **kwargs)
        Consultant.__init__(self, **kwargs)
        self.title = "Consultant_Manager"

    def cal_salary(self):
        # salary is calculated the same as a consultants plus the manager bonus
        salary = float(Consultant.cal_salary(self) + self.bonus)
        return round(salary, 1)

    def __str__(self):
        # prints the values for the consultant attributes on one line
        # and the values for the manager attribues on the next line
        return Consultant.__str__(self) + ',' + self.title + '\n' + self.name +',' + self.id + ',' + str(self.salary) + ',' + str(self.bonus)


############################################################
############################################################
############################################################



###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100, hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")


if __name__ == "__main__":
  main()
