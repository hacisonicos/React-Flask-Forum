import React from "react";
import { useState, useEffect } from "react";
//material.ui
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import CssBaseline from "@material-ui/core/CssBaseline";
import Container from "@material-ui/core/Container";
import News from "../components/News/news";

export default function App() {
  const [newsData, setnewsData] = useState([]);

  useEffect(() => {
    fetch("/news/business")
      .then((res) => res.json())
      .then((data) => {
        setnewsData(data);
      });
  }, []);

  return (
    <div>
      <Toolbar />
      <React.Fragment>
        <CssBaseline />
        <Container maxWidth="md">
          <Typography paragraph>
            {newsData.map((news) => (
              <News
                title={newsData.length > 0 && news.title}
                url={newsData.length > 0 && news.image_url}
                alt={newsData.length > 0 && news.description}
                context={newsData.length > 0 && news.description}
              ></News>
            ))}
          </Typography>
        </Container>
      </React.Fragment>
    </div>
  );
}
