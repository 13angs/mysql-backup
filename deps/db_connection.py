import os
import datetime

class DbConnection:
    container_name = ''
    password = ''
    user = ''
    database = ''
    # backup_path = ''
    # restore_path = ''

    def __init__(self, **kwargs) -> None:
        

        self.container_name = kwargs['container_name']
        self.password = kwargs['password']
        self.user = kwargs['user']
        self.database = kwargs['database']
    
    def backup(self, bk_path, multiple=False) -> None:
        dt_now = datetime.datetime.now()
        formatted_dt = dt_now.strftime('%Y-%m-%d_%H:%M:%S')
        full_backup_path = os.path.join(bk_path, f'{formatted_dt}_{self.database}')

        if multiple:
            print('\n=========================================================')
            print('Running backup for multiple db...')
        else:
            dump_cmd = f'docker exec -i {self.container_name} ' + \
                f'mysqldump -u {self.user} -p{self.password} {self.database} ' + \
                f'> {full_backup_path}.sql'
        
        try:
            print('\n=========================================================')
            print(f'Running backup for {self.database}...')
            os.system(dump_cmd)
            os.system('docker ps')
            print(f'Finished running backup for {self.database}')

        except:
            print('Error backup db')

        

