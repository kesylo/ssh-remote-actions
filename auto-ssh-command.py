#!/usr/bin/env python3
import paramiko
import time


# Path to hosts file
hosts = "hosts.txt"
commands = "commands.txt"
port = 22

# Loop through each host
f = open(hosts, "r")
for x in f:

    # Split the hole string
    list_string = x.split()

    # get ip
    ip = list_string[2]

     # get user
    user = list_string[5]

    # get pwd
    pwd = list_string[8]

    # init connection to host
    ssh_client = paramiko.SSHClient()
    # Accept default policy for fis
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(ip,port=port, username=user, password=pwd)

    sudo_access = f"echo {pwd} | sudo -S "

    g = open(commands, "r")
    for c in g:
        command = sudo_access + c
        stdin, stdout, stderr = ssh_client.exec_command(command)
        cmd_out = stdout.readlines()
        print ('\n'.join(cmd_out))

    


    