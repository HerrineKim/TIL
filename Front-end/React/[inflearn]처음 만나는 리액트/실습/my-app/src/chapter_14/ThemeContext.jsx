import React from "react";

// context의 초기값을 설정하지 않고 이후 provider에서 설정 예정
const ThemeContext = React.createContext();
// 개발자 도구로 Context의 이름 확인 가능
ThemeContext.displayName = "ThemeContext";

export default ThemeContext;