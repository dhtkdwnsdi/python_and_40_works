from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() :
    return 'hello'

def main():
    app.run(debug=True, port=80)

if __name__ == '__main__':
    main()

# if __name__ == '__main__' : 의 의미
# __name__은 코드를 직접 실행 시 이름이 __main__입니다.
# 코드가 모듈로 동작시는 __name__이 이름이 모듈이름으로 됩니다.
# 즉 if __name__ == '__main__': 의 의미는 코드를 직접 실행 시 조건이 참입니다.