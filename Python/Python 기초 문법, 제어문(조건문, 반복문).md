# Python 기초 문법

```
# 추가로 공부해볼 것

1. class, function, method?
```

> ## 변수와 객체

- 변수: 객체를 할당 할 수 있는 이름
  - 객체(object): 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것
  - 언제든 할당된 객체가 바뀔 수 있기 때문에 '변수'라고 불림
  - type(변수): 변수에 할당된 값의 타입
  - id(변수): 변수의 메모리주소* (*추후 배울 예정)

> ## 사용자 입력

- input(): 사용자로부터 값을 즉시 입력 받을 수 있는 내장함수

  반환값은 항상 문자열

> ## 주석

- 한 줄 주석: '#'

- 여러 줄의 주석

  한 줄씩 #을 사용하거나, """ 또는 '''으로 표현* (*docstring: 함수/클래스의 설명을 작성. 추후 배울 예정)



> ## 자료형
>
> Data - None / Boolean / Numeric / String - Int / Float / Complex

> ## 1. Boolean

- **False인 경우**

  0, 0.0, (), [], {}, '', None

> ## 2. Numeric

1. **Int(정수)**

   - 매우 큰 수를 나타낼 때 오버플로우(데이터 타입별로 사용할 수 있는 메모리의 크기를 넘어서는 상황)가 발생 X
   - Arbitrary precision arithmetic을 통해 고정된 형태의 메모리가 아닌 가용 메모리들을 활용하여 모든 수 표현에 활용
   - 진수 표현
     - 2진수: 0b
     - 8진수: 0o
     - 16진수: 0x

2. **Float(실수)**

   - 정수가 아닌 모든 실수는 float 타입

   - 부동소수점

     - 실수를 컴퓨터가 표현하는 방법. 2진수(비트)로 숫자를 표현

     - 이 과정에서 floating point rounding error가 발생. 값 비교하는 과정에서 주의

     - ```python
       # 2. system 상의 machine epsilon
       import sys
       print(abs(a - b) <= sys.float_info.epsilon)
       print(sys.float_info.epsilon)
       
       # 결과
       True
       2.220446049250313e-16
       
       # 3. Python 3.5이상
       import math
       math.isclose(a, b)
       
       # 결과
       True 
       ```

3. **Complex(복소수)**

   - 실수부와 허수부로 구성된 복소수는 모두 complex 타입

   - 허수부를 j로 표현

   - ```python
     a = 3 + 4j
     
     # 복소수의 실수부를 반환하는 method
     a. real
     # 결과
     3.0
     
     # 복소수의 허수부를 반환하는 method
     a.imag
     # 결과
     4.0
     ```

> ## 3. String

- **Immutable(변경불가능성)**

  그렇다면 mutable한 객체는? -> list, dict

- **Iterable(값을 한 개씩 순차적으로 접근이 가능하도록 만들 수 있다)**

- ```python
  a = '123'
  for char in a:
      print(char)
    
  # 결과
  1
  2
  3

- **삼중따옴표: 작은 따옴표나 큰 따옴표를 삼중으로 사용**

  따옴표 안에 따옴표를 넣을 때, 여러 줄을 나눠 입력할 때 편리

- **Escape sequence**

  \n 줄 바꿈

  \t 탭

  \r 캐리지리턴

  \0 널(null)

  \\` \

  \` ` 단일인용부호

  \"` 이중인용부호

- **String Interpolation(문자열 보간)**

  1. **%-formatting**

     ```python
     print('Hello, %s' % name)
     ```

  2. **str.format()**

     ```python
     print('Hello, {}! 성적은 {}'.format(name, score))
     ```

  3. **f-strings: python 3.6+**

     ```python
     print(f'Hello, {name}! 성적은 {score}')
     ```



