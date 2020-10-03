import React from 'react';
//navigation
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
//material.ui
import { makeStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import CssBaseline from '@material-ui/core/CssBaseline';
import "./App.css";
//pages
import Home from "./topic/Home";
import World from "./topic/World";
import Nation from "./topic/Nation";
import Business from "./topic/Business";
import Technology from "./topic/Technology";
import Entertainment from "./topic/Entertainment";
import Science from "./topic/Science";
import Sports from "./topic/Sports";
import Health from "./topic/Health";

const drawerWidth = 200;

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
  },
  drawer: {
    width: drawerWidth,
    flexShrink: 0,
  },
  drawerPaper: {
    width: drawerWidth,
  },
  drawerContainer: {
    overflow: 'auto',
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
  },
  link:{
    textDecoration: 'none',
    color: theme.palette.text.primary
  }
}));

export default function App() {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <CssBaseline />
      <AppBar position="fixed" className={classes.appBar}>
        <Toolbar>
          <Typography variant="h6" noWrap>
            Haber Akışı
          </Typography>
        </Toolbar>
      </AppBar>
      <Router>
      <Drawer
        className={classes.drawer}
        variant="permanent"
        classes={{
          paper: classes.drawerPaper,
        }}
      >
        <Toolbar />
        <div className={classes.drawerContainer}>
          <List>
            <Link to="/" className={classes.link}>
              <ListItem button key="Home">
                <ListItemText primary="Anasayfa"/>
              </ListItem>
            </Link>
            <Link to="/world" className={classes.link}>
              <ListItem button key="World">
                <ListItemText primary="Dünya"/>
              </ListItem>
            </Link>
            <Link to="/nation" className={classes.link}>
              <ListItem button key="Nation">
                <ListItemText primary="Ulusal"/>
              </ListItem>
            </Link>
            <Link to="/business" className={classes.link}>
              <ListItem button key="Business">
                <ListItemText primary="Ekonomi"/>
              </ListItem>
            </Link>
            <Link to="/technology" className={classes.link}>
              <ListItem button key="Technology">
                <ListItemText primary="Teknoloji"/>
              </ListItem>
            </Link>
            <Link to="/entertainment" className={classes.link}>
              <ListItem button key="Entertainment">
                <ListItemText primary="Magazin"/>
              </ListItem>
            </Link>
            <Link to="/science" className={classes.link}>
              <ListItem button key="Science">
                <ListItemText primary="Bilim"/>
              </ListItem>
            </Link>
            <Link to="/sports" className={classes.link}>
              <ListItem button key="Sports">
                <ListItemText primary="Spor"/>
              </ListItem>
            </Link>
            <Link to="/health" className={classes.link}>
              <ListItem button key="Health">
                <ListItemText primary="Sağlık"/>
              </ListItem>
            </Link>
          </List>
        </div>
      </Drawer>
      <main className={classes.content}>
        <Switch>
          <Route exact path="/">
            <Home/>
          </Route>
          <Route exact path="/world">
            <World/>
          </Route>
          <Route exact path="/nation">
            <Nation/>
          </Route>
          <Route exact path="/business">
            <Business/>
          </Route>
          <Route exact path="/technology">
            <Technology/>
          </Route>
          <Route exact path="/entertainment">
            <Entertainment/>
          </Route>
          <Route exact path="/science">
            <Science/>
          </Route>
          <Route exact path="/sports">
            <Sports/>
          </Route>
          <Route exact path="/health">
            <Health/>
          </Route>
        </Switch>
      </main>
      </Router>
    </div>
  );
}