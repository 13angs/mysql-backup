from array import array
from difflib import restore
import json
import string

class Settings:
    settings = []
    backup_path = ''
    restore_path = ''

    def __init__(self) -> None:
        pass
    
    def load(self, path='./setting.json'):
        with open(path, 'r', encoding="utf8") as f:
            self.settings = json.load(f)
        
        self.backup_path = self.settings['dest']['backup']
        self.restore_path = self.settings['dest']['restore']

    def select_action(self) -> string:
        # load the setting.json
        self.load()

        print('\n=========================================================')
        print('Available actions: ')

        actions = self.settings['actions']

        for ind in range(1, len(actions)+1):
            print(f"{ind}. {actions[ind-1]}")

        selected_action = int(input('Choose the action: '))
        
        return actions[selected_action-1]
    
    def select_server(self) -> tuple[str, object] :
        print('\n=========================================================')
        print('Available servers: ')

        servers = self.settings['servers']
        for ind in range(1, len(servers)+1):
            print(f"{ind}. {servers[ind-1]['name']}")

        selected_action = int(input('Choose the server: '))
        
        return [servers[selected_action-1]['name'], servers[selected_action-1]]

    def select_db(self, server) -> string:
        print('\n=========================================================')
        server_name = server['name']
        print(f'Available databases for {server_name}: ')

        databases = server['databases']
        for ind in range(1, len(databases)+1):
            print(f"{ind}. {databases[ind-1]}")

        selected_action = int(input('Choose the database: '))
        
        return databases[selected_action-1]

