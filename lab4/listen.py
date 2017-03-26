# -*- coding: utf-8 -*-
import sys
import socket

def usage():
  usg_str = "Usage: python3 {} $port\n"
  sys.stderr.write(usg_str.format(sys.argv[0]))
  exit(1)

try:
  port = int(sys.argv[1])
except (IndexError, ValueError):
  usage()

def listen(port):
  try: # open socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
  except socket.gaierror:
    print('fail to create socket')
  try: #bind socket
    sock.bind(('',port))
  except:
    print('Bind failed')
    sys.exit()
  while True:
    msg, addr = sock.recvfrom(1024) # receive data 
    print('{}: {}'.format(addr[0],msg.decode())) #print msg using specific format
    if msg.decode() == 'quit':
      sys.exit()
  sock.close()
 
if __name__ == "__main__":
  listen(port)

