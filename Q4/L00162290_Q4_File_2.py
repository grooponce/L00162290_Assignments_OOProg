#!/usr/bin/env python
"""
# File:             L00162290_Q4_File_2.py
# Created:          07/12/2021, 22:53
# Author:           Gonzalo Roo Ponce
# Student Number:   L00162290
# Version:          1.0.0
# Licensing:        GNU
# Support Contact:  l00162290@student.lyit.ie
# Comments:         
"""

import socket
import subprocess
import sys
from datetime import datetime


def port_scan():
    subprocess.call("clear", shell=True)
    remoteServer = input("Enter a remote host to scan: ")
    remoteServerIP = socket.gethostbyname(remoteServer)
    print("#-" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("#-" * 60)

    t1 = datetime.now()

    try:
        for port in range(1, 65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0 and port == 22:
                print("SSH".format(port))
            elif result == 0 and port == 80:
               print("HTTP".format(port))
            elif result == 0:
                print("Port {}: Open".format(port))
        sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    t2 = datetime.now()
    total = t2 - t1

    print('Scanning Completed in: ', total)
port_scan()
