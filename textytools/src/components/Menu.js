import './Menu.css'
import 'animate.css';

import React,{useState} from 'react'

export default function Menu() {
const [text,settext]=useState('  ')
// const [text,settext]=useState('  ')
// const [text,settext]=useState('  ')

function handleOnchange(event){
    settext(event.target.value)
}
function handleUppercase(){
    settext(text.toUpperCase())
}
function handleLowercase(){
    settext(text.toLowerCase())
}
  return (
    <div id='main'>
      <div id="menu">

        <textarea id="txtarea" cols="30" rows="10" className="animate__animated animate__bounceIn" value={text} onChange={handleOnchange}></textarea>
        <div id="btnarea">
            <a id='btn' className='animate__animated' onClick={handleUppercase}>Upper Case</a>
            <a id='btn' className='animate__animated' onClick={handleLowercase}>Lower Case</a>
            <a id='btn' className='animate__animated'>tOgglE cAsE</a>
            <a id='btn' className='animate__animated'>Copy Text</a>
        </div>
      </div>
    </div>
  )
}
