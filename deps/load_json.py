import array
from settings import Settings
import os
import json
import uuid
import datetime


settings = Settings()
settings.load()

backup_logs = []
restore_logs = []
dt_format = '%Y-%m-%d %H:%M:%S'
backup_log_detail = {
        "id": "backup_id",
        "server": "db_server",
        "database": "db_name",
        "created_date": "date_created",
        "status": "success",
        "action": "backup_or_restore",
        "backup_type": "single",
        "dest": "path_where_the_file_is_located",
    }

restore_log_detail = {
        "id": "restore_id",
        "backup_id": "restore_id",
        "server": "db_server",
        "database": "db_name",
        "created_date": "date_created",
        "status": "success",
        "action": "backup_or_restore",
        "backup_type": "single",
        "dest": "path_where_the_file_is_located",
    }

log_path = settings.logs_path
backup_name = 'backup.json'
restore_name = 'restore.json'
action = 'restore'

backup_log_file_path = os.path.join(log_path, backup_name)
restore_log_file_path = os.path.join(log_path, restore_name)

# create backup/restore file if not exist
def file_exist(log_file_path, logs) -> bool:
    print('\n=========================================================')
    print('Checking if file exist...')
    if not os.path.exists(log_file_path):
        with open(log_file_path, 'w', encoding='utf8') as json_file:
            # pretty print JSON
            json.dump(logs, json_file, indent=4, sort_keys=True)
        return True
    return True

# load the data
def load_file(log_file_path) -> array:
    with open(log_file_path, 'r', encoding="utf8") as json_file:
        log_file = json.load(json_file)
    return log_file

def save_checkpoint(logs, log_detail):
    logs.append(log_detail)

def save_change(log_file_path, logs):
    with open(log_file_path, 'w', encoding='utf8') as json_file:
        # pretty print JSON
        json.dump(logs, json_file, indent=4, sort_keys=True)
    
    # pretty print the backup_logs
    print(json.dumps(logs, indent=4, sort_keys=True))

def backup_action(backup_path, logs):
    backup_exist = file_exist(backup_path, backup_logs)

    # only load the file if exist
    if backup_exist:
        logs = load_file(backup_path)

    # append the data
    backup_log_detail['id'] = str(uuid.uuid4())
    backup_log_detail['created_date'] = datetime.datetime.now().strftime(dt_format)
    backup_log_detail['status'] = "success"
    backup_log_detail['action'] = "backup"
    backup_log_detail['backup_type'] = "single"
    backup_log_detail['dest'] = backup_path

    save_checkpoint(logs, backup_log_detail)

    # save the data
    save_change(backup_path, logs)

def restore_action(backup_path, restore_path, backup_logs, restore_logs):
    backup_exist = file_exist(backup_path, backup_logs)
    backup_logs = load_file(backup_path)

    # check and only run restore when backup is exist
    if backup_exist:
        restore_exist = file_exist(restore_path, restore_logs)

        if restore_exist:
            restore_logs = load_file(restore_path)

            # append the data
            first_backup_detail = backup_logs[-1]
            restore_log_detail['id'] = str(uuid.uuid4())
            restore_log_detail['backup_id'] = first_backup_detail['id']
            restore_log_detail['id'] = str(uuid.uuid4())
            restore_log_detail['created_date'] = datetime.datetime.now().strftime(dt_format)
            restore_log_detail['status'] = "success"
            restore_log_detail['action'] = "restore"
            restore_log_detail['backup_type'] = "single"
            restore_log_detail['dest'] = restore_path
            save_checkpoint(restore_logs, restore_log_detail)

            # save the restore
            save_change(restore_path, restore_logs)



if __name__ == '__main__':
    if action == 'backup':
        backup_action(backup_log_file_path, backup_logs)

    elif action == 'restore':
        restore_action(backup_log_file_path, restore_log_file_path, backup_logs, restore_logs)
