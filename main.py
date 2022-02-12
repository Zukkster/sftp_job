from sftp_client import *
import os
import logging


dir_path = os.path.dirname('/home/db_admin/logs/')
filename = os.path.join(dir_path, "sftp_job.log")
#Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter("%(asctime)s|%(name)s|%(levelname)s|%(message)s"))
logger.addHandler(file_handler)

logger.info("Starting sftp_job")
#=========================================================================================
#Get DIVENDO files

host = os.environ['DIVENDO_SFTP_HOST']
password = os.environ['DIVENDO_SFTP_PASSWORD']
username = os.environ['DIVENDO_SFTP_USERNAME']
remote_path = '/'
local_path = '/storage/data/vivobarefoot/divendo/'
port = 22

#Connect to SFTP site
sftpclient = create_sftp_client2(host, port, username, password, None, None)
logger.info("Sucessfuly connected to divendo - hostname:" + os.environ['DIVENDO_SFTP_HOST'])

#get VIVO files
files_moved = move_files_matching(sftpclient, "get", "vb-fulfilled*.*", local_path, remote_path, True)
logger.info("Retrieved " + str(files_moved) + " FULFILLMENT  VIVOBAREFOOT files from divendo sftp")

files_moved = move_files_matching(sftpclient, "get", "vb-cancelled*.*", local_path, remote_path, True)
logger.info("Retrieved " + str(files_moved) + " CANCEL VIVOBAREFOOT files from divendo sftp")

files_moved = move_files_matching(sftpclient, "get", "vb-stock*.*", local_path, remote_path, True)
logger.info("Retrieved " + str(files_moved) + " STOCK  VIVOBAREFOOT files from divendo sftp")

#get VIVO files

local_path = '/storage/data/revivo/divendo/'

files_moved = move_files_matching(sftpclient, "get", "revivo-fulfilled-*.*", local_path, remote_path, True)
logger.info("Retrieved " + str(files_moved) + " FULFILLMENT REVIVO files from divendo sftp")

files_moved = move_files_matching(sftpclient, "get", "revivo-cancelled-*.*", local_path, remote_path, True)
logger.info("Retrieved " + str(files_moved) + " CANCEL REVIVO files from divendo sftp")

#We're done with this connection close it
sftpclient.close()
logger.info("Closed connected to magento SFTP")
#=========================================================================================
#Get MAGENTO files

host = os.environ['MAGENTO_SFTP_HOST']
password = os.environ['MAGENTO_SFTP_PASSWORD']
username = os.environ['MAGENTO_SFTP_USERNAME']
remote_path = '/PerformalyticsLive/PAREPORTS/'
local_path = '/storage/data/vivobarefoot/magento/'
port = 22

#Connect to SFTP site
sftpclient = create_sftp_client2(host, port, username, password, None, None)
logger.info("Sucessfuly connected to magento - hostname:" + os.environ['MAGENTO_SFTP_HOST'])

#get files
files_moved = move_files_matching(sftpclient, "get", "VIVO-New-SalesOverview*.*", local_path, remote_path, True)
logger.info("Retrieved " + str(files_moved) + " from magneto sftp")

sftpclient.close()
logger.info("Closed connected to magento SFTP")

logger.info("Completed sftp_job")
