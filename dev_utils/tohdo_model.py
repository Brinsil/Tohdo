# Creating class for the model

from datetime import datetime

class Tohdo:
    def __init__(self, id, task, section, date_completed = None, status = 'To-do') -> None:
        self.id = id
        self.task = task
        self.section = section
        self.date_added = datetime.now().isoformat()
        self.date_completed = date_completed
        self.status = status

    def get_id():
        return self.id

    def get_section():
        return self.section

    def get_date_added():
        return self.date_added

    def get_date_completed():
        return self.date_completed

    def get_status():
        return self.status

    def __repr__(self) -> str:
        return f'{self.id}, {self.task}, {self.section}, {self.date_added}, {self.date_completed}, {self.status}'



