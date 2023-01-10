// App.jsx에서 썼던 테스트 코드를 가져와서 List로 바꿔만 준다.
// 테스트 코드를 다 작성했으면 App.jsx를 복사해 List.jsx도 만든다.
import React from 'react';
import { render } from '@testing-library/react';
import List from './List';
import tasks from '../fixtures/tasks';

describe('List', () => {
  it('renders tasks', () => {
    // * container: 해당 컴포넌트의 최상위 DOM
    const { container } = render((
      <List
        tasks={tasks}
      />
    ));
    expect(container).toHaveTextContent('점심 메뉴 고민하기');
    expect(container).toHaveTextContent('고양이 사진 보기');
    // 두 개의 리스트 요소를 모두 작성했으면 최종적으로 App.jsx에 List를 사용할 수 있도록 import 해주러 가자.
  });
});
