import React from 'react';
import Hero from "../components/Intro";
import Biography from "../components/Biography";
import MessageForm from "../components/MessageForm";
import Departments from "../components/Departments";
import Intro from '../components/Intro';

const Home = () => {
  return (
    <>
    <Intro title={"Welcome to KIPS LAB | Best Metallographic Software"} imageUrl={"/about_right.png"}/>
    <Biography imageUrl={"/about_right.png"} />
    <Departments />
    <MessageForm />
  </>
  )
}

export default Home
