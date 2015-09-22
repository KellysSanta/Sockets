#!/usr/bin/python
# Este programa retorna el nombre de un servicio dado su numero de puerto
#
import socket

port = 25 # port identifier 
protocolname = "tcp" # protocol
print "Protocol %s, port %i => name [%s]"%(protocolname,port,socket.getservbyport(port, protocolname))
port = 53 # another por identifier
protocolname = "udp" # another transport protocol
print "Protocol %s, port %i => name [%s]"%(protocolname,port,socket.getservbyport(port, protocolname))
