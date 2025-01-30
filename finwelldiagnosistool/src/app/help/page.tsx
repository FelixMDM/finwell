import React from "react";

const page = () => {
    return (
        <div className="h-screen">
            <div className="flex flex-col ml-6 mt-[5%] space-y-12 text-4xl text-[#595959]">
                <div>
                    <p>
                       How does this work?
                    </p>
                    <ul className="text-lg mx-6 py-3">
                        <li>
                            Located on the home page is a text box. Copy paste difficult intake form requests here. 
                            Requests are sent to the server and fed through a machine-learning model trained on historical intake form results. 
                            Finally, hit submit to view results.
                        </li>
                    </ul>
                </div>
                <div>
                    <p>
                        How accurate is this?
                    </p>
                    <ul className="text-lg mx-6 py-3">
                        <li>
                            As of writing this blurb, this model returns a weighted average precision score of 78%, and a macro average of 84%. 
                            That is to say, based on the training data I&apos;ve supplied the model with, you can confidently expect the model to determine the correct course of action around 81% of the time.
                        </li>
                    </ul>
                </div>
                <div>
                    <p>
                        Disclaimer
                    </p>
                    <ul className="text-lg mx-6 py-3">
                        <li>
                            Please note that the handling of intake form requests is an involved process that requires context and training far beyond what I&apos;ve implemented in the model seen here. 
                            Given the nuanced nature of the requests we receive on the intake form, it is entirely possible that we are able to take on appointments that my algorithm would otherwise have you reject.
                            Conequently, I encourage you to interpret the results returned by this tool as more of a guiding hand in the case of uncertainty rather than as an infallible fact  .
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    )
}

export default page;