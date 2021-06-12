# Deep_Learning_from_Scratch
> 밑바닥부터 시작하는 딥러닝

## 목록

### [1. 라이브러리](#1_딥러닝-라이브러리)
### [2. 퍼셉트론](#2_퍼셉트론(인공-뉴런/단순-퍼셉트론))
### [3. 신경망](https://github.com/BOSOEK/Study/blob/main/Book/Deep_Learning_from_Scratch/3%EC%9E%A5.%20%EC%8B%A0%EA%B2%BD%EB%A7%9D.ipynb)
### [4. 신경망 학습](#4_신경망-학습)
### [5. 오차역전파법](#5_오차역전파법)
### [6. 학습 관련 기술들](#6_학습-관련-기술들)
### [7. 합성곱 신경망(CNN)](#7_합성곱-신경망(CNN))
### [8. 딥러닝](#8_딥러닝)
### [9. 기타]()

***

## 1_딥러닝 라이브러리
* ### 넘파이(Numpy)
> 딥러닝 구현시 필요한 배열이나 행렬 계산을 넘파이의 배열 클래스 numpy.array의 메서드로 편하게 구현할 수 있다.
 ***
> ### 넘파이 배열 생성
> * 넘파이 배열 생성시에는 np.array() 메서드 사용하여 numpy.ndarray를 반환받는다
```
import numpy as np
x = np.array([1.0, 2.0, 3.0]) # [1., 2., 3.] 출력, 타입은 'numpy.ndarray'이다
```
> ### 넘파이 산술 연산
> * 넘파이 배열의 산술 연산은 각 원소에 대해서 행해진다(원소 수나 배열의 차원이 다르면 오류가 발생한다)
```
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
x + y # array([3.0, 6.0, 9.0])
```
> ### 넘파이 N차원 배열
> * 배열.shape : 각 차원의 크기를 보여줌
> * 배열.dtype : 배열의 타입 - **수학에서는 1차원 배열은 벡터(vector), 2차원 배열은 행렬(matrix), 벡터와 행렬을 일반화한 것을 텐서(tensor)라고 한다**
> ### 브로드 캐스트
> * 넘파이에서 형상(배열 수, 차원)이 다른 배열끼리의 계산 시 자동으로 형상을 맞춰 계산되는 기능을 __브로드 캐스트__라고 한다.
```
N = np.array([1, 2, 3, 4])
N * 10 # np.array([10, 20, 30, 40]) # 스칼라 값(수치 하나)인 10이 2X2로 확대됐다.
 
A = np.array([1, 2], [3, 4])
B = np.array([10, 20])
A * B # array([10, 40], [30, 80]) #B가 자동으로 2차원 배열 A와 똑같은 형상으로 변환됐다
```
> ### 원소 접근
> * 배열.flatten() : 배열을 1차원 배열로 변환(평탄화)
```
X = np.array([51, 55], [14, 19], [0, 4])
X.flatten() # [51, 55, 14, 19, 0, 4]
 
X[np.array([0, 2, 4])] # array([51, 55, 19]) # 인덱스가 0, 2, 4인 원소 얻기
```
* ### matplotlib
> 딥러닝 실험시 필요한 그래프와 데이터 시각화를 그려주는 라이브러리
***
> ### 그래프 그리기
> * 그래프는 matplotlib의 pyplot 모듈을 사용한다
```
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1) # 0~6까지 0.1 간격으로 생성
y = np.sin(x)

plt.plot(x, y) # 그래프 작성
plt.show() # 그래프 출력
```
> ### pyplot의 기능
```
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 그래프 그리기
plt.plot(x, y1, label="sin") #레이블에 'sin'이라고 표시
plt.plot(x, y2, linestyle="--", label="cos") # cos 함수는 점선으로 그리고 레이블에 'cos'이라고 표시
plt.xlabel("x") # x축 이름
plt.ylabel("y") # y축 이름
plt.title("sin & cos") # 제목
plt.legend()
plt.show()
```
> ### 이미지 표시
> * 이미지를 읽어들일 때는 matplotlib.image 모듈의 imread() 메서드를 사용하고 표시할때는 imshow()를 사용한다
```
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("이미지 경로")
plt.imshow(img)
plt.show()
```
***
## 2_퍼셉트론(인공 뉴런/단순 퍼셉트론)
> 퍼셉트론 알고리즘은 1957년 프랑크 로젠블라트가 고안한 신경망(딥러닝)의 기원이 되는 알고리즘으로 다수의 신호를 입력받아 하나의 신호를 출력하며 전류와 비슷하지만 퍼셉트론 신호는 흐른다(1)/안흐른다(0)의 두가지 값만 가진다.

