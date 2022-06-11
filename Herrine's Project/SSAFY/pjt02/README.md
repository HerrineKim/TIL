# README

## 01. 정보

- JSON: JavaScript Object Notation. Javascript 객체 문법으로 구조화된 데이터를 표현하기 위한 문자 기반의 표준 포맷. 웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용.



> 파이썬을 활용한 데이터 수집

#### 정보 스크랩 1단계 - 요청

- 정보가 있는 사이트 URL을 확인한다.

- URL로 요청을 보낸다.

  ```python
  import requests
  from bs4 import BeautifulSoup
  
  url = 'https://naver.com'
  import requests
  response = requests.get(url).text
  # https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
  # response (200) : 성공적으로 가져왔다! 
  ```

- Beautifulsoup4 활용: text -> 다른 객체로 변환

- Beautifulsoup: HTML정보로 부터 원하는 데이터를 가져오기 쉽게, 비슷한 분류의 데이터별로 나누어주는(parsing) 파이썬 라이브러리 ( 보통 html정보를 가져오는 urllib.request.urlopen() 모듈과 함께 사용되곤 합니다 )

  ```python
  data = BeautifulSoup(response, 'html.parser')
  kospi = data.select_one('#KOSPI_now')  # 선택자 복사해올 것
  print(kospi.text)
  
  #<span>~</span>
  ```

- API(Application Programming Interface): 컴퓨터나 컴퓨터 프로그램 사이의 연결

  - 주소로 요청을 보내면, JSON 문서로 응답

    ```python
    URL = 'https://api.agify.io'
    params = {
        'name' : 'michael'
    }
    response = requests.get(URL, params=params).json()
    print(response.get('age'))
    
    # 70
    ```


- 요청해보기

  1. URL 및 요청변수 설정

     ```python
     BASE_URL = 'http://api.themoviedb.org/3
     path = '/movie/now_playing'
     params = {
         'api_key': '****'
         'region': 'KR',
         'language': 'ko'
     }
     
     # URL로 만들어보기: http://api.themoviedb.org/3/movie/now_playing?api_key=****&region=KR&language=ko
     ```

  2. 요청 보낸 결과 저장

     ```python
     response = requests.get(BASE_URL+path, params=params)
     ```

  3. 조작

     ```python
     print(response.status_code, response.url)
     data = response.json()
     ```

     

## Problem_a

> 문제 사항

1. requests를 이용하여 요청 보내는 기본적인 방법을 테스트 하는 문제

> 해결 방법

1. API 기본 사용법을 이용해 값을 불러오고, len() 함수를 이용해 값의 개수를 최종적으로 return 해주었다.

> 느낀점

- API를 사용하면 데이터의 다양한 활용이 가능하구나!



## Problem_b

> 문제 사항

1. 특정 value 값에 조건을 붙여 조건을 만족하는 값들만 새로운 리스트로 출력해야 한다.

> 해결 방법

1. 값을 불러온 다음, for-if문을 이용해 새로운 리스트에 append 해주었다.

> 느낀점

- 자료형에 따른 접근 방법을 잘 정리해보자



 ## Problem_c

> 문제 사항

1.  리스트 안의 딕셔너리들을 특정 value 값을 기준으로 내림차순으로 정렬한 후, 그 중 top 5를 새로운 리스트에 담아 출력해야 했다.

> 해결 방법

1. sorted(딕셔너리, key= lambda X: (-X[키 값])) (- 를 안 붙일 시 오름차순이 기본 형식이다.) 를 사용한 뒤 for-if문을 통해 index 0~4까지 새로운 리스트에 담아주면 끝! 

> 느낀점

- Googling is god...
- lambda 함수를 알차게 사용해보았다



## Problem_d

> 문제 사항

1. API를 두 가지 사용해서 최종적으로 입력값에 따라 다른 결과들을 출력하는 문제.

> 해결 방법

1. 두 개를 사용한다는 것 뿐  Problem_c와 거의 같은 문제라고 볼 수 있다. index를 잘 사용해 새로운 리스트에 append 하는 작업만 실수없이 하면 된다.
2. 경우를 나누어 언제 어떤 값이 출력되어야 하는지 잘 살펴 적절한 곳에 return 값을 넣어주었다.

> 느낀 점

- 긴 코드도 변수가 많아서 복잡해서 그렇지 차근차근 하면 기본적인 방법으로 모두 풀리는구나!



## Problem_e

> 문제 사항

1. 역시 두 개의 API를 사용해서 입력값에 따라 다른 결과들을 출력하는 문제.

> 해결 방법

1. Problem_d와 90% 동일한 문제로, 마지막에 배우와 감독을 각 리스트로 만든 후 새로운 딕셔너리로 만들어주는 과정을 추가해주었다.

> 느낀 점

- 동일한 방법으로 해결할 수 있는 문제를 알아보는 것이 중요하다!