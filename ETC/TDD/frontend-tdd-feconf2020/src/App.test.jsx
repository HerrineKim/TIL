import React from 'react';
import { useSelector } from 'react-redux';
import { render } from '@testing-library/react';
import App from './App';
import tasks from '../fixtures/tasks';

jest.mock('react-redux');

// Import해 온 App 컴포넌트를 대상으로 어떤 컴포넌트를 사용할 지 작성한다.
describe('App', () => {
  useSelector.mockImplementation((selector) => selector({
    tasks,
  }))
  // 할 일 목록을 렌더링 한다.
  it('renders tasks', () => {
    // render()로 앱을 그린 다음 container를 가져 온다.
    const { container } = render((
      <App />
    ));
    // 우리가 기대하는 것은 container 안에 '아무 일도 하기 싫다'라는 글자가 보이는 것이다.
    expect(container).toHaveTextContent('고양이 사진 보기');
  });
});
// 테스트 주도 개발에서 원칙으로 제시하는 것은 이 테스트를 통과하는 코드를 최대한 빨리 작성하는 것이다.
// App.jsx로 고고!