#!/usr/bin/python

import socket
import time

ip = "8.8.8.8"
port = 22
retry = 5
delay = 5
timeout = 3

def isOpen(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
                s.connect((ip, int(port)))
                s.shutdown(socket.SHUT_RDWR)
                return True
        except:
                return False
        finally:
                s.close()

def checkHost(ip, port):
        ipup = False
        for i in range(retry):
                if isOpen(ip, port):
                        ipup = True
                        break
                else:
                        time.sleep(delay)
        return ipup

if checkHost(ip, port):
        print(ip,"is UP")