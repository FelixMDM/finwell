"use client";
import React from "react";
import { useState } from "react";

interface FormElements extends HTMLFormControlsCollection {
    comments: HTMLInputElement
}

interface CommentFormElement extends HTMLFormElement {
    readonly elements: FormElements
}

type response = {
    status: string,
    classification: string
}

const Tool = () => {
    const [comments, setComments] = useState("");
    const [classification, setClassification] = useState("");

    const logToServer = async (message: string) => {
        try {
            const response = await fetch('http://localhost:8080/inquiry', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    Inquiry: message
                })
            })

            const data: response = await response.json();
            setClassification(data.classification.toString());
        } catch (error) {
            console.error('Failed to send inquiry to server:', error);
        }
    };

    const handleSubmit = async (event: React.FormEvent<CommentFormElement>) => {
        event.preventDefault();
        const commentValue = event.currentTarget.elements.comments.value;
        await logToServer(commentValue);
    };

    return (
        <div className="flex flex-col vw-full h-screen justify-center items-center">
            <form onSubmit={handleSubmit}>
                <div className="flex flex-col">
                    <input
                        id="comments"
                        name="comments"
                        type="text"
                        value={comments}
                        onChange={(e) => setComments(e.target.value)}
                        className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                        placeholder="Enter your comments here"
                        required
                    />
                </div>
                <button
                    type="submit"   
                    className="w-full mt-[15%] py-1 bg-blue-600 rounded-md font-bold text-white"
                >
                    SUBMIT
                </button>
                <div>
                    {classification}
                </div>
            </form>
        </div>
    );
}

export default Tool;