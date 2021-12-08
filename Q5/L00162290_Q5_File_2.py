"""
# File:             L00162290_Q2_File_1.py
# Created:          02/11/2021, 09:34
# Author:           Gonzalo Roo Ponce
# Student Number:   L00162290
# Version:          1.0.0
# Licensing:        GNU
# Support Contact:  l00162290@student.lyit.ie
# Comments:         
"""

import paramiko
import os

def ssh_connection():
    global user_file
    global cmd_file
    global session

    try:
        #open(user_file, 'r')
        ip = "192.168.1.169"
        user_name = "l00162290".rstrip("\n")
        user_password = "J4ef3r34".rstrip("\n")

        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        session.connect(hostname=ip.rstrip("\n"),username=user_name,password=user_password)
    except:
        test = "test"

# Q5.1 - Install curl - FAILED#
#ssh_connection()
#connection = session.invoke_shell()
#session.exec_command("sudo apt install curl; J4ef3r34")


# Q5.2 - Create folder structure #
ssh_connection()
connection = session.invoke_shell()
session.exec_command("mkdir Labs; cd Labs; mkdir Lab1; mkdir Lab2\n")


# Q5.3 - #
# Here I had to find how to gather the information from the command sent, 
# from the Paramiko documentation, using "stdin, stdout, stderr"
print("The list of files in the home folder of the remote VM is as per below: ")
ssh_connection()
connection = session.invoke_shell()
stdin, stdout, stderr = session.exec_command("cd ~;ls -l --time=atime")
output = stdout.readlines()
output = str(output)
for list in output.split(","):
    print(list)

session.close()
