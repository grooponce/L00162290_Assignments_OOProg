"""
# File:             L00162290_Q2_File_1.py
# Created:          02/11/2021, 09:34
# Author:           Gonzalo Roo Ponce
# Student Number:   L00162290
# Version:          1.0.2
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

#Create file to verify SSH connectivity
ssh_connection()
connection = session.invoke_shell()
session.exec_command("mkdir This;cd This; touch that.txt\n")
