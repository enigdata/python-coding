#Inheritance: What common attributes and behaviors exist between real-world objects?
#Inheritance models an is a relationship (Cat is an animal; Apple is a fruit; Fish is a food and an animal)

#Composition: How are objects in the real world composed (made up) of one another?
#Composition models a has a relationship (A car is composed of an engine)
#In Python, one class can be a component of another composite class

class MyError(Exception):
    def __init__(self, message):
        super().__init__(message)

#raise MyError("Something went wrong")

#Interface: a description of the features and behaviors 
class PayrollSystem:
    def calculate_payroll(self, employees):
        print("Calculating Payroll")
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check Amount: {employee.calculate_payroll()}')
            print('')

#this is an abstract class. We can only inherit from it but not instantiate it 
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name 

    @abstractmethod
    def calculate_payroll(self):
        pass 

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate 

    def calculate_payroll(self):
        return self.hour_rate * self.hours_worked

class ComissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission
    
    def calculate_payroll(self):
        fixed = super().calculate_payroll() # same as super().weekly_salary()
        return fixed + self.commission

salary_employee = SalaryEmployee(1, "John Smith", 1500)
hourly_employee = HourlyEmployee(2, "Jane Doe", 40, 15)
commission_employee = ComissionEmployee(3, "Kevin Bacon", 1000, 250)

payroll_system = PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])

class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours}.')

class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')

class SalesPerson(ComissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')

class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')

class ProductivitySystem:
    def track(self, employees, hours):
        print("Tracking productivity")
        print('=====================')
        for employee in employees:
            employee.work(hours)

        print('')

      
class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)

    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)

#TODO: finish the rest materials on composition       




