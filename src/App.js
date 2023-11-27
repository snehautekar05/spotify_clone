import React from 'react'
import Sidebar from './components/Sidebar'

function App() {
  return (
    <>
      <div className='flex h-[calc(100vh-theme(space.24))]'>
        <Sidebar/>
      </div>
    </>
  )
}

export default App