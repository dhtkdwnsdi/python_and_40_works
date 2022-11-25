#QR코드 생성기
#[qr코드모음.txt]을 읽어 한 줄 한 줄 표시하는 프로그램
import qrcode
from PIL import Image

file_path = r'qr코드모음.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_lines = f.readlines()

    for line in read_lines :
        line = line.strip()  #line.strip()은 줄 마지막줄에 줄바꿈 문자를 삭제
        print(line)

