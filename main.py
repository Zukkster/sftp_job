from sftp_client import *
import os

host = os.environ['DIVENDO_SFTP_HOST']
password = os.environ['DIVENDO_SFTP_PASSWORD']
username = os.environ['DIVENDO_SFTP_USERNAME']
local_path = '/'
remote_path = '/home/db_admin/data/vivobarefoot/divendo/'
#keyfile_path=None
port = 22

#Connect to SFTP site
sftpclient = create_sftp_client2(host, port, username, password, None, None)

#get files
print("get file 1")
files_moved = move_files_matching(sftpclient, "get", "vb-fulfilled*.*", local_path, remote_path, False)
print(files_moved)
print("get file 2")
files_moved = move_files_matching(sftpclient, "get", "vb-cancelled*.*", local_path, remote_path, False)
print(files_moved)

#sftpclient.close()