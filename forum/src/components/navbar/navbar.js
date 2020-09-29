import React from 'react';
import './navbar.css';
import { styled } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';

const MyButton = styled(Button)({
    height: 25,
    width: 140,
    background: "#00adb5",
    border: 0,
    borderRadius: 3,
    marginLeft: 5,
    color: "#222831",
    justifySelf: "center",
    alignSelf:"center"
});

const MySearch = styled(TextField)({
    marginRight: 1,
    marginLeft: 1,
    width: '300px',
    height: "40px",
    borderRadius: 3,
    background: "#00adb5",
    '& label.Mui-focused': {
        color: 'white',
      },
      '& .MuiInput-underline:after': {
        borderBottomColor: 'white',
      },
      '& .MuiOutlinedInput-root': {
        '& fieldset': {
          borderColor: '#222831',
        },
        '&.Mui-focused fieldset': {
          borderColor: 'white',
        },
      },
    },
);


function Navbar() {
    return(
        <div className="Navbar">
            <header className="Navbar_header">
                <h1 className="Navbar_text">News Feed</h1>
                <MySearch          
                    label="Search"
                    margin="dense"
                    variant="outlined"
                    type="search"
                    size="small"/>
                <MyButton variant="contained"> Sign In</MyButton>
                <MyButton variant="contained"> Sign Up</MyButton>
            </header>
        </div>
    );
  }

  export default Navbar;