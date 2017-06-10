import socket
import struct

class NClient:

   def __init__(self, uuid):
      self.uuid = uuid

   def printUUID(self):
      print("UUID : ", str(self.uuid))
	  
CLIENTS = []

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', MCAST_PORT))  # use MCAST_GRP instead of '' to listen only
                             # to MCAST_GRP, not all groups on MCAST_PORT
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
  print("Receiving...")
  data = sock.recv(10240).decode('utf-8')
  if "C_CON" in data:
    CLIENTS.append(NClient(data.split(":")[1]))