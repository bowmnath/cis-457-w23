'''
Example client code that implements a made-up protocol from the activities.
This protocol intentionally can fail in various ways and is NOT a good
example of how to design a distributed application.
'''
import socket



server_ip = 'localhost'
server_port = 11457
buffer_size = 2048

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    message = input('Input message:')

    client_socket.sendto(message.encode('utf-8'), (server_ip, server_port))
    response, server_address = client_socket.recvfrom(buffer_size)
    print(response.decode('utf-8'))
client_socket.close()
