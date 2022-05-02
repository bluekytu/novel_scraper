import Textbox from "./Components/TextBox.js";
import "./CSS/App.css"
import NovelPage from "./NovelPage.js";
import { BrowserRouter, Routes, Route } from 'react-router-dom'
function App() {
  const novelNameSubmitted = async (novelTitle) => {
    const requestOptions = {
      mode: 'no-cors',
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title: novelTitle })

    };
    fetch('http://127.0.0.1:5000/receiveNovelTitle', requestOptions)
      .then(res => {
        console.log("request sent!")
      })


  }

  return (

    <BrowserRouter>
      <Routes>
        <Route path="/novel" element={<NovelPage />} />
      </Routes>
      <div className="App">

        <div className="flex h-screen">
          <div className="m-auto">

            <Routes>
              <Route path="/" element={<Textbox onSubmitNovelName={(value) => novelNameSubmitted(value)} />} />
            </Routes>
          </div>
        </div>
      </div>

    </BrowserRouter>
  );
}

export default App;
