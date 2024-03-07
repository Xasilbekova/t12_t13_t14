class Developer:
    def __init__(self, surname, position, salary) -> None:
        self.surname = surname
        self.position = position
        self.salary = salary

class SoftwareEngineer(Developer):
    def __init__(self, surname, position, salary, bonus, department) -> None:
        super().__init__(surname, position, salary)
        self.bonus = bonus
        self.department = department

def calculate_payments(engineers):
    payments = {}
    for engineer in engineers:
        if engineer.department not in payments:
            payments[engineer.department] = 0
        payments[engineer.department] += engineer.salary + engineer.bonus
    return payments

obj1 = SoftwareEngineer("Anvar", "Junior", 500, 100, "1-bo'lim")
obj2 = SoftwareEngineer("Vali", "Junior", 500, 100, "2-bo'lim")
obj3 = SoftwareEngineer("Farrux", "Junior", 500, 100, "3-bo'lim")
obj6 = SoftwareEngineer("Farrux", "Junior", 500, 100, "3-bo'lim")
obj4 = SoftwareEngineer("Komila", "Junior", 500, -100, "2-bo'lim")
obj5 = SoftwareEngineer("Anvar", "Junior", 500, 100, "1-bo'lim")

engineers = [obj1, obj2, obj3, obj4, obj5, obj6]

payments = calculate_payments(engineers)

for department, payment in payments.items():
    print(f"{department}: {payment}")
