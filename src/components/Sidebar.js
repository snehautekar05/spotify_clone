import React from 'react'
import logo from '../img/logo.svg'
import Menu from './Sidebar/Menu'
import Playlist from './Sidebar/Playlist'

function Sidebar() {
  return (
<>
    <aside className='w-60 pt-6 flex flex-shrink-0 flex-col bg-black text-white'>
        <div className='mb-7 px-6'>
         <img src={logo} alt=''/>
        </div>
        <Menu/>
        <Playlist/>
    </aside>
</>
  )
}

export default Sidebar