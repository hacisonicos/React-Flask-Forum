import React from 'react';
import { Divider, Button, makeStyles } from '@material-ui/core';

import './news.css';

const useStyles = makeStyles((theme) => ({
    root: {
        marginLeft: "auto"
    },
  }));

function News(props) {
    const classes = useStyles();
    return(
        <div>
            <header className="News-header">
                <h1 className="News-title">{props.title}</h1>
                <img className="News-image"
                src={props.image_url}
                alt={props.alt}/>
                <p className="News-context">{props.context}</p>
            </header>
            <div className="News-button">
            <Button className={classes.root} color="primary" a href={props.url}>
                Haber detayına git!
            </Button>
            </div>
            <Divider/>
        </div>
    );
  }

  export default News;