import datetime

class Worker:
    def __init__(self, id: int, firstName: str, lastName: str, hireDate: datetime):

        self.__id = id
        self.__firstName = firstName
        self.__lastName = lastName
        self.__hireDate = hireDate

    def set_firstName(self, firstName: str):

        self.__firstName = firstName

    def set_lastName(self, lastName: str):

        self.__lastName = lastName

    def get_id(self):

        return self.__id

    def get_firstName(self):

        return self.__firstName

    def get_lastName(self):

        return self.__lastName

    def get_hireDate(self):

        return self.__hireDate

class Employee (Worker):

    def __init__(self, id: int, firstName: str, lastName: str, hireDate: datetime, salary: float):

        self.__salary = salary
        super().__init__(id, firstName, lastName, hireDate)

    def set_salary(self, salary: float):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def get_hourlyRate(self):
        return self.__salary / 261 / 8

class Contractor(Worker):

    def __init__(self, id: int, firstName: str, lastName: str, hireDate: datetime, hourlyRate: float):

        self.__hourlyRate = hourlyRate
        super().__init__(id, firstName, lastName, hireDate)

    def set_hourlyRate(self, hourlyRate: float):
        self.__hourlyRate = hourlyRate

    def get_hourlyRate(self):
        return self.__hourlyRate

class Task:

    def __init__(self, id: int, name: str, description: str, assignedTo: Worker, durationHrs: float):

        self.__id = id
        self.__name = name
        self.__description = description
        self.__assignedTo = assignedTo
        self.__durationHrs = durationHrs
        self.__hrsComp = 0.0

    def set_name(self, name: str):
        self.__name = name

    def set_description(self, description: str):
        self.__description = description

    def set_assignedTo(self, assignedTo: Worker):
        self.__assignedTo = assignedTo

    def set_durationHrs(self, durationHrs: str):
        self.__durationHrs = durationHrs

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_worker(self):
        return self.__assignedTo

    def get_assignedTo(self):
        return self.__assignedTo

    def get_durationHrs(self):
        return self.__durationHrs

    def get_hrsComp(self):
        return self.__hrsComp

    def add_time(self, num_hrs: float):
        self.__hrsComp += num_hrs

class Project:

    def __init__(self, id: int, name: str, HrsEstim: float):

        self.__id = id
        self.__name = name
        self.__HrsEstim = HrsEstim
        self.__tasks = []

    def set_name(self, name: str):
        self.__name = name

    def set_HrsEstim(self, HrsEstim: float):
        self.__HrsEstim = HrsEstim

    def getId(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_HrsEstim(self):
        return self.__HrsEstim

    def add_task(self, task: Task):
        self.__tasks.append(task)

