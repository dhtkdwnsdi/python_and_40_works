#번역 내용을 새 파일로 저장하는 코드 만들기
from os import linesep
import googletrans

translator = googletrans.Translator()

read_file_path = r'영어파일.txt'
write_file_path = r'한글파일.txt'

with open(read_file_path, 'r') as f:
    readlines = f.readlines()

for lines in readlines :
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
    with open(write_file_path, 'a', encoding='UTF8') as f:
        f.write(result1.text + '\n')