from os import linesep
import googletrans

translator = googletrans.Translator()

#read_file_path = r'9. 영어 문서를 한글로 자동번역\영어파일.txt'
read_file_path = r'영어파일.txt'

with open(read_file_path, 'r') as f :
    readlines = f.readlines()

for lines in readlines :
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)