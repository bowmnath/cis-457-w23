'''
Example server code that implements a made-up protocol from the activities.
This protocol intentionally can fail in various ways and is NOT a good
example of how to design a distributed application.
'''
import socket



def parse_ints_from_message(message):
    nums = message.strip().split()

    if len(nums) != 2:
        return None

    try:
        x = int(nums[0])
        y = int(nums[1])
        return (x, y)
    except:
        return None


server_ip = 'localhost'  # needs to be changed before server is started on DataComm
server_port = 11457
buffer_size = 2048

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

print('The server is ready to receive')

greeted = False
while True:
    message, client_address = server_socket.recvfrom(buffer_size)
    modified_message = message.decode('utf-8').upper()
    if not greeted:
        if modified_message == 'HELLO':
            greeted = True
            response = 'Nice to see you!'
        else:
            response = "That's not a proper greeting -- how rude."
    else:
        vals = parse_ints_from_message(modified_message)
        if vals is not None:
            x, y = vals
            if x < y:
                response = '%d is less than %d' % vals
            else:
                response = '%d is not less than %d' % vals
            greeted = False
        else:
            response = ("That's not a pair of numbers... "
                        "are you sure you're feeling alright?")

    server_socket.sendto(response.encode('utf-8'), client_address)
