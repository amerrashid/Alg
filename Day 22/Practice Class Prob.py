import datetime

class Worker:

    def __init__(self, id, name, hireDate):
        self.id = id
        self.name = name
        self.hireDate = hireDate


class Employee (Worker):

    def __init__(self, yearlySal):
        self.id = id
        self.yearlySal = yearlySal

    def get_hr(self, hrsWork):
        self.hrsWork = hrsWork
        return self.hrsWork

class Contractor (Worker):

    def __init__(self, hourlyRate):
        self.id = id
        self.hourlyRate = hourlyRate

    def get_hr(self, hrsWork):
        self.hrsWork = hrsWork
        return self.hrsWork

class Task:

    def __init__(self, TaskId = int, TName = str, TDesc = str, DuratHrs = datetime, WHrsWrk = int, TAssignTo = []):
        self.TaskId = TaskId
        self.TName = TName
        self.TDesc = TDesc
        self.TAssignTo = TAssignTo
        self.DuratHrs = DuratHrs
        self.WHrsWrk = WHrsWrk



