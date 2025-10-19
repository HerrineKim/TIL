# HTML이란

## 1. Markup Language

- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
- 대표적인 예 - HTML, Markdown



## 2. HTML

웹 페이지를 작성(구조화)하기 위한 언어



## 3. HTML 기본 구조

```html
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
    </head>
</html>
<body>
    
</body>
</html>
```

- html: 문서의 최상위(root) 요소

- head: 문서 메타데이터(데이터를 설명해주는 데이터) 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- body: 문서 본문 요소
  - 실제 화면 구성과 관련된 내용



> 요소(element)

태그와 내용(`<h1>안녕, 난 혜린이야</h1>`)

- 내용이 없는 태그들
  - br, hr, img, input, link, meta
- 요소는 중첩될 수 있다.



> 속성(attribute)

속성을 통해 태그의 부가적인 정보를 설정한다. 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재한다.

- `href`: 속성명
- `"https://google.com"`: 속성값
- 태그 별로 사용할 수 있는 속성은 다르다.
- 속성 작성 방식은 통일해야 한다(공백, 따옴표 등)



*HTML Global Attribute(태그 종류에 관계 없이 사용 가능한 속성들)

- `id`: 문서 전체에서 유일한 고유 식별자 지정
- `class`: 공백으로 구분된 해당 요소의 클래스의 목록(CSS, JS에서 요소를 선택하거나 접근)
- `data-*`: 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
- `style`: inline 스타일
- `title`: 요소에 대한 추가 정보 지정
- `tabindex`: 요소의 탭 순서



### 시맨틱 태그

- HTML에서 의미론적 요소를 담은 태그가 등장해, 기존 영역을 의미하는 div 태그를 대체하여 사용한다.
- 대표적인 태그 목록은 이렇다.
  - `header`: 문서 전체나 섹션의 헤더(머리말 부분)
  - `nav`: 내비게이션
  - `aside`: 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
  - `section`: 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
  - `article`: 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - `footer`: 문서 전체나 섹션의 푸터(마지막 부분)

 

> 시맨틱 태그의 목적

- 개발자 및 사용자 뿐만 아니라 검색 엔진 등에 의미 있는 정보의 그룹을 태그로 표현한다.
- 단순히 구역을 나누는 것 뿐만 아니라 '의미'를 가지는 태그들을 활용하기 위한 노력
- 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 한다.
- 검색엔진최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용해야 한다.



## 4. HTML 문서 구조화

### 인라인, 블록 요소



### 텍스트 요소

| 태그                           | 설명                                                         |
| ------------------------------ | ------------------------------------------------------------ |
| `<a></a>`                      | href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성     |
| `<b></b>`, `<strong></strong>` | 굵은 글씨 요소, 중요한 강조하고자 하는 요소(보통 굵은 글씨로 표현) - 의미론적 차이! |
| `<i></i>`, `<em></em>`         | 기울임 글씨 요소, 중요한 강조하고자 하는 요소(보통 기울임 글씨로 표현) |
| `<br>`                         | 텍스트 내에 줄 바꿈 생성                                     |
| `<img>`                        | src 속성을 활용하여 이미지 표현                              |
| `<span></span>`                | 의미 없는 인라인 컨테이너                                    |



### 그룹 컨텐츠

| 태그                        | 설명                                                         |
| --------------------------- | ------------------------------------------------------------ |
| `<p></p>`                   | 하나의 문단(paragraph)                                       |
| `<hr>`                      | 문단 레벨 요소에서의 주제의 분리를 의미하여 수평선으로 표현됨 |
| `<ol></ol>`, `<ul></ul>`    | 순서가 있는 리스트, 순서가 없는 리스트                       |
| `<pre></pre>`               | HTML에 작성한 내용을 그대로 표현. 보통 고정폭 글꼴이 사용되고 공백 문자를 유지 |
| `<blockquote></blockquote>` | 텍스트가 긴 인용문. 주로 들여쓰기를 한 것으로 표현됨         |
| `<div></div>`               | 의미 없는 블록 레벨 컨테이너                                 |



### table

![img](HTML%EC%9D%B4%EB%9E%80.assets/%ED%85%8C%EC%9D%B4%EB%B8%942_html_20180416_181513.jpg)

```html

<table border="1">
<caption> 방과 후 종목 별 신청자 수 </caption>
<thead>
<tr>
<th>종목</th>
<th>축구</th>
<th>배드민턴</th>
<th>수영</th>
</tr>
</thead>
<tfoot>
<tr>
<td>합계</td>
<td>40명</td>
<td>51명</td>
<td>26명</td>
</tr>
</tfoot>
<tbody>
<tr>
<td>1학년</td>
<td>15명</td>
<td>30명</td>
<td>10명</td>
</tr>
<tr>
<td>2학년</td>
<td>15명</td>
<td>11명</td>
<td>10명</td>
</tr>
<tr>
<td>3학년</td>
<td>10명</td>
<td>10명</td>
<td>6명</td>
</tr>

</tbody>


</table>
```



### form

- `<form>`은 정보(데이터)를 서버에 제출하기 위한 영역이다.



#### form 기본 속성

- action: form을 처리할 서버의 URL
- method: form을 제출할 때 사용할 HTTP 메서드(GET 혹은 POST)
- enctype: method가 post인 경우 데이터의 유형
  - application/x-www-form-urlencoded: 기본값
  - multipart/form-data: 파일 전송시(input type이 file인 경우)



### input

- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공된다.



#### `<input>`의 대표적인 속성

- name: form control에 적용되는 이름(이름/값 페어로 전송됨)
- value: form control에 적용되는 값(이름/값 페어로 전송됨)
- required, readonly, autofocus, autocomplete, disabled 등



#### input label

- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
  - 사용자는 선택할 수 있는 영역이 늘어나 웹/모바일(터치) 환경에서 편하게 사용할 수 있음
  - label과 input 입력의 관계가 시각적 뿐만 아니라 화면 리더기에서도 label을 읽어 쉽게 내용을 확인할 수 있도록 함
- `<input>`에 id 속성을, `<label>`에는 for 속성을 활용하여 상호 연관을 시킴

```html
<label for="agreement">개인정보 수집에 동의합니다.</label>
<input type="checkbox" name="agreement" id="agreement">
```



#### input 유형 - 일반

- 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML 기본 검증 혹은 추가 속성을 활용할 수 있음
  - text: 일반 텍스트 입력
  - password:  입력 시 갑싱 보이지 않고 문자를 특수기호(*)로 표현
  - email: 이메일 형식이 아닌 경우 form 제출 불가
  - number: min, max, step 속성을 활용하여 숫자 범위 설정 가능
  - file: accept 속성을 활용하여 파일 타입 지정 가능



#### input 유형 - 항목 중 선택

![File:Radiobutton checkbox.png - Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/e/e4/Radiobutton_checkbox.png)

- 일반적으로 label을 사용하여 내용을 작성하여 항목 중 선택할 수 있는 input을 제공
- 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value를 지정해야 함
  - checkbox: 다중 선택
  - radio: 단일 선택



#### input 유형 - 기타

- 다양한 종류의 input을 위한 picker를 제공
  - color: color picker
  - date: date picker
- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
  - hidden: 사용자에게 보이지 않는 input



#### input 유형 - 종합

- `<input>` 요소의 동작은 type에 따라 달라지므로, 각각의 내용을 숙지할 것.

