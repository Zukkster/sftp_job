import paramiko
import datetime

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

def fn_get_file_sftp():
    # initialise logging function
    #logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
    #logger = logging.getLogger(__name__)

    # get details from config files
    sftp_params = fn_parse_config("etl_process.ini", "remote_sftp")
    sftp_folders = fn_parse_config("etl_process.ini", "sftp_folders")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # print('start')
    try:
        logger.info("SFTP Connection:Send credentials")
        ssh.connect(**sftp_params)
        logger.info("SFTP Connection:SUCCESS")

    except paramiko.SSHException:
        logger.error("SFTP Connection: Connection Error")

    sftp = ssh.open_sftp()
    logger.info(sftp.listdir("/"))

    for file in sftp.listdir("/"):
        sftp.get(remotepath=sftp_folders.get('remote_path') + file, localpath=sftp_folders.get('local_path') + file)
        logger.info("RETRIEVED SFTP FILE: " + file)
        sftp.remove(sftp_folders.get('remote_path') + file)
        logger.info("REMOVED SFTP FILE: " + file)
    ssh.close()
    logger.info("SFTP Connection:CLOSED")


if __name__ == '__main__':
    fn_get_file_sftp()
