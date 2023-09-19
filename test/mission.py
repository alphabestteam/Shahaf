from project import Project
from developer import Developer
import datetime

class Mission:
    days_by_month = {1: 31, 2:28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, description: str, start_date: datetime, project: Project, work_days: int, difficulty: int, developer: Developer) -> None:
        self.description = description, 
        self.start_date = start_date, 

        year = start_date.year
        month = start_date.month
        days = start_date.day

        if (days + work_days) > Mission.days_by_month[month]:
            left_days = (days + work_days) - Mission.days_by_month[month]
            month += 1
            if month > 12:
                year += 1
                month = month - 12
                self.finish_date = datetime.date(year, month, left_days)

            else: 
                self.finish_date = datetime.date(year, month, left_days)

        else:
            self.finish_date = datetime.date(year, month, days + work_days)

        self.project = project, 
        self.work_days = work_days, 
        self.difficulty = difficulty, 
        self.developer = developer,

        if developer == None:
            self.payment = 0

        else: 
            self.payment = developer.seniority * (difficulty / work_days), 
        
        self.is_finished = False  

    def allocate_developer(self, developer: Developer) -> None:
        self.developer = developer

        print('Mission was allocated!')
