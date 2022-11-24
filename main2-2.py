#컴퓨터의 외부 및 내부 IP 확인하기
#컴퓨터 내부 IP 알아보는 코드만들기
#socket으로 외부사이트에 접속하고 접속된 정보를 바탕을 IP를 확인하는 방법
import socket

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print(in_addr.getsockname()[0])

