#!/bin/bash

if command mysqldump --version >/dev/null 2>&1 ; then
    echo "mysqldump found"
    echo "version: $(mysqldump --version)"
else
    echo "mysqldump not found"
    echo "Installing required dependencies..."
    sudo apt-get update && \
    sudo apt-get install -y mariadb-client
fi

python3 main.py
# PS3="Choose the action: "
# echo "Available actions: "
# select action in Backup Restore
# do
#     case $action in
#         Backup)
#             echo "Backuping db..."
#             python3 main.py
#             break
#             ;;
#         Restore)
#             echo "Restoring db..."
#             break
#             ;;
#         *)
#             break
#             ;;
#     esac
# done
