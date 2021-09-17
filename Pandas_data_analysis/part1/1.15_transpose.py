# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장 
exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print('\n')

# 데이터프레임 df를 전치하기 (메소드 활용)
df = df.transpose()
print(df)
print('\n')

# 데이터프레임 df를 다시 전치하기 (클래스 속성 활용)
df = df.T
print(df)