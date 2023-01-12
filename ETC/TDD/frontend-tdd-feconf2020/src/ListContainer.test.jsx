import reducer from './reducer';
import {
  setTasks,
  deleteTask,
} from './actions';
import tasks from '../fixtures/tasks';

// 상태 관리에 관한 것임
describe('reducer', () => {
  // 할 일 데이터 세팅
  describe('setTasks', () => {
    it('changes tasks array', () => {
      const initialState = {
        tasks: [],
      };

      const state = reducer(initialState, setTasks(tasks));

      expect(state.tasks).not.toHaveLength(0);
    });
  });
  // * 할 일 삭제(BDD)
  describe('deleteTask', () => {
    // * 행동 1: 삭제할 할 일 id가 존재하는 경우
    context('존재하는 ID의 할 일을 삭제 시도하려는 경우', () => {
      it('할 일 목록으로부터 해당 할 일을 삭제한다.', () => {
        const state = reducer({
          tasks: [
            { id: 1, title: 'Task' },
          ],
        }, deleteTask(1));
        // toHaveLength(): 배열의 길이를 체크
        expect(state.tasks).toHaveLength(0);
      });
    });
    // * 행동 2: 삭제할 할 일 id가 존재하지 않는 경우
    context('존재하지 않는 ID인 경우', () => {
      it("삭제 함수가 작동하지 않는다.", () => {
        const state = reducer({
          tasks: [
            { id: 1, title: 'Task' },
          ],
        }, deleteTask(100));

        expect(state.tasks).toHaveLength(1);
      });
    });
  });
});
