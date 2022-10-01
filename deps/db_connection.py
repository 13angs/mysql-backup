import os
import datetime
from .logging import Logging

class DbConnection:
    host = ''
    password = ''
    user = ''
    database = ''
    dt_format = '%Y-%m-%d_%H:%M:%S'
    log_dt_format = '%Y-%m-%d %H:%M:%S'
    # backup_path = ''
    # restore_path = ''

    def __init__(self, **kwargs) -> None:
        

        self.host = kwargs['host']
        self.password = kwargs['password']
        self.user = kwargs['user']
        self.database = kwargs['database']
    
    def backup(self, bk_path, multiple=False) -> None:
        dt_now = datetime.datetime.now()
        formatted_dt = dt_now.strftime(self.dt_format)
        full_backup_path = os.path.join(bk_path, self.database, formatted_dt , self.database)

        # init the log
        logging = Logging()
        logging.init_log_detail()

        if multiple:
            print('\n=========================================================')
            print('Running backup for multiple db...')
        else:
            # f'docker exec -i {self.host} ' + \
            # check if directory exist if not create it
            sv_dir_path = os.path.join(bk_path, self.database)
            dt_dir_path = os.path.join(bk_path, self.database, formatted_dt)
            if not os.path.exists(sv_dir_path):
                os.mkdir(sv_dir_path)
            if not os.path.exists(dt_dir_path):
                os.mkdir(dt_dir_path)

            dump_cmd = f'mysqldump -h {self.host} -u {self.user} -p{self.password} {self.database} ' + \
                f'> {full_backup_path}.sql'
            gz_cmd = f'gzip {full_backup_path}.sql'
        
        try:
            print('\n=========================================================')
            print(f'Running backup for {self.database}...')
            print(f'Command: {dump_cmd}\n')
            os.system(dump_cmd)

            print(f'Compressing the {self.database}.sql to {self.database}.sql.gz')
            print(f'Command: {gz_cmd}')
            os.system(gz_cmd)

            # setting up logging
            logging.log_detail['server'] = self.host
            logging.log_detail['database'] = self.database
            logging.log_detail['created_date'] = datetime.datetime.now().strftime(self.log_dt_format)
            logging.log_detail['dest'] = f'{full_backup_path}.sql.gz'
            logging.save_checkpoint()
            logging.save_change()
            
            print('\n=========================================================')
            print(f'Finished running backup for {self.database}!')

        except:
            print('Error backup db')

        

