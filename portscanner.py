#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear screen
subprocess.call('clear', shell=True)

# Get host address
remoteServer = input("Enter remote host: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Start time
started_at = datetime.now();

try:
	for port in range(1,1025):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
		  print("Port " + format(port) + " open!")
		sock.close()

# Close program
except KeyboardInterrupt:
	print("Pressed Ctrl+C")
	sys.exit()

# Hostname error
except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()

# Connect error
except socket.error:
	print("Couldn't connect to server")
	sys.exit()

# Finish time
finished_at = datetime.now()

# Elapsed Time
elapsed = started_at - finished_at

print("Completed in: ", elapsed)
