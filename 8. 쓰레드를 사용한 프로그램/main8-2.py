import threading
import time

def thread_1():
    while True:
        print('스레드1 동작')
        time.sleep(1)

t1 = threading.Thread(target=thread_1)
t1.daemon = True   #파이썬을 종료하면 실행하고 있는 쓰레드도 함께 종료
t1.start()

while True:
    print("메인동작")
    time.sleep(2)