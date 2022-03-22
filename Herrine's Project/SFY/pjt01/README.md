# README

- 2022년 3월 22일 수정(느낀점 추가 예정)



## 0. 정보: 파이썬을 활용한 데이터 수집 I

> 파일 입력

- open(file, mode='r', encoding=None)
  - file: 파일명
  - mode: 텍스트 모드
  - encoding: 인코딩 방식(일반적으로 utf-8 활용)'



> 파일 입력 활용법

- with 키워드 활용

  ```python
  with open('workfile') as f:
      read_data = f.read()
  f.closed
  True
  ```

- 파일 객체 활용

  ```python
  f = open('workfile', 'w')
  ```



> JSON(JavaScript Object Notation)

- 자바스크립트 객체 표기법. 웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용함
- 문자 기반(텍스트) 데이터 포맷으로 다수의 프로그래밍 환경에서 쉽게 활용 가능함



> JSON 파일의 활용

- 객체(리스트, 딕셔너리 등)를 JSON으로 변환

- JSON을 객체로 변환

  ```python
  x = json.load(f)
  ```



> 딕셔너리 접근 방법

- dict.get(key, default)

  ```python
  for stock in stocks:
      print(stock.get('price', '비상장주식'))
  # 디폴트 값이 없다면 'None'
  ```

  

## problem_a.py

특정 영화의 특정 값들만 보기 위해서 movie.json 파일의 데이터에서 필요한 value 값들을 가져와 새로운 dictionary로 만들어주었습니다.

## problem_b.py

특정 값을 교체해주기 위해서 새로운 list를 만들었습니다.

## problem_c.py 

movies 파일의 여러 영화들에 동일한 작업을 해주었습니다.