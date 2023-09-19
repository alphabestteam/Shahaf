from mission import Mission

class Developer:
    def __init__(self, name: str) -> None:
        self.name = name, 
        self.finished_missions = [], 
        self.work_days = 0, 
        self.payment = 0, 
        self.to_do_missions = [], 
        self.seniority: 1

    def finished_mission(self, mission: Mission) -> None:
        self.seniority += mission.difficulty
        self.payment += mission.payment
        self.to_do_missions.pop(self.to_do_missions.index(mission))
        self.finished_missions.append(mission)
        mission.is_finished = True