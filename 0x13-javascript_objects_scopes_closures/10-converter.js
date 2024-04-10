#!/usr/bin/node
/**
 * a script that defines a function to convert a number from base 10
 * to another base passed as argument
*/

// converts base to to any base except 16
const handleBaseExcept16 = (base, value) => {
  if (value >= base) {
    let bin = '';
    let result = 0;
    let rem = 0;
    do {
      result = parseInt(value / base);
      rem = value % base;
      bin += rem;
      value = result;
    } while (result >= base);
    bin = bin.split('').reverse().join(''); // reverse the value
    bin = result + bin;
    return (bin);
  } else {
    return (value);
  }
};

// converts base 10 to base 16
const handleBase16 = (value) => {
  if (value >= 0 && value <= 16) {
    return (hexChar(value));
  } else {
    let hex = '';
    let result = 0;
    let rem = 0;
    do {
      result = parseInt(value / 16);
      rem = value % 16;
      hex += hexChar(rem);
      value = result;
    } while (result > 16);
    hex = hex.split('').reverse().join(''); // reverse the value
    hex = hexChar(result) + hex;
    return (hex);
  }

  function hexChar (value) {
    if (value >= 0 && value <= 9) {
      return (value);
    } else if (value > 9 && value <= 15) {
      const letters = ['a', 'b', 'c', 'd', 'e', 'f'];
      return (letters[value - 10]);
    } else if (value === 16) {
      return (16);
    }
  }
};

exports.converter = function (base) {
  function toBase (value) {
    switch (base) {
      case 2:
      case 8:
        return (handleBaseExcept16(base, value));
      case 16:
        return (handleBase16(value));
      default:
        // assuming base 10
        return (value);
    }
  }

  return toBase;
};
