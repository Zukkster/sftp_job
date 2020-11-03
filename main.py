from sftp_client import *
import os

#=========================================================================================
#Get DIVENDO files

host = os.environ['DIVENDO_SFTP_HOST']
password = os.environ['DIVENDO_SFTP_PASSWORD']
username = os.environ['DIVENDO_SFTP_USERNAME']
remote_path = '/'
local_path = '/home/db_admin/data/vivobarefoot/divendo/'
port = 22

#Connect to SFTP site
sftpclient = create_sftp_client2(host, port, username, password, None, None)

#get files
print("get files: FULFILLED")
files_moved = move_files_matching(sftpclient, "get", "vb-fulfilled*.*", local_path, remote_path, True)
print(files_moved)
print("get files: CANCELLED")
files_moved = move_files_matching(sftpclient, "get", "vb-cancelled*.*", local_path, remote_path, True)
print(files_moved)
print("get files: STOCK")
files_moved = move_files_matching(sftpclient, "get", "vb-stock*.*", local_path, remote_path, True)
print(files_moved)

#We're done with this connection close it
sftpclient.close()

#=========================================================================================
#Get MAGENTO files

host = os.environ['MAGENTO_SFTP_HOST']
password = os.environ['MAGENTO_SFTP_PASSWORD']
username = os.environ['MAGENTO_SFTP_USERNAME']
remote_path = '/'
local_path = '/home/db_admin/data/vivobarefoot/magento/'
port = 22

#Connect to SFTP site
sftpclient = create_sftp_client2(host, port, username, password, None, None)

#get files
print("get ANY files")
files_moved = move_files_matching(sftpclient, "get", "*.*", local_path, remote_path, False)

sftpclient.close()