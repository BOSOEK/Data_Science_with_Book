# -*- coding: utf-8 -*-

# 라이브러리 불러오기 
import pandas as pd

# 딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(student1)
print('\n')

# 학생의 과목별 점수를 200으로 나누기
percentage = student1 / 200

print(percentage)
print('\n')
print(type(percentage))