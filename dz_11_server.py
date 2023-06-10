import socket
import datetime


def message_chat(msg: str):

    if 'привіт' in msg.lower():
        return 'Привіт клієнте'
    elif 'дата' in msg.lower():
        return str(datetime.datetime.today().date())
    elif 'година' in msg.lower():
        return str(datetime.datetime.today().time())
    else:
        return 'Повідомлення отримано'
def handle_client(client_socket, client_address):
    while True:

        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break

        print(f'Повідомлення від клієнта {client_address}: {message}')

        response_2 = str(len(message.split()))
        client_socket.send(message_chat(message).encode('utf-8'))
        client_socket.send(response_2.encode('utf-8'))

    # Закриваємо з'єднання з клієнтом
    client_socket.close()


def start_server():
    host = '127.0.0.1'  # IP-адреса сервера
    port = 55555  # Порт сервера

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f'Сервер запущений на {host}:{port}')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"З'єднання встановлено з {client_address}")

        handle_client(client_socket,client_address)

start_server()