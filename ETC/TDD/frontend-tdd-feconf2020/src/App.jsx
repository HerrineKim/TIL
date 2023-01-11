import React, { useEffect } from 'react'
import { useDispatch } from 'react-redux'
import ListContainer from './ListContainer'
import { setTasks } from './actions'
import tasks from '../fixtures/tasks'


export default function App() {
  // 액션 보내주기
  const dispatch = useDispatch()
  // 앱 컴포넌트가 그려질 때 초기 데이터를 주기
  useEffect(() => {
    dispatch(setTasks(tasks))
  }, [])
  // 데이터도 여기로 가져와서 직접 전달해준다.
  return (
    <div>
      <h1>To-do</h1>
      {/* ListContainer 하위에 List 컴포넌트를 넣어 관심사 분리 */}
      <ListContainer />
    </div>
  );
}
