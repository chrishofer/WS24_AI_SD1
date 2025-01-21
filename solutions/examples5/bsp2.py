class Employee:
    def __init__(self, lastname: str, firstname: str, department: str, base_salary: float):
        self._lastname = lastname
        self._firstname = firstname
        self._department = department
        self._base_salary = base_salary

    def get_full_salary(self) -> float:
        return self._base_salary

class FixCommissionEmployee(Employee):
    def __init__(self, lastname: str, firstname: str, department: str, base_salary: float, additional_commission: float):
        super().__init__(lastname, firstname, department, base_salary)
        self._additional_commission = additional_commission

    def get_full_salary(self) -> float:
        return self._base_salary + self._additional_commission

class PercentComissionEmployee(Employee):
    def __init__(self, lastname: str, firstname: str, department: str, base_salary: float, percent_commission: float):
        super().__init__(lastname, firstname, department, base_salary)
        self._percent_commission = percent_commission

    def get_full_salary(self) -> float:
        return self._base_salary * (1.0 + self._percent_commission / 100)


class EmployeeManager:
    def __init__(self):
        self.__emp_list = []

    def add_employee(self, emp: Employee):
        self.__emp_list.append(emp)

    def calc_total_salary(self) -> float:
        total = 0
        for emp in self.__emp_list:
            total += emp.get_full_salary()
        return total

    def get_salary_by_department(self) -> dict[str, float]:
        d = {}

        for e in self.__emp_list:
            d[e._department] = d.get(e._department, 0) + e.get_full_salary()

        return d

if __name__ == '__main__':
    mg = EmployeeManager()

    mg.add_employee(Employee("wurst", "hans", "IT", 2000))
    mg.add_employee(FixCommissionEmployee("wurst", "tina", "IT", 2000, 500))
    mg.add_employee(PercentComissionEmployee("lind", "peter", "Marketing", 2000, 10))

    print(mg.calc_total_salary())
    print(mg.get_salary_by_department())