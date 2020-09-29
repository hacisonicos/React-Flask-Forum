import React from 'react';
import './navbar.css';
import { styled } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';

const MyButton = styled(Button)({
    height: 22,
    background: "#00adb5",
    border: 0,
    borderRadius: 3,
    marginLeft: 5,
    marginTop: 10,
    color: "#222831"
});

function Navbar() {
    return(
        <div className="Navbar">
            <header className="Navbar_header">
                <h1 className="Navbar_text">News Feed</h1>
                <form
                >
                    <input
                    className="Navbar_search"
                        type="text"
                        placeholder="Search"
                        />
                </form>
                <MyButton variant="contained"> Sign In</MyButton>
                <MyButton variant="contained"> Sign Up</MyButton>
            </header>
        </div>
    );
  }

  export default Navbar;