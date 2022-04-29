import Textbox from "./Components/TextBox.js";
import "./CSS/App.css"
function App() {
  const novelNameSubmitted = (novelTitle) => {
    console.log(novelTitle)
  }
  return (
    <div className="App">
      <div className="flex h-screen">
        <div className="m-auto">
          <Textbox  onSubmitNovelName={e => {novelNameSubmitted()}}/>
        </div>
      </div>
    </div>
  );
}

export default App;
