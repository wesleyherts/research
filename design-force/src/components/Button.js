import React from 'react';
import './Button.css';

const Button = ({ text, clickHandler }) => {
  return (
    <button className="button" onClick={clickHandler}>
      {text}
    </button>
  );
};

export default Button;
