from sftp_client import *
import os

host = os.environ['DIVENDO_SFTP_HOST']
password = os.environ['DIVENDO_SFTP_PASSWORD']
username = os.environ['DIVENDO_SFTP_USERNAME']
local_path = '/'
remote_path = '/home/db_admin/data/vivobarefoot/divendo/'
port = 22



sftpclient = create_sftp_client2(host, port, username, password, keyfile_path, 'RSA')

files_moved = move_files_matching(sftpclient, "get", "vb-fulfilled*.*", local_path, remote_path, True)
print(files_moved)

files_moved = move_files_matching(sftpclient, "get", "vb-cancelled*.*", local_path, remote_path, True)
print(files_moved)

sftpclient.close()