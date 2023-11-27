import React from 'react'

function Playlist() {
  return (
    <>
        <nav className='mx-6 mt-2 py-2 flex-auto border-t border-white border-opacity-20 overflow-y-auto'>
            <ul>
               {new Array(50).fill().map((_,index)=>(
                <li key={index}>
                  <div className='text-sm text-gray-500 hover:text-white flex items-center'>
                    My Playlist
                  </div>
                </li>
               ))}
            </ul>
        </nav>
    </>
  )
}

export default Playlist