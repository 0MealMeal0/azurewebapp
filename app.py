from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():    
	return render_template("index.html")
# 메인 페이지는 index.html이다.

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=5010, debug=True)
    app.run()
# 주소는 로컬주소와 노트북 주소를 Flask 서버 주소로 사용하고, 포트는 5010번을 사용한다.
# debug=True 옵션으로 소스 저장 시 바로바로 해당 내용이 적용 가능하게 한다.