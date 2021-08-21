from flask import Flask, request, jsonify, abort
import socket
import json

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from werkzeug.utils import append_slash_redirect

# 챗봇 엔진 접속 정보
host = '127.0.0.1'
port = 5050

# flask 애플리케이션
app = Flask(__name__)

# 챗봇 엔진 서버와 통식
def get_answer_from_engine(bottype, query):
    # 챗봇 엔진 서버 연결
    mySocket = socket.socket()
    mySocket.connect((host, port))

    # 챗봇 엔진 질의 요청
    json_data = {
        'Query' : query,
        'BotType' : bottype
    }
    message = json.dumps(json_data)
    mySocket.send(message.encode())

    # 챗봇 엔진 답변 출력
    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)

    # 챗봇 엔진 서버 연결 소켓 닫기
    mySocket.close()

    return ret_data

# 챗봇 엔진 query 전송 API
@app.route('/query/<bot_type>', methods=['POST'])
def query(bot_type):
    body = request.get_json()

    try:
        if bot_type == 'TEST':
            # 챗봇 API 테스트
            ret = get_answer_from_engine(bottype=bot_type, query=body['query'])
            return jsonify(ret)

        elif bot_type == 'KAKAO':
            body = request.get_json()
            utterance = body['userRequest']['utterance']
            ret = get_answer_from_engine(bottype=bot_type, query=utterance)

            from KakaoTemplate import KakaoTemplate
            skillTemplate = KakaoTemplate()
            return skillTemplate.send_resp(ret)

        elif bot_type == 'NAVER':
            # 네이버는 안할거임
            pass

        else:
            abort(404)

    except Exception as e:
        abort(500)

if __name__ == '__main__':
    app.run()
