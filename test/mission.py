from project import Project
from developer import Developer
import datetime

class Mission:
    def __init__(self, description: str, start_date: datetime, work_days: int, difficulty: int, developer: Developer, project: Project = None) -> None:
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

        raise('Mission was allocated!')
    
    def assign_project(self, project: Project):
        if self not in project.mission_list:
            self.project = project
            project.mission_list.append(self)
            project.to_do_list.append(self)

        else:
            raise('Mission already assigned!')
        
    def __str__(self) -> str:
        print(f'Mission description: \ndescription: {self.description}, \nstart date: {self.start_date}, \n end date: {self.finish_date}, \nproject: {self.project.description}, \nwork days: {self.work_days}, \ndifficulty: {self.difficulty}, \ndeveloper: {self.developer.name}')
            
    @property
    def description(self):
        return self.description
    
    @property
    def start_date(self):
        return self.start_date
    
    @property
    def finish_date(self):
        return self.finish_date
    
    @property
    def project(self):
        return self.project

    @property
    def work_days(self):
        return self.work_days
    
    @property
    def difficulty(self):
        return self.difficulty
    
    @property
    def developer(self):
        return self.developer
    
    @description.setter
    def description(self, new_description : str):
        if type(new_description) == str:
            self.description = new_description

        else:
            raise Exception('Invalid value!')

    @start_date.setter
    def start_date(self, new_start_date : datetime):
        if type(new_start_date) == datetime:
            self.start_date = new_start_date

        else:
            raise Exception('Invalid value!')

    @finish_date.setter
    def finish_date(self, new_finish_date : datetime):
        if type(new_finish_date) == datetime:
            self.finish_date = new_finish_date

        else:
            raise Exception('Invalid value!')
    
    @project.setter
    def project(self, new_project : Project):
        if type(new_project) == Project:
            self.project = new_project

        else:
            raise Exception('Invalid value!')

    @work_days.setter
    def work_days(self, new_work_days : int):
        if type(new_work_days) == int:
            self.work_days = new_work_days

        else:
            raise Exception('Invalid value!')

    @difficulty.setter
    def difficulty(self, new_difficulty : int):
        if type(new_difficulty) == int:
            self.difficulty = new_difficulty

        else:
            raise Exception('Invalid value!')
    
    @developer.setter
    def developer(self, new_developer : bool):
        if type(new_developer) == bool:
            self.developer = new_developer

        else:
            raise Exception('Invalid value!')
