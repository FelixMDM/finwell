import React from "react";

const page = () => {
    return (
        <div className="h-screen">
            <div className="flex flex-col ml-6 mt-[5%] space-y-12 text-4xl text-[#595959]">
                <div>
                    <p>
                       What is this? 
                    </p>
                    <ul className="text-lg mx-6 py-3">
                        <li>
                            This website is a tool intended for use within the Financial Wellness Program, for the purposes of filling out the intake form accurately and efficiently.
                            Provide intake form requests on the home page and receive guidance based on historical intake form data.
                        </li>
                    </ul>
                </div>
                <div>
                    <p>
                        Why does this exist?
                    </p>
                    <ul className="text-lg mx-6 py-3">
                        <li>
                            I understand how daunting of a task it can be to respond to intake form requests. Yes, it becomes easier with time; though, never straightforward.  
                            My goal is that after I am gone and unable to provide you with guidance, you have a resource to turn to apart from Yazleen, in the form of this website.
                        </li>
                    </ul>
                </div>
                <div>
                    <p>
                        Need more help?
                    </p>
                    <ul className="text-lg mx-6 py-3">
                        <li>
                            If you require additional assistance, reach out to either myself, or Yazleen on MS Teams.
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    )
}

export default page;