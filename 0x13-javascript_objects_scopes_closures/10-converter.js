#!/usr/bin/node

// Define and export a function called converter that takes a single parameter called base
exports.converter = function (base) {
  // Return an anonymous function that takes a single parameter called n
  return function (n) {
    // Use the toString method to convert n to a string representation in the specified base
    return n.toString(base);
  };
};
