# 다수의 쓰레드를 동작시키는 코드 만들고 실행
import threading

def sum(name, value):
    for i in range(0, value):
        print(f'{name} : {i}')

t1 = threading.Thread(target=sum, args=('1번 스레드', 100))
t2 = threading.Thread(target=sum, args=('2번 스레드', 100))

t1.start()
t2.start()

print("Main Thread")