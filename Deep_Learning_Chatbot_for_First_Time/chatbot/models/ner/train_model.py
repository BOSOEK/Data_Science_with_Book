# 챗봇 엔진 NER 모델

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

import tensorflow as tf
from tensorflow.keras import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
from utils.Preprocess import Preprocess

# 학습 파일 불러오기
def read_file(file_name):
    sents = []
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for idx, l in enumerate(lines):
            if l[0] == ',' and lines[idx + 1][0] == '$':
                this_sent = []
            elif l[0] == '$' and lines[idx - 1][0] == ',':
                continue
            elif l[0] == '\n':
                sents.append(this_sent)
            else:
                this_sent.append(tuple(l.split()))
    return sents

# 전처리 객체 생성
p = Preprocess(word2index_dix='./train_tools/dict/chatbot_dict.bin', userdic='./utils/user_dic.tsv')

# 학습용 말뭉치 데이터를 불러옴
corpus = read_file('models/ner/ner_train.txt')

# 말뭉치 데이터에서 단어와 BIO 태그만 불러와 학습용 데이터셋 생성
sentences, tags = [], []
for t in corpus:
    tagged_sentence = []
    sentence, bio_tag = [], []
    for w in t:
        tagged_sentence.append((w[1], w[3]))
        sentence.append(w[1])
        bio_tag.append(w[3])

    sentences.append(sentence)
    tags.append(bio_tag)

print('샘플 크기 : \n', len(sentences))
print('0번째 샘플 단어 시퀀스 : \n', sentences[0])
print('0번째 샘플 bio 태그 : \n', tags[0])
print('샘플 단어 시퀀스 최대 길이 : ', max(len(l) for l in sentences))
print('샘플 단어 시퀀스 평균 길이 : ', (sum(map(len, sentences))/len(sentences)))

# 토크나이저 정의
tag_tokenizer = preprocessing.text.Tokenizer(lower=False)  # 태그 정보는 소문자로 변환 안함
tag_tokenizer.fit_on_texts(tags)

# 단어 사전 및 태그 사전 크기
vocab_size = len(p.word_index) + 1
tag_size = len(tag_tokenizer.word_index) + 1
print('BIO 태그 사전 크기 : ', tag_size)
print('단어 사전 크기 : ', vocab_size)

# 학습용 단어 시퀀스 생성
x_train = [p.get_wordidx_sequence(sent) for sent in sentences]
y_train = tag_tokenizer.texts_to_sequences(tags)

index_to_ner = tag_tokenizer.index_word  # 시퀀스 인덱스를 NER로 변환하기 위해
index_to_ner[0] = 'PAD'

# 시퀀스 패딩 처리
max_len = 40
x_train = preprocessing.sequence.pad_sequences(x_train, padding='post', maxlen=max_len)