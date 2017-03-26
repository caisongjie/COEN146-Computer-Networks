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

def server(port, chunk_size=1024):
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  except socket.gaierror:
    print('fail to create socket')
  try:
    sock.bind(('',port))
  except:
    print('Bind failed')
    sys.exit()
  r, addr = sock.recvfrom(chunk_size) #receive termination string fron client
  dst_file, addr = sock.recvfrom(chunk_size) # receive dst_file from client
  with open (dst_file,'w') as f:
    while True:
      msg, addr = sock.recvfrom(chunk_size) # receive data from client and write data to dst_file until receiving termination string from client
      if msg == r:
        break
      f.write(msg.decode())
  sock.close()

  # Pseudo Code:
  #   open udp (socket.SOCK_DGRAM) socket
  #   bind socket to listen at port
  #   receive session termination string from client (see note below)
  #   receive dst_file name from client
  #   open dst_file for writing
  #     forever until termination string received (see note below)
  #       receive data (chunk_size at a time) from client
  #       write data to dst_file
  #   close socket
  #
  # Note:
  #   The random number as session termination string is my suggestion.
  #   You can implement it in a different way.



if __name__ == "__main__":
  server(port)
