class KakaoTemplate:
    def __init__(self):
        # 템플릿 버전
        self.virsion='2.0'
    
    # 단순 텍스트 출력 요소
    def simpleTextComponent(self, text):
        return {
            'simpleText' : {'text' : text}
        }
    
    # 단순 이미지 출력 요소
    def simpleImageComponent(self, imageUrl, altText):
        return {
            'simpleImage' : {'imageUrl' : imageUrl, 'altText' : altText}
        }

    # 사용자에게 응답 스킬 전송
    def send_response(self, bot_resp):
        responseBody = {
            'version' : self.version,
            'templatte' : {
                'outputs' : []
            }
        }

        # 이미지 답변이 텍스트 답변보다 먼저 출력됨
        # 이미지 답변 있는 경우
        if bot_resp['AnswerImageUrl'] is not None:
            responseBody['templatte']['outputs'].append(
                self.simpleImageComponent(bot_resp['AnswerImageurl'], '')
            )
        
        # 텍스트 답변이 있는 경우
        if bot_resp['Answer'] is not None:
            responseBody['templatte']['outputs'].append(
                self.simpleTextComponent(bot_resp['Answer'])
            )
        return responseBody