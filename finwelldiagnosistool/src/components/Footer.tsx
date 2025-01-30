import React from "react";
import Link from "next/link";
import links from "@/data/FooterData";

const Footer = () => {
    return (
        <div className="flex flex-row w-full h-[5vw] bg-[#C6DEF1] items-center">
            {/* <Link
                href="/about"
                className="rounded-md w-[8%] ml-6 bg-[#595959] font-bold text-center text-[#FAF8F6] hover:scale-110"
            >
                Disclaimer
            </Link> */}
            <div className="absolute right-0 mr-6 flex gap-4">
                {links.map((link, index: number) => (
                    <Link
                        href={link.link}
                        key={index}
                        className="text-4xl text-[#FAF8F6] hover:scale-110"
                        target="_blank"
                    >
                        {link.icon}
                    </Link>
                ))}
            </div>
        </div>
    )
}

export default Footer;