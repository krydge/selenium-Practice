import logo from './logo.svg';
import './App.css';
import {useState,  useEffect } from 'react'


function App() {

  const [data,setData] = useState('')

useEffect( async ()=>{
  async function fetchData(){
    let responce = await fetch("https://www.google.com")
  }
  fetchData()
  console.log("useEffect")
 
},[])
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
