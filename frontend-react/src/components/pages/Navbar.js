import React from 'react';
import { Link } from 'react-router-dom';
function Navbar() {
  return (
    <div className="header">
      <nav>
            <div>
                <Link to="/" className="logo"><b>LOGO</b></Link>
            </div>
            <div className="nav-links" id="navLinks">
                {/* <i class="fa fa-times" onclick="hideMenu()"></i> */}
                <ul>
                    <span><li>Hello,</li></span>
                    <span><li>HELP</li></span>
                    <span><li>LOGOUT</li></span>
                </ul>
            </div>
            {/* <i className="fa fa-bars"onClick={showMenu}></i>        */}
        </nav>
    </div>
  )
}

export default Navbar
