import React from "react";
import { Link } from "react-router-dom";
import { FaLocationArrow, FaPhone, FaWhatsapp } from "react-icons/fa6";
import { MdEmail } from "react-icons/md";

const Footer = () => {
const timings = [
    {
      id: 1,
      day: "Monday",
      time: "9:00 AM - 6:00 PM",
    },
    {
      id: 2,
      day: "Tuesday",
      time: "9:00 PM - 6:00 PM",
    },
    {  
      id: 3,
      day: "Wednesday",
      time: "9:00 PM - 6:00 PM",
    },
    {
      id: 4,
      day: "Thursday",
      time: "9:00 PM - 6:00 PM",
    },
    {
      id: 5,
      day: "Friday",
      time: "9:00 AM - 6:00 PM",
    },
    {
      id: 6,
      day: "Saturday",
      time: "9:00 AM - 3:00 PM",
    },
  ];

  return (
    <>
      <footer className={"container"}>
        <hr />
        <div className="content">
          <div>
            <img src="/kipsma.png" style={{height:"60px", width:"60px"}} alt="logo" className="logo-img"/>
          </div>
          <div>
            <h4>Quick Links</h4>
            <ul>
              <Link to={"/"}>Home</Link>
              <Link to={"/about"}>About Us</Link>
            </ul>
          </div>
          <div>
            <h4>Timings</h4>
            <ul>
              {timings.map((element) => (
                <li key={element.id}>
                  <span>{element.day}</span>
                  <span>{element.time}</span>
                </li>
              ))}
            </ul>
          </div>
          <div>
            <h4>Contact</h4>
            <div>
              <FaPhone />
              <span>+91 981-157-1224</span>
            </div>
            <div>
              <FaWhatsapp />
              <span>+91 965-086-5730</span>
            </div>
            <div>
              <MdEmail />
              <span>info@kipslabs.com</span>
            </div>
            <div>
              <FaLocationArrow />
              <span>India</span>
            </div>
          </div>
        </div>
      </footer>
    </>
  );
};

export default Footer;