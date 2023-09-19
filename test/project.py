class Project:
    def __init__(self, description: str, start_date: str, finish_date: str, mission_list: list, developer_list: list, to_do_list: list, done_list: list, cost_of_project: float) -> None:
        description: str, 
        start_date: str, 
        finish_date: str,
        mission_list: list, 
        developer_list: list, 
        to_do_list: list, 
        done_list: list, 
        cost_of_project: float
        self.is_finished = False