# -*- coding: utf-8 -*-

import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 평균값 
print(df.mean())
print('\n')
print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
print(df[['mpg','weight']].mean())

# 중간값 
print(df.median())
print('\n')
print(df['mpg'].median())

# 최대값 
print(df.max())
print('\n')
print(df['mpg'].max())

# 최소값 
print(df.min())
print('\n')
print(df['mpg'].min())

# 표준편차 
print(df.std())
print('\n')
print(df['mpg'].std())

# 상관계수 
print(df.corr())
print('\n')
print(df[['mpg','weight']].corr())