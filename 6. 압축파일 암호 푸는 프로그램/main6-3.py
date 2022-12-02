# 비밀번호를 찾으면 프로그램이 종료되는 코드 만들고 실행
import itertools
import zipfile

def un_zip(passwd_string, min_len, max_len, zFile) :
    for len in range(min_len, max_len + 1) :
        to_attempt = itertools.product(passwd_string, repeat = len)
        for attempt in to_attempt:
            passwd = ''.join(attempt)
            print(passwd)
            try:
                zfile.extractall(pwd=passwd.encode())
                print(f'비밀번호는 {passwd} 입니다.')
                return 1
            except:
                pass

passwd_string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

zfile = zipfile.ZipFile(r'암호1234.zip')

min_len = 1
max_len = 5

unzip_result = un_zip(passwd_string, min_len, max_len, zfile)

if unzip_result == 1 :
    print('암호찾기에 성공했습니다.')
else :
    print('암호찾기에 실패했습니다.')