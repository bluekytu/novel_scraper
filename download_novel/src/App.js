import Textbox from "./Components/TextBox.js";
import "./CSS/App.css"
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
    <div className="App">
      <div className="flex h-screen">
        <div className="m-auto">
         {<Textbox  onSubmitNovelName={(value) => novelNameSubmitted(value)}/>}
        </div>
      </div>
    </div>
  );
}

export default App;
