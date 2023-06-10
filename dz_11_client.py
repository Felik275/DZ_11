import socket

def start_client():
    host = 'localhost'  # IP-адреса сервера
    port = 55555  # Порт сервера

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        # Введення повідомлення для сервера
        message = input('Введіть повідомлення: ')

        # Надсилаємо повідомлення на сервер
        client_socket.send(message.encode('utf-8'))

        # Очікуємо відповідь від сервера
        while True:
            response = client_socket.recv(1024).decode('utf-8')
            print(f'Відповідь від сервера: {response}')

    # Закриваємо з'єднання з сервером
    client_socket.close()


start_client()