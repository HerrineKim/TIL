import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import List from './List';

// * BDD 적용
// given - when - then 패턴

// given: 테스트에 필요한 상태를 설명한다.
// when: 테스트에 필요한 행동을 설명한다.
// then: 테스트 결과를 설명한다.

// describe: 테스트 대상은 List
// context: 테스트 대상이 놓인 상황(받을 파라미터 등)
// it: 테스트 대상이 수행하는 행동(함수 호출 등)
describe('List', () => {
  const handleClickDelete = jest.fn();
  // 테스트 코드 리팩토링: render() 함수 반복되니 하나의 함수로 묶기
  function renderList(tasks) {
    return render((
      <List
        tasks={tasks}
        onClickDelete={handleClickDelete}
      />
    ));
  }
  // * 행동 1: tasks 有
  context('with tasks', () => {
    const tasks = [
      { id: 1, title: '고양이 사진 보기' },
      { id: 2, title: '점심 메뉴 고민하기' },
    ];

    it('renders tasks', () => {
      const { getByText } = renderList(tasks);
      // toBeNull(): null인지 체크
      expect(getByText(/점심 메뉴 고민하기/)).not.toBeNull();
    });

    it('renders "완료" button to delete a task', () => {
      const { getAllByText } = renderList(tasks);
      // 버튼 다 가져와!
      const buttons = getAllByText('완료');
      // 첫 번째 버튼만 눌러 봐!
      fireEvent.click(buttons[0]);
      // 함수 한 번 실행 될 거야.
      expect(handleClickDelete).toBeCalledWith(1);
    });
  });
  // * 행동 2: tasks 無
  context('without tasks', () => {
    it('render no tasks message', () => {
      // 빈 데이터일 때
      const tasks = [];
      const { getByText } = renderList(tasks);
      // 기본값으로 '할 일이 없어요!!!!'와 같은 말을 넣어 놓자.
      // 그리고 그건 절대 없으면 안되는 거니까 .not.toBeNull()로 null값인지 체크!
      expect(getByText(/할 일이 없어요/)).not.toBeNull();
    });
  });
});
