#!/usr/bin/node

// Define the class Rectangle
class Rectangle {
  // Define the constructor that takes in two arguments
  constructor (width, height) {
    // Create a conditional statement that checks if width and height are both greater than zero
    if (width > 0 && height > 0) {
      // If the conditional statement is true, set the width and height properties of the Rectangle object
      this.width = width;
      this.height = height;
    }
  }

  // Define the print() method
  print () {
    // Use a for loop to iterate through each row of the Rectangle object
    for (let i = 0; i < this.height; i++) {
      // Print each row of the Rectangle object using console.log()
      console.log('X'.repeat(this.width));
    }
  }
}

// Export the Rectangle class so that it can be used in other files
module.exports = Rectangle;

