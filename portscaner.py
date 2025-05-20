#!/usr/bin/env python3

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
import signal
import sys

def colored (str, *args):
    return str
open_sockets = []

def def_handler(sig, frame):
    print(colored(f"\n[!] Quiting program...", 'red'))

    for socket in open_sockets:
        socket.close()

    sys.exit(1)

signal.signal(signal.SIGINT, def_handler) # Ctrl+C


def get_arguments():
    parser = argparse.ArgumentParser(description='Fast TCP Port Scanner')
    parser.add_argument("-t", "--target", dest="target", required=True, help="Victim Target to scan (Ex: -t 192.168.1.254)")
    parser.add_argument("-p", "--port", dest="port", required=True, help="Port range to scan (Ex: -p 1-65535) or Port to scan (EX: -p 80) or Ports to scan (Ex: -p 22,80,443)")
    options = parser.parse_args()

    return options.target, options.port

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    open_sockets.append(s)

    return s

def port_scanner(port, host):

    s = create_socket()

    try:
        s.connect((host, port))
        s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
        response = s.recv(1024)
        response = response.decode(errors='ignore').split('\n')

        if response:
            print(colored(f"\n[+] Port {port} is open", 'green'))

            for line in response:
                print(colored(line, 'grey'))
        else:
            print(colored(f"\n[+] Port {port} is open", 'green'))

    except (socket.timeout, ConnectionRefusedError):
       print(colored(f"\n[x] Port {port} is closed", 'red'))
       pass

    finally:
       s.close()

def scan_ports(ports, target):

    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda port: port_scanner(port, target), ports)



def parse_ports(ports_str):

    if '-' in ports_str:
        start, end = map(int, ports_str.split('-'))
        return range(start, end+1)
    elif ',' in ports_str:
        return map(int, ports_str.split(','))
    else:
        return (int(ports_str),)

def main():

    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    scan_ports(ports, target)


if __name__ == '__main__':
    main()
