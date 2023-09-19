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
        if mission.developer == self:
            self.seniority += mission.difficulty
            self.payment += mission.payment
            self.to_do_missions.pop(self.to_do_missions.index(mission))
            self.finished_missions.append(mission)
            mission.is_finished = True
            mission.project.to_do_list.pop(mission.project.to_do_list.index(mission))
            mission.project.done_list.append(mission)
            mission.project.cost_of_project += mission.payment

            raise('Mission status updated to finished!')
        
        else:
            raise Exception('Mission not allocated to this developer, can not change status to finished!')
        
    def __str__(self) -> str:
        print(f'developer description: \nname: {self.name},\nfinished missions: {self.finished_mission}, \nwork days: {self.work_days}, \npayment: {self.payment}, \nunfinished missions: {self.to_do_missions}, \seniority: {self.seniority}')
    
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
    def name(self, new_name: str):
        if type(new_name) == str:
            self.name = new_name

        else:
            raise Exception('Invalid value!')

    @finished_missions.setter
    def finished_missions(self, new_finished_missions: list):
        if type(new_finished_missions) == list:
            self.finished_missions = new_finished_missions

        else:
            raise Exception('Invalid value!')
    
    @work_days.setter
    def work_days(self, new_work_days: int):
        if type(new_work_days) == int:
            self.work_days = new_work_days

        else:
            raise Exception('Invalid value!')

    @payment.setter
    def payment(self, new_payment: float):
        if type(new_payment) == float:
            self.payment = new_payment

        else:
            raise Exception('Invalid value!')

    @to_do_missions.setter
    def to_do_missions(self, new_to_do_missions: list):
        if type(new_to_do_missions) == list:
            self.to_do_missions = new_to_do_missions

        else:
            raise Exception('Invalid value!')
    
    @seniority.setter
    def seniority(self, new_seniority: int):
        if type(new_seniority) == int:
            self.seniority = new_seniority

        else:
            raise Exception('Invalid value!')