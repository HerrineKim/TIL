import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { fireEvent, render } from '@testing-library/react'
import ListContainer from './ListContainer'
import tasks from '../fixtures/tasks'

jest.mock('react-redux')

describe('ListContainer', () => {
  const dispatch = jest.fn()
  useDispatch.mockImplementation(() => dispatch)
  useSelector.mockImplementation((selector) => selector({
    tasks,
  }))
  it('renders tasks', () => {
    const { container, getAllByText } = render((
      <ListContainer />
    ))
    expect(container).toHaveTextContent('고양이 사진 보기')
    
    const buttons = getAllByText('완료')

    fireEvent.click(buttons[0])

    expect(dispatch).toBeCalledWith({
      type: 'deleteTask',
      payload: { id: 1 },
    })
  })
})