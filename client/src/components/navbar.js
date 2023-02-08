import React from "react";

import { Link } from "react-router-dom";


const NavBar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark bg-body-tertiary">
            <div className="container-fluid">
                <Link className="navbar-brand" to="/">Recipe App </Link>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                <ul className="navbar-nav">
                    <li className="nav-item">
                    <Link className="nav-link active" to="/home">Home</Link>
                    </li>
                    <li className="nav-item">
                    <Link className="nav-link active" to="/signup">SignUp</Link>
                    </li>
                    <li className="nav-item">
                    <Link className="nav-link active" to="/login">Login</Link>
                    </li>
                    <li className="nav-item">
                    <Link className="nav-link active" to="/createRecipe">Create Recipe</Link>
                    </li>
                    <li className="nav-item">
                    <Link className="nav-link active" to="/">Log Out</Link>
                    </li>
                </ul>
                </div>
            </div>
        </nav>
    )
}

export default NavBar;