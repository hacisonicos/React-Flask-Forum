import React from "react";
import "./App.css";
import Navbar from "./components/navbar/navbar";
import News from "./components/News/news";
import { useState, useEffect } from "react";

function App() {
  const [newsData, setnewsData] = useState([]);

  useEffect(() => {
    fetch("/news")
      .then((res) => res.json())
      .then((data) => {
        setnewsData(data);
      });
  }, []);

  return (
    <div className="App">
      <Navbar />
      <header className="App-header">
        {newsData.map((news) => (
          <News
            title={newsData.length > 0 && news.title}
            url={newsData.length > 0 && news.url}
            alt={newsData.length > 0 && news.alt}
            context={newsData.length > 0 && news.context}
          ></News>
        ))}
      </header>
    </div>
  );
}

export default App;
