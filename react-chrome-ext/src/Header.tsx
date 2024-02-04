// import React from 'react';
// import logo from './logo.svg';
// import './App.css';

type HeaderProps = {
    title: string
}

function Header(props: HeaderProps) {
    return (
        <h1>
            {props.title}
        </h1>
    );
}

export default Header;
