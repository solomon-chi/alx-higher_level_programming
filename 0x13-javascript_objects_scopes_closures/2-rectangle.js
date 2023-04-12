#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      // If either w or h is less than or equal to 0, create an empty object
      return {};
    } else {
      // Otherwise, initialize the instance attributes width and height with the given values
      this.width = w;
      this.height = h;
    }
  }
}
