from mission import Mission
import datetime

class Project:
    days_by_month = {1: 31, 2:28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, description: str, start_date: datetime, mission_list: list, developer_list: list, to_do_list: list, done_list: list, cost_of_project: float) -> None:
        self.description = description, 
        self.start_date = start_date, 

        work_days = 0

        for mission in mission_list:
            work_days += mission.work_days

        self.finish_date = start_date + datetime.timedelta(days = work_days)
        self.mission_list = mission_list, 
        self.developer_list = developer_list, 
        self.to_do_list = mission_list, 
        self.done_list = [], 
        self.cost_of_project = cost_of_project,
        self.is_finished = False

    def add_mission(self, mission: Mission) -> None:
        if mission not in self.mission_list and mission.project == None:
            self.mission_list.append(mission)
            self.to_do_list.append(mission)
            self.developer_list.append(mission.developer)

            raise('Mission was added successfully!')

        else:
            raise Exception('Mission already added!')

    def delete_mission(self, mission: Mission) -> None:
        if mission in self.to_do_list and mission not in self.done_list:
            self.mission_list.pop(self.mission_list.index(mission))
            self.to_do_list.pop(self.to_do_list.index(mission))
            self.developer_list.pop(self.developer_list.index(mission.developer))

            raise('Mission was deleted successfully!')

        else:
            raise Exception('Can not delete mission, mission status is done!')

    def search_mission_by_description(self, description: str) -> Mission:
        for mission in self.mission_list:
            if mission.description == description:
                return mission
            
        raise Exception('Mission not found!')
    
    def _str_(self) -> str:
        return f'name: {self._name}, tz: {self._TZ}, age: {self._age}'
    
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
    def mission_list(self):
        return self.mission_list
    
    @property
    def developer_list(self):
        return self.developer_list
    
    @property
    def to_do_list(self):
        return self.to_do_list

    @property
    def done_list(self):
        return self.done_list
    
    @property
    def cost_of_project(self):
        return self.cost_of_project
    
    @property
    def is_finished(self):
        return self.is_finished
    
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

    @mission_list.setter
    def mission_list(self, new_mission_list : list):
        if type(new_mission_list) == list:
            self.mission_list = new_mission_list

        else:
            raise Exception('Invalid value!')

    @developer_list.setter
    def developer_list(self, new_developer_list : list):
        if type(new_developer_list) == list:
            self.developer_list = new_developer_list

        else:
            raise Exception('Invalid value!')
    
    @to_do_list.setter
    def to_do_list(self, new_to_do_list : list):
        if type(new_to_do_list) == list:
            self.to_do_list = new_to_do_list

        else:
            raise Exception('Invalid value!')

    @done_list.setter
    def done_list(self, new_done_list : list):
        if type(new_done_list) == list:
            self.done_list = new_done_list

        else:
            raise Exception('Invalid value!')

    @cost_of_project.setter
    def cost_of_project(self, new_cost_of_project : float):
        if type(new_cost_of_project) == float:
            self._cost_of_project = new_cost_of_project

        else:
            raise Exception('Invalid value!')
    
    @is_finished.setter
    def is_finished(self, new_is_finished : bool):
        if type(new_is_finished) == bool:
            self.is_finished = new_is_finished

        else:
            raise Exception('Invalid value!')