#/usr/bin/python
import socket
import sys

HOST = '' # Este servidor escuchara por todas las interfaces de red
PORT = 8888 # Un identificador de puerto cualquiera

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'Socket created'

try:
	s.bind((HOST, PORT)) # Esta funcion asocia un socket a un IP y un port
except socket.error, msg:
	print 'Bind failed. Error code: ' + str(msg[0]) + ' message ' + msg[1]
	sys.exit()

print 'Socket bind complete'

s.listen(10)
print 'Socket bind complete'

#Funcion para el manejo de conexiones por medio de hilos
def clientthread(conn,addr):
    #Envio de mensaje de bienvenida al cliente
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string

    #ciclo infinito para recepcion de mensajes
    while True:

        #Lectura de datos que envia el cliente
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data:
            print "Cierre conexion con:"+str(addr[0])
            break

        conn.sendall(reply)

    #cierre de la conexion
    conn.close()


#ahora hablaremos con el cliente con ayuda de la funcion clientthread
while 1:
    #Espera por aceptar la conexion de un cliente
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #Abrimos un hilo con la funcion clientthread
    start_new_thread(clientthread(conn,addr))

s.close()

