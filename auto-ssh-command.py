#!/usr/bin/env python3
import paramiko


# Path to hosts file
file = "hosts"

# Loop through each host
f = open(file, "r")
for x in f:
    # Separate ip from pwd
    ip = 

    # Create ssh client
    ssh = paramiko.SSHClient()

    # Set policy to auto accept ssh keys
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    # Connect to host
    ssh.connect()
    print(x)