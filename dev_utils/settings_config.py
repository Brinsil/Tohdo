# Creating configuration file for the program

import json
import os
from os.path import expanduser

class Settings:

    def __init__(self) -> None:
        self.settings_name = self.get_settings_name()
        self.settings_path = self.get_settings_path()
        self.full_settings_path = os.path.join(self.settings_path, self.settings_name)
        self.create_settings_dir()
        self.minimum_default_settings = {'username' : '', 'tasks' : False}

    def get_settings_name(self) -> str:
        return 'settings.json'

    def get_settings_path(self) -> os.path:
        return os.path.join(expanduser('~'), '.config', 'tohdo')

    def get_full_settings_path(self) -> os.path:
        return self.full_settings_path

    def create_settings_dir(self) -> os.path:
        if not os.path.exists(self.settings_path):
            os.makedirs(self.settings_path)

    def settings_exists(self) -> bool:
        return os.path.exists(self.full_settings_path)
    
    def write_settings(self, data : dict) -> None:
        with open(self.full_settings_path, 'w', 
                encoding='utf-8') as settings_file:
            json.dump(data, settings_file, indent=2)

    def get_settings(self) -> dict:
        if self.settings_exists():
            with open(self.full_settings_path, 
                    encoding='utf-8') as settings_file:
                return json.load(settings_file)
        return self.minimum_default_settings
        
    def get_name(self):
        return self.get_settings().get('username', '')

    def get_tasks(self):
        return self.get_settings().get('tasks', False)


if __name__ == '__main__':
    setting = Settings()
    setting.write_settings({'username' : 'Brinsil Elias', 'task' : False})
    print(setting.get_settings())