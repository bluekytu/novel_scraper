import Textbox from "./Components/TextBox.js";
import "./CSS/App.css"
import NovelPage from "./NovelPage.js";
import { useState } from "react";
import { BrowserRouter, Routes, Route } from 'react-router-dom'
function App() {
  const [NovelName, setNovelName] = useState("")
  const novelNameSubmitted = async (novelTitle) => {
    
    setNovelName()
  }

  return (

    <BrowserRouter>
      <Routes>
        <Route path="/novel" element={<NovelPage novelName={NovelName} />} />
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
