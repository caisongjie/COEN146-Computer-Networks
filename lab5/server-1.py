# -*- coding: utf-8 -*-

import json
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

def compute_checksum(data, bound=256):
  return sum(data.encode()) % bound




def reliable_recv(udp_socket, packet_size=1024):
  # initialize/create acknowledgement packet
  packet = { "data": '',
             "checksum": '',
             "sequence": ''}  

  while True:
    #   receive packet from client
    packet_recv,addr = udp_socket.recvfrom(packet_size)   
    print(packet_recv)
    #   deserialize packet
    packet_recv1 = json.loads(packet_recv.decode())   
    #   compute checksum of data in packet
    cs = compute_checksum(packet_recv1['data'])  
    #   compare computed checksum with checksum in packet
    # if they match, add 1 to sequence and send it back, then break
    # if they do not match, send back the packet 
    if cs == packet_recv1['checksum']:  
      packet_recv1['sequence'] += 1 
      udp_socket.sendto(json.dumps(packet_recv1).encode(),addr)
      break
    else:
      udp_socket.sendto(json.dumps(packet_recv1).encode(),addr) 
  return packet_recv1['data']  
  #return packet's data




def server(port):
  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  udp_socket.bind( ("", port) )
  term_string = reliable_recv(udp_socket)
  dst_file = reliable_recv(udp_socket)

  with open(dst_file, "w") as stream:
    while True:
      data = reliable_recv(udp_socket)
      if data == term_string:
        break
      stream.write(data)
  udp_socket.close()




if __name__ == "__main__":
  server(port)






