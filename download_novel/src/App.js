import Textbox from "./Components/TextBox.js";
import "./CSS/App.css"
function App() {
  const AddNovel = () => {
    console.log("Submitted")
  }
  return (
    <div className="App">
  

      <div className="flex h-screen">
        <div className="m-auto">
          {<Textbox onAdd={AddNovel()} />}
        </div>
      </div>
    </div>
  );
}

export default App;
