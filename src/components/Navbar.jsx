import logo from '../logo.svg';
import "./Navbar.css"
import { Link } from "react-router-dom";

const Navbar = () => {
    return ( 
        <nav className="navbar">
            <div className="navbar-logo">
                <img src={logo} className="App-logo" alt="logo" />
            </div>
            <div className="navbar-menu">
                <Link to="/" className="navbar-menu-item">Home</Link>
                <Link to="/about" className="navbar-menu-item">About</Link>
                <Link to="/contact" className="navbar-menu-item">Services</Link>
                <Link to="/portfolio" className="navbar-menu-item">Contact</Link>
            </div>
        </nav>
     );
}
 
export default Navbar;