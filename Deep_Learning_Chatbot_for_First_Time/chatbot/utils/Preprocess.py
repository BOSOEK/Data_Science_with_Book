from konlpy.tag import Komoran

# 챗봇 전처리 클래스
class Preprocess:
    def __init__(self, userdic=None):
        #형태소 분석기 초기화
        self.komoran = Komoran(userdic=userdic)

        # 제외할 품사, 관계언, 기호, 어미, 접미사 제거
        # 코모란 형태소 분석기 품사 정보 : https://docs/komoran.kr/firststep/postypes.html
        self.exclusion_tags = [
            'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ',
            'JX', 'JC',
            'SF', 'SP', 'SS', 'SE', 'SO',
            'EP', 'EF', 'EC', 'ETN', 'ETM',
            'XSN', 'XSV', 'XSA'
        ]
    # 형태소 분석기 POS 태거 호출
    def pos(self, sentence):
        return self.komoran.pos(sentence)

    # 불용어 제거 후 필요한 품사 정보만
    def get_keywords(self, pos, without_tag=False):
        f = lambda x: x in self.exclusion_tags
        word_list = []
        for p in pos:
            if f(p[1]) is False:
                word_list.append(p if without_tag is False else p[0])
        return word_list