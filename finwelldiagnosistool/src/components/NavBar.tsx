import React from "react";
import Link from "next/link";

const NavBar = () => {
    return (
        <div className="flex flex-row w-full text-[#595959]">
            <div className="flex flex-col ml-6 items-left">
                <Link
                    href="/"
                    className="text-6xl py-3 hover:opacity-50"
                >
                    Finwell Diagnosis Tool
                </Link>
                <Link
                    href="/about"
                    className="text-2xl hover:opacity-50"
                >
                    About
                </Link>
                <Link
                    href="/help"
                    className="text-2xl hover:opacity-50"
                >
                    Help
                </Link>
            </div>
        </div>
    )
}

export default NavBar;