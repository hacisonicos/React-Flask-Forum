import React from "react";
import { useState, useEffect } from "react";
import CssBaseline from "@material-ui/core/CssBaseline";
import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import "./App.css";
import Navbar from "./components/navbar/navbar";
import News from "./components/News/news";

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
      <React.Fragment>
        <CssBaseline />
        <Container maxWidth="md">
          <Typography component="div">
            {newsData.map((news) => (
              <News
                title={newsData.length > 0 && news.title}
                url={newsData.length > 0 && news.image_url}
                alt={newsData.length > 0 && news.description}
                context={newsData.length > 0 && news.text}
              ></News>
            ))}
          </Typography>
        </Container>
      </React.Fragment>
    </div>
  );
}

export default App;
