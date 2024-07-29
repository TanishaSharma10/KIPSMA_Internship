import React from 'react'
import Intro from '../components/Intro';
import Footer from '../components/Footer';
import MessageForm from '../components/MessageForm';

const Contact = () => {
   
  return (
    <>
      <Intro
      title={"Learn More About Us | Contact Us"}
      imageUrl={"/about.png"}
      />
      <h1>Whatsapp</h1>
      <MessageForm />
    </>
  )
}

export default Contact
