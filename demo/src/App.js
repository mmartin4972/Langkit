import { useState } from 'react'
import axios from "axios";
import './App.css';

function App() {

   // new line start
  const [flashcardData, setFlashcardData] = useState(null)

  function getData() {
    axios({
      method: "GET",
      url:"/flashcards",
    })
    .then((response) => {
      const res =response.data
      setFlashcardData(({words: res.words}))
      console.log(res)
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}
    //end of new line 


  return (
    <div className="App">
        {/* new line start*/}
        <p>To get your profile details: </p>
          <button onClick={getData}>Click me</button>
          <div>{flashcardData.words}</div>
         {/* end of new line */}
    </div>
  );
}

export default App;