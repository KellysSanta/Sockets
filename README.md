# Sockets
Tarea de sockets - Redes

# ****************socket_01.py

Se crea un socket segun las indicaciones socket.AF_INET, socket.SOCK_STREAM y se tiene una captura de errores provenientes de la creación del socket. Sí no se genera error se imprime "Socket created", de lo contrario se muestra mensjae de error y se detiene la ejecución del programa.


# ****************socket_02.py

Adicional a lo que se hace en el archivo socket_01.py, este programa declara un host el cual es "www.google.com" y mediante el metodo gethostbyname() toma el nombre del host y lo pasa al formato de dirección IPv4, y finalmente esta dirección es retornada como un string. Existe también control de errores del tipo gaierror los cuales aparecen cuando el nombre del host es invalido.
