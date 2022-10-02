"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class Salaried_Employee(Employee):
    def __init__(self, name, salary):
        super.__init__(name)
        self.base_pay = salary

class Hourly_Employee(Employee):
    def __init__(self, name, wage_rate, hours):
        super.__init__(name)
        self.base_pay = wage_rate * hours

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salaried_Employee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly_Employee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Salaried_Employee('Renee', 3000)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Hourly_Employee('Jan', 25, 150)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Salaried_Employee('Robbie', 2000)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Hourly_Employee('Ariel', 30, 120)
