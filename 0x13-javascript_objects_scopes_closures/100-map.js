#!/usr/bin/node

// Import the array called "list" from the "./100-data" module
const originalList = require('./100-data').list;

// Print the original array to the console
console.log(originalList);

// Use the map method to create a new array with modified values
const mappedList = originalList.map(function (e, index) {
  // Multiply each element by its index and return the result as the new value
  return (e * index);
});

// Print the new array to the console
console.log(mappedList);
