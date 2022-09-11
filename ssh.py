import paramiko
from paramiko.ssh_exception import AuthenticationException

def check_ssh():

    # linux服务器信息
    host_ip = "192.168.1.12"
    t = paramiko.Transport((host_ip, 22))
    return t
