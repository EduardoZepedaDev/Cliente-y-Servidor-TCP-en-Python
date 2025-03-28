# SE IMPORTA EL MODULE
import socket

# SE INICIA EL CLIENT, COMO ESPECIFICACION QUE SE CONECTE EN EL PUERTO 5000
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))
    print("Conectado al servidor en localhost:5000")
    # EL CLIENT PIDE QUE SE ESCRIBA UN MENSAJE
    while True:
        message = input("Escribe un mensaje: ")
        client_socket.send(message.encode('utf-8'))
        # SI EL MENSAJE ES 'DESCONEXION', SE CIERRA LA CONEXION AL SERVIDOR Y SE TERMINA EL CLIENTE
        if message.strip().upper() == 'DESCONEXION':
            print("Desconectando del servidor.")
            break
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Respuesta del servidor: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
