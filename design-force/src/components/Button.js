import React from 'react';
import './Button.scss';

const Button = ({ className, text, clickHandler }) => {
  return (
    <button className={className} onClick={clickHandler}>
      {text}
    </button>
  );
};

export default Button;
