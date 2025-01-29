import { Link } from "react-router-dom";


interface classification {
    result: string,
    status: string;
}

const Classification = ({ result, status }: classification) => {
    return (
        <div className="mt-[15%]">
            {status === "success" &&
                <div className="flex flex-col bg-green-400 rounded-md text-white p-2">
                    {result}
                </div>}
            {status === "error" &&
                <div className="flex flex-col bg-red-400 rounded-md text-white p-2">
                    {result}
                </div>}
        </div>
    );
}

export default Classification;