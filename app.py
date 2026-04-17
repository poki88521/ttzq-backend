from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有跨域

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    message = data.get('message', '')
    reply = f'你发送了：{message}'
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(port=5000)