> ## Container
>
> 여러 개의 값을 담을 수 있는 객체로, 서로 다른 자료형을 저장할 수 있다.
>
> ![A summary of Python's different container aspects.  ](Python%20%EA%B8%B0%EC%B4%88%20%EB%AC%B8%EB%B2%95,%20%EC%A0%9C%EC%96%B4%EB%AC%B8(%EC%A1%B0%EA%B1%B4%EB%AC%B8,%20%EB%B0%98%EB%B3%B5%EB%AC%B8).assets/A-summary-of-Pythons-different-container-aspects.png)

1. ### 시퀀스형 컨테이너 

   `모든 시퀀스형은 패킹/언패킹 연산자 '*'를 사용하여 객체의 패킹 또는 언패킹이 가능`

- **List**

  순서를 가지는 0개 이상의 객체 참조

  가변형

  []

  - 대괄호 혹은 list()를 통해 생성
  - 값에 대한 접근은 list[i]

- **Tuple**

  순서를 가지는 0개 이상의 객체 참조

  불변형

  ()

  단일 항목의 경우, 생성시 값 뒤에 쉼표를 붙여야 함

  ```python
  (1,)
  ```

  튜플 대입: 우변의 값을 좌변의 변수에 한 번에 할당

  ```python
  x, y = 1, 2
  print(x, y)
  
  1 2
  ```

- **Range**

  숫자의 시퀀스를 나타내기 위해 사용



2. ### 비시퀀스형 컨테이너

- **Set**

  순서없이 0개 이상의 immutable한 객체를 참조하는 자료형

  가변형

  수학에서의 집합과 동일: 중복과 순서가 없음

  {}, set() (*빈 set 만들기 위해서는 반드시 set())

  순서가 없어 별도의 값에 접근할 수 없음

  set을 사용하여 다른 종류의 컨테이너에서 중복된 값을 쉽게 제거할 수 있다. ex) set(my_list)

- **Dictionary**

  순서 없이 key-value 쌍으로 이뤄진 객체를 참조하는 자료형

  key: immutable한 불변자료형

  value: 어떠한 형태든 관계 없음

  {}, dict()

  key를 통해 value에 접근



> ## 연산자

- **set 연산자**

  `|` 합집합

  `&` 교집합

  `-` 여집합

  `^` 대칭차

- **연산자 우선 순위**

  `()`

  `Slicing`

  `Indexing`

  `**`

  `단항 연산자(+, -): 부호`

  `산술 연산자(*, /, %)`

  `산술 연산자(+, -)`

  `비교 연산자, in, is`

  `not`

  `and`

  `or`



> ## 컨테이너 형 변환
>
> <img src="Python%20%EA%B8%B0%EC%B4%88%20%EB%AC%B8%EB%B2%95,%20%EC%A0%9C%EC%96%B4%EB%AC%B8(%EC%A1%B0%EA%B1%B4%EB%AC%B8,%20%EB%B0%98%EB%B3%B5%EB%AC%B8).assets/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png" alt="https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png" style="zoom:50%;" />



> ## 파이썬 프로그램 구성 단위
>
> 1. **식별자(identifier)** 
>
>    변수, 함수, 클래스 등 프로그램이 실행되는 동안 다양한 값을 가질 수 있는 이름
>
> 2. **리터럴(literal)**
>
>    읽혀지는 대로 쓰여있는 값 그 자체
>
> 3. **표현식(expression)**
>
>    새로운 데이터 값을 생성하거나 계산하는 코드 조각
>
> 4. **문장(statement)**
>
>    특정한 작업을 수행하는 코드 전체
>
>    모든 표현식은 문장이다
>
> 5. **함수(function)**
>
>    특정 명령을 수행하는 함수 묶음
>
> 6. **모듈(module)**
>
>    함수/클래스의 모음 또는 하나의 프로그램을 구성하는 단위
>
> 7. **패키지(package)**
>
>    프로그램과 모듈 묶음
>
>    프로그램: 실행하기 위한 것
>
>    모듈: 다른 프로그램에서 불러와 사용하기 위한 것
>
> 8. **라이브러리(library)**
>
>    패키지 모음