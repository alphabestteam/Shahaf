from project import Project
from developer import Developer
import datetime

class Mission:
    days_by_month = {1: 31, 2:28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, description: str, start_date: datetime, project: Project, work_days: int, difficulty: int, developer: Developer) -> None:
        self.description = description, 
        self.start_date = start_date, 
        self.finish_date = start_date + datetime.timedelta(days = work_days)
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
