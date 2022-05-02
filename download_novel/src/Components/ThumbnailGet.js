import axios from 'axios'
import { useEffect } from 'react'
import { useState } from 'react'
const ThumbnailGet = ({novelName}) => {
    const [NovelThumbnail, setNovelThumbnail] = useState(" ")
    let FetchImages = () => {
        console.log(novelName)
        const imageName = `${novelName}.png`
        const requestOptions = {
            mode: 'no-cors',
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: novelName })
      
          };
        const url = `http://localhost:5000/fetchImage/${imageName}`
        fetch(url, requestOptions)  
            .then(res => {
                var imageUrl = URL.createObjectURL(res.data)
                setNovelThumbnail(imageUrl)
            })
    }
    useEffect(() => {
        FetchImages()

    }, [])

    return (
        <div>


            <div className="bg-cyan-300">
                <img className="object-scale-down h-48 w-96 ..." src={NovelThumbnail}></img>
            </div>

        </div>
    )   


}
export default ThumbnailGet; 