class Worker:

    def __init__(self, worker_name=""):
        self.__name = worker_name

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

class Employee(Worker):

    def __init__(self, initial_salary, initial_name):
        self.__salary = initial_salary
        super().__init__(initial_name)

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def get_salary(self):
        return self.__salary

e1 = Employee(50000, "Bob")

print(e1.get_name())
print(e1.get_salary())

print(e1.__salary)