![입력이2개인퍼셉트론](https://user-images.githubusercontent.com/68007145/104921566-d9ff5a80-59dc-11eb-8c38-f5f812dc8a45.png)
> * 위 그림은 2개의 신호를 받는 퍼셉트론이다
> * x는 입력신호 y는 출력신호 w(weight)는 가중치를 뜻한다
> * 그림의 원은 뉴런 혹은 노드라고 하며 입력 신호가 뉴런에 보내질 때는 각각의 가중치가 곱해지고 뉴런의 신호의 합이 정해진 한계를 넘을 때만 1을 출력한다(이를 뉴런이 활성화한다라고 표현)
> * 신호의 합이 넘어야 하는 한계를 __임계값__ 이라고 하며 θ(세타)로 나타낸다
> * 퍼셉트론의 동작 원리는 수식으로 다음와 같이 나타낸다.        
> ![ml2](https://user-images.githubusercontent.com/68007145/104923581-9528f300-59df-11eb-8397-aa9d01b1e5ba.png)          
> * #### 퍼셉트론은 복수의 입력 신호에 가중치를 부여하고 가중치는 각 신호가 결과에 주는 영향을 조절한다. 즉 __가중치가 클수록 해당 신호가 그만큼 중요함을 뜻__ 한다.

* ### 퍼셉트론 구현
> ### AND 게이트 구현
```
def AND(x1, x2):
  w1, w2, theta = 0.5, 0.5, 0.7
  tmp = x1*w1 + x2*w2
  if tmp <= theta:
   return 0
  elif tmp > theta:
   return 1
```
> 결과 : 매개변수 w1, w2, theta를 초기화 후 가중치를 곱한 입력 총합이 임계값을 넘으면 1을 반환, 그 외에는 0을 반환
```
AND(0, 0) #0을 출력
AND(1, 0) #0을 출력
AND(0, 1) #0을 출력
AND(1, 1) #1을 출력
```
> ### 가중치와 편향 도입
> * 기존의 퍼셉트론 동작 수식의 θ(세타)를 -b로 치환한다.              
> <img width="280" alt="다운로드" src="https://user-images.githubusercontent.com/68007145/105187381-11edd580-5b76-11eb-92bc-d6d523d584fb.png">      

> * 위 식에서의 b를 __편향(bias)__ 이라 하며 w는 그대로 가중치이다.
> * __편향__ 은 뉴런이 얼마나 쉽게 활성화(결과로 1을 출력) 하는가를 조정하는 매개변수이고, __가중치__ 는 각 입력 신호가 결과에 주는 영향력(중요도)를 조절하는 매개변수이다
> * 식을 해석하면 퍼셉트론은 입력 신호에 가중치를 곱한 값과 편향을 합하여 0을 넘으면 1을 출력, 아니면 0을 출력한다.
```
import numpy as np
x = np.array([0, 1])  #입력
w = np.array([0.5, 0.5])  #가중치
b = -0.7  # 편향
w*x  # array([0., 0.5])
np.sum(w*x)  #0.5
np.sum(w*x) + b  # -0.19999999996(대략 -0.2 - 부동소수점에 의한 연산 오차)
```
> ### 가중치와 편향을 도입한 AND, NAND, OR 게이트
```
def AND(x1, x2) :
 x = np.array([x1, x2])
 w = np.array([0.5, 0.5])
 b = -0.7
 tmp = np.sum(w*x) +b
 if tmp <= 0:
  return 0
 else :
  return 1

def NAND(x1, x2) :
 x = np.array([x1, x2])
 w = np.array([-0.5, -0.5])  #AND와는 가중치와 편향만 다르다
 b = 0.7
 tmp = np.sum(w*x) + b
 if tmp <= 0 :
  return 0
 else :
  return 1

def OR(x1, x2) :
 x = np.array([x1, x2])
 w = np.array([0.5, 0.5])  #가중치와 편향이 다르다
 b = -0.2
 tmp = np.sum(w*x) + b
 if tmp <= 0:
  return 0
 else :
  return 1
```
* ### 퍼셉트론의 한계
> * 퍼셉트론은 직선으로 나뉜 두 영역을 만들고 데이터를 분류하여 출력을 결정한다.     
<img width="493" alt="img (1)" src="https://user-images.githubusercontent.com/68007145/105360028-7aeb5100-5c3b-11eb-9a79-aab5ef235197.png">

> * 다만 XOR(베타적 논리합) 게이트는 직선 하나로는 영역을 나눌 수 없기에 __구현할 수 없다.__
> * #### 이처럼 퍼셉트론(단층퍼셉트론)은 직선 하나로 나눈 영역만 표현할 수 있다(비선형 영역을 분리할 수 없다)는 한계가 있다.
> * <선형 : 직선, 비선형 : 곡선>

* ### 다층 퍼셉트론 
> * 다층 퍼셉트론(층이 여러개인 퍼셉트론)을 사용해 XOR 게이트 구현  

```
def XOR(x1, x2):
 s1 = NAND(x1, x2)
 s2 = OR(x1, x2)
 y = AND(s1, s2)
 return y
 
 # 결과
 XOR(0, 0)  #0
 XOR(1, 0)  #1
 XOR(0, 1)  #1
 XOR(1, 1)  #0
```

***
