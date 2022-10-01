import os
import datetime

class DbConnection:
    host = ''
    password = ''
    user = ''
    database = ''
    # backup_path = ''
    # restore_path = ''

    def __init__(self, **kwargs) -> None:
        

        self.host = kwargs['host']
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
            # f'docker exec -i {self.host} ' + \
            dump_cmd = f'mysqldump -h {self.host} -u {self.user} -p{self.password} {self.database} ' + \
                f'> {full_backup_path}.sql'
        
        try:
            print('\n=========================================================')
            print(f'Running backup for {self.database}...')
            os.system(dump_cmd)
            print(f'Finished running backup for {self.database}')

        except:
            print('Error backup db')

        

