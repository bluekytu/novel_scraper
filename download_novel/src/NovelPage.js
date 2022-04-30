import { useLocation } from "react-router-dom";


function novelPage() {

    const params = useLocation()


    return (

        <div>
            welcome {params}
        </div>
    )
}
export default novelPage;