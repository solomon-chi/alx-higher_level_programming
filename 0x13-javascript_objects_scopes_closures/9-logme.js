#!/usr/bin/node

// Define a counter variable i and set it to 0
let i = 0;

// Export a function called logMe that takes a single argument called item
exports.logMe = function (item) {
  // Log the current value of i and the value of item to the console
  console.log(i + ': ' + item);
  
  // Increment the value of i by 1
  i++;
};

