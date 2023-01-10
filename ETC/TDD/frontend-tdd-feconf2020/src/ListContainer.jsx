import React from 'react'
import List from './List'
import { useSelector } from 'react-redux'

export default function ListContainer() {
  const { tasks } = useSelector((state) => ({
    tasks: state.tasks
  }))
  return (
    <List tasks={tasks} />
  )
}