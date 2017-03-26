# -*- coding: utf-8 -*-
import random
import sys
import socket

def usage():
  usg_str = "python3 talk.py $host:$port"
  sys.stderr.write(usg_str.format(sys.argv[0]))
  exit(1)

try:
  host = sys.argv[1].split(':')[0]
  port = int(sys.argv[1].split(':')[1])
  #dst_file = sys.argv[2]
  
except IndexError:
  usage()


def talk(host, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create a socket
  try: # try to connect to the host. exit if host does not exist
    sock.connect((host, port))
  except socket.gaierror:
    print('Host does not exist')
    sys.exit()
  for data in sys.stdin:
    data = data.rstrip() # strip the /n
    sock.sendto(data.encode(), (host, port)) #send data
    if data == 'quit':
      sys.exit()
  sock.close()
  # Pseudo Code:
  #   generate random number as session termination string (see note below)
  #   create a udp (socket.SOCK_DGRAM) socket
  #   try:
  #     connect socket to host at port
  #   except socket.gaierror:
  #     handle case where host does not exist
  #   send session termination string to define it for server
  #   send dst_file name to server
  #   iterate through input data (this line is already written below)
  #     send data to server using socket
  #   send termination string (see note below)
  #   close socket
  #
  # Note:
  #   The random number as session termination string is my suggestion.
  #   You can implement it in a different way.




if __name__ == "__main__":
  talk(host, port)



