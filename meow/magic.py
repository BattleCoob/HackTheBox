import sys
import telnetlib
import getpass


HOST = sys.argv[1]
user = "root"
password = ""

tn = telnetlib.Telnet()
tn.open(HOST)

tn.read_until(b"login: ")
tn.write(user.encode("ascii")+b"\n")

tn.write(b"exit\n")
print(tn.read_all())
tn.close()
