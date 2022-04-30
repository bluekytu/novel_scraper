import axios from 'axios'
const thumbnailGet = (novelName) => {
    const [novelThumbnail, setnovelThumbnail] = useState(second)

    let fetchImages = () => {
        const imageName = `${novelName}.png`
        const url = `http://localhost:5000/fetchImage/${imageName}`
        axios.get(url, { responseType: 'blob' })
            .then(res => {
                var imageUrl = URL.createObjectURL(res.data)
                setnovelThumbnail(imageUrl)
            })
    }
    useEffect(() => {
        fetchImages()

    }, [])

    return (
        <div>


            <div class="bg-cyan-300">
                <img class="object-scale-down h-48 w-96 ..." src={novelThumbnail}></img>
            </div>

        </div>
    )


}
export default thumbnailGet; 