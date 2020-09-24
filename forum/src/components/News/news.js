import React from 'react';

import './news.css';

function News(props) {
    return(
        <div className="News">
            <header className="News-header">
    <h1 className="News-title">{props.title}</h1>
            </header>
                <img className="News-image"
                src={props.url}
                alt={props.alt}/>
                <p className="News-context">{props.context}</p>
        </div>
    );
  }

  export default News;