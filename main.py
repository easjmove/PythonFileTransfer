import socket
import json
import base64


def send_file_to_server(server_address, server_port, filename):
    f = open(filename, 'rb')
    data = f.read()

    data = base64.b64encode(data)
    data = data.decode("utf-8")
    payload = {"Name": filename, "Data": data}

    json_data = json.dumps(payload)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((server_address, server_port))

    client_socket.send(json_data.encode())


send_file_to_server("10.200.178.10", 12345, "test.exe")

