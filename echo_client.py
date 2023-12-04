import socket
import sys

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Сервер слушает на {host}:{port}")

        connection, client_address = server_socket.accept()

        with connection:
            print(f"Подключено к {client_address}")

            while True:
                data = connection.recv(1024)
                if not data:
                    break
                print(f"Получено: {data.decode()}")
                connection.sendall(data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python echo_server.py <хост> <порт>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    start_server(host, port)
