import os
import paramiko
import fnmatch

def create_sftp_client(host, port, username, password, keyfilepath, keyfiletype):
    """
    create_sftp_client(host, port, username, password, keyfilepath, keyfiletype) -> SFTPClient

    Creates a SFTP client connected to the supplied host on the supplied port authenticating as the user with
    supplied username and supplied password or with the private key in a file with the supplied path.
    If a private key is used for authentication, the type of the keyfile needs to be specified as DSA or RSA.
    :rtype: SFTPClient object.
    """
    sftp = None
    key = None
    transport = None
    try:
        if keyfilepath is not None:
            # Get private key used to authenticate user.
            if keyfiletype == 'DSA':
                # The private key is a DSA type key.
                key = paramiko.DSSKey.from_private_key_file(keyfilepath)
            #if keyfiletype == 'RSA':

            else:
                # The private key is a RSA type key.
                key = paramiko.RSAKey.from_private_key_file(keyfilepath)

        # Create Transport object using supplied method of authentication.
        transport = paramiko.Transport((host, port))
        transport.connect(None, username, password, key)

        sftp = paramiko.SFTPClient.from_transport(transport)

        return sftp
    except Exception as e:
        print('An error occurred creating SFTP client: %s: %s' % (e.__class__, e))
        if sftp is not None:
            sftp.close()
        if transport is not None:
            transport.close()
        pass


def create_sftp_client2(host, port, username, password, keyfilepath, keyfiletype):
    """
    create_sftp_client(host, port, username, password, keyfilepath, keyfiletype) -> SFTPClient

    Creates a SFTP client connected to the supplied host on the supplied port authenticating as the user with
    supplied username and supplied password or with the private key in a file with the supplied path.
    If a private key is used for authentication, the type of the keyfile needs to be specified as DSA or RSA.
    :rtype: SFTPClient object.
    """
    ssh = None
    sftp = None
    key = None
    try:
        if keyfilepath is not None:
            # Get private key used to authenticate user.
            if keyfiletype == 'DSA':
                # The private key is a DSA type key.
                key = paramiko.DSSKey.from_private_key_file(keyfilepath)
            else:
                # The private key is a RSA type key.
                key = paramiko.RSAKey.from_private_key_file(keyfilepath)

        # Connect SSH client accepting all host keys.
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if keyfilepath is  None:
            print("connect1")
            ssh.connect(host, port, username, password, key)
        else:
            print("connect2")
            ssh.connect(host, port, username, password, look_for_keys=False, allow_agent=False)

        # Using the SSH client, create a SFTP client.
        sftp = ssh.open_sftp()
        # Keep a reference to the SSH client in the SFTP client as to prevent the former from
        # being garbage collected and the connection from being closed.
        sftp.sshclient = ssh

        return sftp
    except Exception as e:
        print('An error occurred creating SFTP client: %s: %s' % (e.__class__, e))
        if sftp is not None:
            sftp.close()
        if ssh is not None:
            ssh.close()
        pass






# List files in the default directory on the remote computer.
#dirlist = sftpclient.listdir('./cron.*')
# for row in dirlist:
#     print (row)
def move_files_matching (sftp_client, action, filename_pattern, local_path, remote_path, remove_file):

    file_count=0
    try:
        if action == "get":
            for filename in sftp_client.listdir(remote_path):
                if fnmatch.fnmatch(filename, filename_pattern):
                    file_count += 1
                    sftp_client.get(remote_path + filename, local_path + filename)
                    if remove_file:
                        sftp_client.remove(remote_path + filename)

        if action == "put":
            for filename in os.listdir(local_path):
                if fnmatch.fnmatch(filename, filename_pattern):
                    file_count += 1
                    sftp_client.put(local_path + filename, remote_path + filename)
                    if remove_file:
                        os.remove(local_path + filename)

        return file_count
    except Exception as e:
        print('An error occurred moving files to/from the SFTP: %s: %s' % (e.__class__, e))
        # if sftp_client is not None:
        #     sftp_client.Clos

# Retrieve a file with the name 'remote_file.txt' on the remote computer and store it in a file named 'downloaded_file.txt'
# next to this SFT client program.
#sftpclient.get('remote_file.txt', 'downloaded_file.txt')
# Upload a file that locally has the name 'testfile.txt' to a file on the remote computer that will have the name 'remote_testfile.txt'.
#sftpclient.put('C:/Users/stuar/Documents/cron.log', '/home/stuar/cron.log')

# We're done with the SFTPClient.
#sftpclient.close()