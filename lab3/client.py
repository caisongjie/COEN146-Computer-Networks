import random
import sys
import socket

def usage():
  usg_str = "Usage: python3 {} $host:$port $dst_file <$input_file\n"
  sys.stderr.write(usg_str.format(sys.argv[0]))
  exit(1)

try:
  host = sys.argv[1].split(':')[0]
  port = int(sys.argv[1].split(':')[1])
  dst_file = sys.argv[2]
except IndexError:
  usage()

def get_chunk(chunk_size=1024, stream=sys.stdin):
  while True:
    data = stream.read(chunk_size)
    if not data:
      break
    yield data

def client(host, port, dst_file):

  r = random.random()
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create a udp socket
  try: # try to connect to the host. exit if host does not exist
    sock.connect((host, port))
  except socket.gaierror:
    print('Host does not exist')
    sys.exit()
  sock.sendto(str(r).encode(), (host, port)) #send termination string to server
  sock.sendto(dst_file.encode(),(host, port)) # send dst_file to server
  for data in get_chunk():
    sock.sendto(data.encode(), (host, port)) # send data to server using socket
  sock.sendto(str(r).encode(), (host, port)) # send termination string to server to stop transfer
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
  client(host, port, dst_file)


