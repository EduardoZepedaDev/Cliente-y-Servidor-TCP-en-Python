# SE IMPORTA EL MODULE
import socket

# SE INICIA EL SERVER, COMO ESPECIFICACION QUE ESCUCHE EN EL PUERTO 5000
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(5)
    print("Servidor escuchando en localhost:5000")
    # SI LA CONEXION SE REALIZA CORRECTAMENTE SE ENVIE EL MENSAJE DE CONEXION ESTABLECIDA
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexión establecida con {addr}")
        # EL SERVER RECIBE LOS MENSAJES DEL CLIENTE
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Mensaje recibido: {data}")
            # SI EL MENSAJE DEL CLIENTE ES "DECONEXION", EL SERVER SE DECONECTA DEL CLIENTE
            if data.strip().upper() == 'DESCONEXION':
                print("Cliente desconectado.")
                client_socket.close()
                break
            # SI EL MENSAJE NO ES "DECONEXION", EL SERVER LO ENVIA COMO RESPUESTA AL CLIENTE
            response = data.upper()
            client_socket.send(response.encode('utf-8'))

if __name__ == "__main__":
    start_server()