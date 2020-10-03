import React from 'react';
import { Divider, Typography } from '@material-ui/core';

import './news.css';

function News(props) {
    return(
        <div>
            <header className="News-header">
                <h1 className="News-title">{props.title}</h1>
                <img className="News-image"
                src={props.url}
                alt={props.alt}/>
                <p className="News-context">{props.context}</p>
            </header>
            <Divider/>
        </div>
    );
  }

  export default News;