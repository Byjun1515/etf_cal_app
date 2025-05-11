from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '🚀 Render에서 Flask 앱 성공적으로 실행 중입니다!'

if __name__ == '__main__':
    app.run()
