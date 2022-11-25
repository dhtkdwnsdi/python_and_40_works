#2. 컴퓨터의 외부 및 내부 IP 확인하기
#컴퓨터 외부 IP 알아보는 코드 만들고 실해
import requests
import re

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print(out_addr)

