import { useState } from "react";
const TextBox = ({ onAdd }) => {
    const [NovelName, setNovelName] = useState(" ")
    let onSubmit = (e) => {
        
        if (!NovelName) {
            alert("Please enter a novel!")
            return
        }
        setNovelName("")
    }
    return (
            <form className="w-full max-w-sm" onSubmit={onSubmit()}>
                <input  type="submit"/>
            </form>

    )
        

}

export default TextBox;