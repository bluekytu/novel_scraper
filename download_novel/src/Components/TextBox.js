import { useState } from "react";
const TextBox = ({ onSubmitNovelName }) => {
    const [NovelName, setNovelName] = useState(" ")
    let clickFunc = (e) => {
        e.preventDefault()
        onSubmitNovelName(NovelName)
        setNovelName(" ")
        
    }
    return (

            <div className="flex items-center border-b border-teal-500 py-2">
                <input className="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" placeholder="Enter Novel" aria-label="Full name" onChange={e => {setNovelName(e.target.value)}}></input>
                <button  className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded"onClick={(e) => {clickFunc(e)}} type="button">
                Submit
                </button>
            </div>

    )
        

}

export default TextBox;