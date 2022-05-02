import ThumbnailGet from "./Components/ThumbnailGet.js";


let NovelPage = ({novelName}) => {



    return (

        <div className='flex h-screen' style={{ color: "white", backgroundColor: "black" }}>
            <div className='m-auto'>
                BIVEKASDA
                <ThumbnailGet novelName={novelName} />
            </div>

        </div>
    )
}
export default NovelPage;