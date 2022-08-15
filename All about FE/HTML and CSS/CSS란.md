# CSS(Cascading Style Sheets)

> 스타일을 지정하기 위한 언어

```markdown
- 선택자(Selector) - h1
- color: blue; - 선언(Declaration)
- font-size - 속성(Property)
- 15px - 값(Value)
```



- CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택한다.
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미.
  - 속성(Property): 어떤 스타일 기능을 변경할지 결정
  - 값(Value): 어떻게 스타일 기능을 변경할지 결정



### CSS 정의 방법

- 인라인
- 내부 참조 - <style>
- 외부 참조 - 분리된 CSS 파일



### CSS with 개발자 도구

- styles: 해당 요소에 선언된 모든 CSS
- computed: 해당 요소에 최종 계산된 CSS



## CSS Selectors

### 선택자 유형

- 기본 선택자
  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자
- 결합자(Combinators)
  - 자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자
- 의사 클래스/요소(Pseudo Class)
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자



### CSS 적용 우선순위(Cascading order)

- 중요도(importance) - 사용시 주의!
  - !important
- 우선 순위
  - 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
- CSS 파일 로딩 순서



### CSS 상속

https://developer.mozilla.org/ko/docs/Web/CSS/inheritance

> CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.

속성 중에서는 상속이 되는 것과 되지 않는 것이 있다/

- 상속 O
  - ex) Text 관련 요소, opacity, visibility 등
- 상속 X
  - ex) Box model 관련 요소, position 관련 요소 등



*심화

### 결합자(Combinators)

- 자손 결합자

  - selectorA 하위의 모든 selectorB 요소

  ```css
  div span {
      color: red;
  }
  ```

  ```html
  <div>
      <span>이건 빨강입니다.</span>
      <p>
          이건 빨강이 아닙니다.
      </p>
      <p>
          <span>이건 빨강입니다.</span>
      </p>
  </div>
  ```

  

- 자식 결합자

  - selectorA 바로 아래의 selectorB 요소

  ```css
  div > span {
      color: red;
  }
  ```

  ```html
  <div>
      <span>이건 빨강입니다.</span>
      <p>
          이건 빨강이 아닙니다.
      </p>
      <p>
          <span>이건 빨강이 아닙니다.</span>
      </p>
  </div>
  ```

  

- 일반 형제 결합자

  - selectorA의 형제 요소 중 뒤에 위치하는 selectorB 요소를 모두 선택

  ```css
  p ~ span {
      color: red;
  }
  ```

  ```html
  <span>p태그의 앞에 있기 때문에 이건 빨강이 아닙니다.</span>
  <p>
      여기 문단이 있습니다.
  </p>
  <b>그리고 코드도 있습니다.</b>
  <span>p태그와 형제이기 때문에 이건 빨강입니다!</span>
  <b>더 많은 코드가 있습니다.</b>
  <span>이것도 p태그와 형제이기 때문에 빨강입니다!</span>
  ```

  

- 인접 형제 결합자

  - selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택





## CSS 기본 스타일

### 크기 단위

- px(픽셀)
  - 모니터 해상도의 한 화소인 픽셀 기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
- %
  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용
- em
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
- viewport
  - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 화면)
  - 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
  - vw, vh, vmin, vmax



### 색상 단위

- 색상 키워드
  - 대소문자를 구분하지 않음
  - red, blue, black과 같은 특정 색을 직접 글자로 나타냄
- RGB 색상
  - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
- HSL 색상(Hue(색상), 채도(Saturation), 명도(Lightness))
  - 색상 채도, 명도를 통해 특정 색을 표현하는 방식
- 색상 키워드
- RGB 색상
  - '#' + 16진수 표기법
  - rgb() 함수형 표기법
- HSL 색상
  - 색상, 채도, 명도
- a는 alpha(투명도)



### CSS 문서 표현 - 추후 추가

- 텍스트
  - 서체, 서체 스타일
- 컬러, 배경



## CSS Box model

> CSS 원칙: 모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.(좌측 상단에 배치)



### Box model

- 모든 HTML 요소는 box 형태로 되어있다.
- 하나의 박스는 네 부분(영역)으로 이루어짐
  - content
  - padding
  - border
  - margin

![image-20220814215927750](CSS%EB%9E%80.assets/image-20220814215927750.png)

#### shorthand

![image-20220814220142594](CSS%EB%9E%80.assets/image-20220814220142594.png)



### box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box다.
  - padding을 제외한 순수 contents 영역만을 box로 지정한다.
- 다만 영역을 border까지로 넓히고 싶다면 box-sizing을 border-box로 설정하면 된다. 





## CSS Display

> CSS 원칙 2: display에 따라 크리와 배치가 달라진다. 

### 대표적으로 활용되는 display

*[블록 레벨 요소와 인라인 레벨 요소 구분은 HTML 4.1까지 적용. HTML 5부터는 다른 구분을 사용한다](https://developer.mozilla.org/ko/docs/Web/Guide/HTML/Content_categories)

#### 1. display: block

- 줄 바꿈이 일어나는 요소
- 화면 크기 전체의 가로 폭을 차지한다.
- 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있다.

- 대표적인 



#### 2. display: inline

- 줄 바꿈이 일어나지 않는 행의 일부 요소
- content 너비만큼 가로 폭을 차지한다.
- width, height, margin-top, margin-bottom을 지정할 수 없다.
- 상하 여백은 line-height로 지정한다.



#### 3. display: inline-block

- block과 inline 레벨 요소의 특징을 모두 가짐
- inline처럼 한 줄에 표시 가능하고, block처럼 width, height, margin 속성을 모두 지정할 수 있음



#### 4. display: none

- 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
- 이와 비슷한 visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.



#### 5. 이 외 다양한 display 속성

- https://developer.mozilla.org/ko/docs/Web/CSS/display



## CSS Position

### CSS position

- 문서 상에서 요소의 위치를 지정
- `static`: 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
  - `relative`: 상대 위치
    - 자기 자신의 static 위치를 기준으로 이동(normal flow 유지)
    - 레이아웃에서 요소가 차지하는 공간은 static 일 때와 같음(normal position 대비 offset)
  - `absolute`: 절대 위치
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
    - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 body)
    - 부모요소에 relative 설정 필수
  - `fixed`: 고정 위치
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
    - 부모 요소와 관계 없이 viewport를 기준으로 이동(스크롤 시에도 항상 같은 곳에 위치함)



## 참고

- [MDN web docs](https://developer.mozilla.org/ko/)
- [개발자 도구 활용법](https://developer.chrome.com/docs/devtools/css)
- Emmet
  - https://emmet.io/
  - https://docs.emmet.io/cheat-sheet/