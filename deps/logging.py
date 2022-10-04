import datetime

class Logging:
    log = []
    log_detail = {}
    created_date = datetime.datetime.now()
    dt_format = '%Y-%m-%d %H:%M:%S'

    def __init__(self) -> None:
        self.created_date = self.created_date.strftime(self.dt_format)
    
    # def load_json(self):


    def save_checkpoint(self) -> None:
        # append to self.log
        self.log.append(self.log_detail)
        print('\n=========================================================')
        print(f'Append {self.log_detail["database"]} to the log...')
    
    def save_change(self):
        # save to json file
        print(f'Saving the log to {self.created_date}.json...')
    
    def init_log_detail(self) -> object:
        self.log_detail = {
            "server": "db_server",
            "database": "db_name",
            "created_date": datetime.datetime.now().strftime(self.dt_format),
            "status": "success",
            "action": "backup",
            "backup_type": "single",
            "dest": "./data/backup/single",
        }
        return self.log_detail