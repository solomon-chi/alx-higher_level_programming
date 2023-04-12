#!/usr/bin/node
// Import the Rectangle class from 4-rectangle.js
const Rectangle = require('./4-rectangle');

// Define a Square class that extends the Rectangle class
class Square extends Rectangle {
  constructor (size) {
    // Call the super constructor with size as both width and height
    super(size, size);
  }
}

// Export the Square class for use in other files
module.exports = Square;

