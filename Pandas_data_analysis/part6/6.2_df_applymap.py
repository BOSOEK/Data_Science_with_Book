# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print('\n')

# 사용자 함수 정의
def add_10(n):   # 10을 더하는 함수
    return n + 10
    
# 데이터프레임에 applymap()으로 add_10() 함수를 매핑 적용
df_map = df.applymap(add_10)   
print(df_map.head())
