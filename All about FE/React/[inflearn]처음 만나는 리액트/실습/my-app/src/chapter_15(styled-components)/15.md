# 상태와 관련된 대표적인 selector

:hover
- 마우스 커서가 element 위에 올라왔을 때

:active
- 주로 `<a></a>태그`에 사용되는데, element가 클릭됐을 때를 의미

:focus
- 주로 `<input>태그`에 사용되는데, element가 초점을 갖고 있을 경우를 의미

:checked
- radio button이나 checkbox 같은 유형의 `<input>태그`가 체크되어 있는 경우를 의미

:first-child, :last-child
- 상위 element를 기준으로 각각 첫 번째 child, 마지막 child일 경우를 의미

# display 속성

# visibility 속성

# position 속성

# flexbox

# font와 관련된 속성

## font-family 속성

## font-weight 속성

## font-style 속성

# 기타

## background-color

- CSS의 색상 값
1. 16진수 컬러 값: #ff0000
2. 투명도를 가진 16진수 컬러 값: #ff000055
3. RGB 컬러 값: rgb(255, 0, 0)
4. RGBA 컬러 값: rbga(255, 0, 0, 0.5)
5. HSL 컬러 값: hsl(120, 100%, 25%)
6. HSLA 컬러 값: hsla(120, 100%, 50%, 0.3)
7. 미리 정의된 색상의 이름: red
8. currentcolor 키워드: 현재 지정된 색상 값을 사용

# border 속성

# styled-components 설치 방법

- npm install --save styled-components

# 기본 사용법

## tagged template literal

- React가 이것을 사용하여 CSS가 적용된 컴포넌트를 만들어 준다.

## Props를 사용해 동적으로 구현 가능

```react
import React from "react";
import styled from "styled-components";

const Button = styled.button`
  color: ${props => props.dark ? "white" : "dark"};
  background: ${props => props.dark ? "black" : "white"};
  border: 1px solid black;
`;

<!-- styled-component를 확장하는 기본적인 방법 -->
const RoundedButton = styled(Button)`
  border-radius: 16px;
`;

function Sample(props) {
  return (
    <div>
      <Button>Normal</Button>
      <Button dark>Dark</Button> 
    </div>
  )
}

export default Sample;
```