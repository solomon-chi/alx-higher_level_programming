#!/usr/bin/node

// function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  // Use the filter method to create a new array containing only the elements
  // that are equal to searchElement. Then, use the length property to get the
  // number of elements in the new array, which is the number of occurrences of
  // searchElement in the original list.
  return (list.filter(e => e === searchElement).length);
};
