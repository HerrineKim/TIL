import { setTasks, deleteTask } from './actions'
import reducer from './reducer'
import tasks from '../fixtures/tasks'

describe('reducer', () => {
  // 할 일 불러오기 함수
  describe('setTasks', () => {
    it('changes tasks array', () => {
      const state = reducer({
        tasks: [],
      }, setTasks(tasks))
      expect(state.tasks).not.toHaveLength(0)
    })
  })
  // 할 일 '완료' 버튼 눌러 삭제하기 함수
  describe('deleteTask', () => {
    it('removes the task from tasks', () => {
      const state = reducer({
        tasks: [
          { id: 1, title: '점심 메뉴 고민하기' },
        ],
      }, deleteTask(1))
      expect(state.tasks).toHaveLength(0)
    })
  })
})
