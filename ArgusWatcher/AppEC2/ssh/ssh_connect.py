from pathlib import Path
import paramiko


def ssh_command_to_ec2(key_path, host_public_ip, username, linux_command):
    ''' Sends Linux command to ec2 instance using ssh '''

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    privkey = paramiko.RSAKey.from_private_key_file(key_path)
    result = ""
    
    try:
        print(f'Connecting instance via SSH: {host_public_ip} ... ')
        ssh.connect(hostname=host_public_ip,
                    username=username, pkey=privkey)
        print("SSH establishes.")
        print(f"Execute command '{linux_command}'")
        stdin, stdout, stderr = ssh.exec_command(linux_command)

        print(stdout.read().decode('utf-8'))
        print(stderr.read().decode('utf-8'))

        print(f"Execute completed.")
        result = "Update completed."
    except Exception as ex:
        print(f"Connection fails.")
        print(f"Error: {ex}")
        result = f"Error: {ex}"
    finally:
        ssh.close()
        print('SSH Closed')

    return result
