# -*- coding: utf-8 -*-

import pandas as pd

# 투플을 시리즈로 변환(index 옵션에 인덱스 이름을 지정)
tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr)
print('\n')

# 원소를 1개 선택
print(sr[0])       # sr의 1 번째 원소를 선택 (정수형 위치 인덱스를 활용)
print(sr['이름'])  # '이름' 라벨을 가진 원소를 선택 (인덱스 이름을 활용)
print('\n')

# 여러 개의 원소를 선택 (인덱스 리스트 활용)
print(sr[[1, 2]]) 
print('\n')           
print(sr[['생년월일', '성별']])
print('\n')

# 여러 개의 원소를 선택 (인덱스 범위 지정)
print(sr[1 : 2])  
print('\n')              
print(sr['생년월일' : '성별'])
