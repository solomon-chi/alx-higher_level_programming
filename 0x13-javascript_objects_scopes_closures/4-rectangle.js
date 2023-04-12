#!/usr/bin/node

// Define the Rectangle class
class Rectangle {
  // Constructor method that takes in two arguments: width and height
  constructor (width, height) {
    // Only initialize the instance variables if width and height are both greater than 0
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  // Method that prints out the rectangle with "X"s
  print () {
    // Loop through the height of the rectangle
    for (let i = 0; i < this.height; i++) {
      // Print out a string of "X"s with a length equal to the width of the rectangle
      console.log('X'.repeat(this.width));
    }
  }

  // Method that rotates the rectangle by swapping the width and height
  rotate () {
    // Save the width in a temporary variable
    const temp = this.width;
    // Set the width to be equal to the height
    this.width = this.height;
    // Set the height to be equal to the temporary variable (i.e., the old width)
    this.height = temp;
  }

  // Method that doubles the width and height of the rectangle
  double () {
    // Multiply the width and height by 2
    this.width *= 2;
    this.height *= 2;
  }
}

// Export the Rectangle class
module.exports = Rectangle;
