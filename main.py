from deps.db_connection import DbConnection
from deps.settings import Settings

def main():

    settings = Settings()
    action = settings.select_action()

    # setup the db info
    container_name = 'eng-api-db'
    password = 'P@ssw0rd'
    user = 'root'
    database = 'WhappyvDb'

    connection = DbConnection(
        container_name=container_name,
        password=password,
        user=user,
        database=database,
    )

    if action == "backup":
        server_name, server = settings.select_server()
        connection.container_name = server_name

        db = settings.select_db(server)
        connection.database = db
        bk_path = settings.backup_path

        connection.backup(bk_path)

if __name__ == '__main__':
    main()
