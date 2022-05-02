import { useState } from "react";
const TextBox = ({ onSubmitNovelName }) => {
    const [NovelName, setNovelName] = useState(" ")



    let clickFunc = (e) => {
        e.preventDefault()
        window.location.href = "/novel"
        if (!NovelName) {
            alert("Please write down a novel's title!")
            return
        }
        onSubmitNovelName(NovelName)

        setNovelName(" ")

    }
    return (

        <div>

            <div className="flex items-center border-b border-teal-500 py-2 w-full">
                <input value={NovelName} className="appearance-none w-64 bg-transparent border-none w-full text-yellow-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" placeholder="Enter Novel" aria-label="Full name" onChange={e => { setNovelName(e.target.value) }}></input>
                <button type="button" className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded" onClick={(e) => clickFunc(e)}>
                    Submit









                </button>
            </div>
        </div>





    )


}

export default TextBox;