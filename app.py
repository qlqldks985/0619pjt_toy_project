# Flask 서버를 사용하기 위해 가져옴
from flask import Flask, render_template


# 내가 만든 회원관리 Blueprint 가져오기
from blueprints.member_service_JJH.routes import member_bp
from blueprints.bank_IGE.bank import bank_bp


# Flask 애플리케이션 생성
app = Flask(__name__)

app.register_blueprint(bank_bp)

@app.route('/')
def home():
    return render_template('index.html')

# 세션(session) 기능을 사용하기 위한 비밀키
# 로그인 정보 저장할 때 필요
app.secret_key = 'team_project_secret'


# -----------------------------
# Blueprint 등록
# -----------------------------
# routes.py 에서 만든 회원관리 기능을
# Flask 서버에 등록하는 작업

app.register_blueprint(member_bp)


@app.route('/bank_home')
def bank_home():
    return render_template('bank/bank_home.html')

# -----------------------------
# 서버 실행
# -----------------------------
# 현재 파일을 직접 실행했을 때만
# Flask 서버가 켜짐

if __name__ == '__main__':
    app.run(debug=True)