import React from 'react';
import './navbar.css';

function Navbar() {
    return(
        <div className="Navbar">
            <header className="Navbar_header">
                <h1 className="Navbar_text">Forum</h1>
                <form
                >
                    <input
                    className="Navbar_search"
                        type="text"
                        placeholder="Search"
                        />
                </form>
                <button className="Navbar_button">Sign In</button>
                <button className="Navbar_button">Sign Up</button>
            </header>
        </div>
    );
  }

  export default Navbar;