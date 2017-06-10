import socket
import uuid
import struct
	
CLIENT_ID = uuid.uuid4()

MCAST_GRP = '192.168.1.255'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
sock.sendto(bytes("C_CON:"+str(CLIENT_ID),"UTF-8"), (MCAST_GRP, MCAST_PORT))