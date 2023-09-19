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

        raise('Mission status updated to finished!')
    
    @property
    def name(self):
        return self.name
    
    @property
    def finished_missions(self):
        return self.finished_missions
    
    @property
    def work_days(self):
        return self.work_days
    
    @property
    def payment(self):
        return self.payment
    
    @property
    def to_do_missions(self):
        return self.to_do_missions
    
    @property
    def seniority(self):
        return self.seniority


    @name.setter
    def name(self, new_name : str):
        self.name = new_name

    @finished_missions.setter
    def finished_missions(self, new_finished_missions : list):
        self.finished_missions = new_finished_missions
    
    @work_days.setter
    def work_days(self, new_work_days : int):
        self.work_days = new_work_days

    @payment.setter
    def payment(self, new_payment : float):
        self.payment = new_payment

    @to_do_missions.setter
    def to_do_missions(self, new_to_do_missions : list):
        self.to_do_missions = new_to_do_missions
    
    @seniority.setter
    def seniority(self, new_seniority : int):
        self.seniority = new_seniority