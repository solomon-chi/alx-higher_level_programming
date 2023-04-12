#!/usr/bin/node

// Define function 'esrever'
exports.esrever = function (list) {

  // Initialize an empty array to store the reversed list
  const reversedList = [];

  // Get the index of the last element in the list
  const last = list.length - 1;

  // Loop through the list in reverse order and append each element to the reversed list
  for (let i = last; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  // Return the reversed list
  return (reversedList);
};
