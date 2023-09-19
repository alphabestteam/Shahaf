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
        self.mission_list.append(mission)
        self.to_do_list.append(mission)

        print('Mission was added successfully!')

    def delete_mission(self, mission: Mission) -> None:
        if mission in self.to_do_list and mission not in self.done_list:
            self.mission_list.pop(self.mission_list.index(mission))
            self.to_do_list.pop(self.to_do_list.index(mission))

            print('Mission was deleted successfully!')

        else:
            print('Can not delete mission, mission status is done!')

    def search_mission_by_description(self, description: str) -> Mission:
        for mission in self.mission_list:
            if mission.description == description:
                return mission
            
        print('Mission not found!')