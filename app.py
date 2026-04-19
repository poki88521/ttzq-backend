from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app,
     origins=origins,                   # 明确指定允许的源，避免使用通配符 '*'
     methods=["GET", "POST", "OPTIONS"], # 明确指定允许的HTTP方法
     allow_headers=["Content-Type"],     # 明确指定请求中允许携带的头部
     supports_credentials=False)        # 若不需要携带Cookie/Token，设为False

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    message = data.get('message', '')
    reply = f'你发送了：{message}'
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(port=5000)