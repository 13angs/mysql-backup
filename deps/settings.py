import json
import string

class Settings:
    settings = []
    single_backup = ''
    multiple_backup = ''
    restore_path = ''
    logs_path = ''
    backup_path = ''
    backup_type = []

    def __init__(self) -> None:
        pass
    
    def load(self, path='./setting.json'):
        with open(path, 'r', encoding="utf8") as f:
            self.settings = json.load(f)
        
        self.single_backup = self.settings['dest']['single_backup']
        self.multiple_backup = self.settings['dest']['multiple_backup']
        self.backup_path = self.settings['dest']['backup']
        self.restore_path = self.settings['dest']['restore']
        self.logs_path = self.settings['dest']['logs']
        self.backup_type = self.settings['backup_type']

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
    
    def select_backup_type(self):
        print('\n=========================================================')
        print('How would you save the db: ')

        selected_type = 0

        for ind in range(1, len(self.backup_type)+1):
            print(f"{ind}. {self.backup_type[ind-1]}")

        selected_type = int(input('Choose the database: '))
        
        return self.backup_type[selected_type-1]

