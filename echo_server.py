import socket
import sys

def start_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        while True:
            message = input("Введите сообщение (или 'exit' для завершения): ")
            if message.lower() == 'exit':
                break

            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)

            print(f"Ответ от сервера: {data.decode()}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python echo_client.py <хост> <порт>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    start_client(host, port)
