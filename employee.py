"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, comm_contracts = 0, comm_rate = 0, total_commission = 0):
        self.name = name
        self.comm_contracts = comm_contracts
        self.comm_rate = comm_rate
        temp_commission1 = comm_contracts * comm_rate
        if temp_commission1 > 0:
            self.total_commission = temp_commission1
        else:
            self.total_commission = total_commission 
        self.base_pay = 0

    # def set_contract_commission(self, comm_contracts, comm_rate):
    #     self.comm_contracts = comm_contracts
    #     self.comm_rate = comm_rate
    #     self.total_commission = comm_contracts * comm_rate

    def get_comm_contracts(self):
        return self.comm_contracts

    def get_comm_rate(self):
        return self.comm_rate

    def set_fixed_commission(self, total_commission):
        self.total_commission = total_commission

    def get_total_commission(self):
        return self.total_commission

    def get_base_pay(self):
        return self.base_pay

    def get_pay(self):
        return self.base_pay + self.total_commission

    def __str__(self):
        pass

class Salaried_Employee(Employee):
    def __init__(self, name, salary, comm_contracts = 0, comm_rate = 0, total_commission = 0):
        super().__init__(name, comm_contracts, comm_rate, total_commission)
        self.base_pay = salary

    def __str__(self):
        if (self.comm_contracts == 0 and self.comm_rate == 0 and self.total_commission == 0):
            return f"{self.name} works on a monthly salary of {str(self.base_pay)}. Their total pay is {str(self.get_pay())}."
        elif (self.comm_contracts == 0 and self.comm_rate == 0 and self.total_commission > 0):
            return f"{self.name} works on a monthly salary of {str(self.base_pay)} and receives a bonus commission of {str(self.total_commission)}. Their total pay is {str(self.get_pay())}."
        elif (self.comm_contracts > 0 and self.comm_rate > 0):
            return f"{self.name} works on a monthly salary of {str(self.base_pay)} and receives a commission for {str(self.comm_contracts)} contract(s) at {str(self.comm_rate)}/contract. Their total pay is {str(self.get_pay())}."
        else:
            return (self.name)

class Hourly_Employee(Employee):
    def __init__(self, name, wage_rate, hours, comm_contracts = 0, comm_rate = 0, total_commission = 0):
        super().__init__(name, comm_contracts, comm_rate, total_commission)
        self.wage_rate = wage_rate
        self.hours = hours
        self.base_pay = wage_rate * hours

    def get_hours_worked(self):
        return self.hours

    def get_wage_rate(self):
        return self.wage_rate

    def get_hours_worked(self):
        return self.hours

    def __str__(self):
        if (self.comm_contracts == 0 and self.comm_rate == 0 and self.total_commission == 0):
            return f"{self.name} works on a contract of {str(self.hours)} hours at {str(self.wage_rate)}/hour. Their total pay is {str(self.get_pay())}."
        elif (self.comm_contracts == 0 and self.comm_rate == 0 and self.total_commission > 0):
            return f"{self.name} works on a contract of {str(self.hours)} hours at {str(self.wage_rate)}/hour and receives a bonus commission of {str(self.total_commission)}. Their total pay is {str(self.get_pay())}."
        elif (self.comm_contracts > 0 and self.comm_rate > 0):
            return f"{self.name} works on a contract of {str(self.hours)} hours at {str(self.wage_rate)}/hour and receives a commission for {str(self.comm_contracts)} contract(s) at {str(self.comm_rate)}/contract. Their total pay is {str(self.get_pay())}."
        else:
            return (self.name)

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salaried_Employee('Billie', 4000, 0, 0, 0)
print(billie.get_pay())
print(billie)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly_Employee('Charlie', 25, 100, 0, 0, 0)
print(charlie.get_pay())
print(charlie)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Salaried_Employee('Renee', 3000, 4, 200, 0)
print(renee.get_pay())
print(renee)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Hourly_Employee('Jan', 25, 150, 3, 220, 0)
print(jan.get_pay())
print(jan)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Salaried_Employee('Robbie', 2000, 0, 0, 1500)
print(robbie.get_pay())
print(robbie)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Hourly_Employee('Ariel', 30, 120, 0, 0 ,600)
print(ariel.get_pay())
print(ariel)
