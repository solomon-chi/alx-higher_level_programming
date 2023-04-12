#!/usr/bin/node

// Require the Square class from the 5-square.js file
const SquareBase = require('./5-square');

// Create a new class Square that extends the SquareBase class
class Square extends SquareBase {
  // Define a new method charPrint with a default parameter of 'X'
  charPrint (c = 'X') {
    // Loop through each row of the square and print out 'c' repeated 'this.width' times
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

// Export the Square class for use in other files
module.exports = Square;
