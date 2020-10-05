import React from "react";
import { useState, useEffect } from "react";
//material.ui
import { makeStyles } from '@material-ui/core/styles';
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import CssBaseline from "@material-ui/core/CssBaseline";
import Container from "@material-ui/core/Container";
import Pagination from '@material-ui/lab/Pagination';
//components
import News from "../components/News/news";

const useStyles = makeStyles((theme) => ({
  paginator: {
    justifyContent: "center",
    padding: "10px"
  }
}));

export default function App() {
  const classes = useStyles();
  const [newsData, setnewsData] = useState([]);

  useEffect(() => {
    fetch("/news/nation")
      .then((res) => res.json())
      .then((data) => {
        setnewsData(data);
      });
  }, []);

  const [page, setPage] = React.useState(1);
  const itemsPerPage = 10;
  const [noOfPages] = React.useState(
    Math.ceil(100 / itemsPerPage)
  );

   const handleChange = (event, value) => {
    setPage(value);
    window.scrollTo(0, 0);
  };

  return (
    <div>
      <Toolbar />
      <React.Fragment>
        <CssBaseline />
        <Container maxWidth="md">
          <Typography paragraph>
            {newsData.slice((page - 1) * itemsPerPage, page*itemsPerPage).map((news) => (
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
      <Pagination count={noOfPages} page={page} onChange={handleChange} showFirstButton showLastButton classes={{ul : classes.paginator}} />
    </div>
  );
}
