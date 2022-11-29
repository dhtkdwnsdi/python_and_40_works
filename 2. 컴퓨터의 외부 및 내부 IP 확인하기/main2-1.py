#컴퓨터 내부 IP 알아보는 코드만들기
import socket

in_addr = socket.gethostbyname(socket.gethostname())

print(in_addr)