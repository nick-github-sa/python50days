#!/usr/bin/python

import socket
import time

ips = ['185.124.68.35','185.124.68.7','185.124.68.40','185.124.68.41','185.124.68.50','185.124.68.52','185.124.68.56','185.124.68.57','185.124.68.66','185.124.68.67','185.124.68.82','185.124.68.83','185.124.68.84','185.124.68.85','jb.mittoapi.com','rest-fra.mittoapi.net','www.mitto.ch']
port = 22
retry = 1
delay = 1
timeout = 2

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

for ip in ips:
    if checkHost(ip, port):
        print(ip,"is UP")
