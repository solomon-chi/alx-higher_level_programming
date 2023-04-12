#!/usr/bin/node

// This script concats 2 files specified as command line arguments

// Retrieve the command line arguments passed to the script
const args = process.argv.slice(2);

// Import the built-in Node.js `fs` module
const file = require('fs');

// Read the contents of the first file specified in the command line arguments
const contentA = file.readFileSync('./' + args[0]);

// Read the contents of the second file specified in the command line arguments
const contentB = file.readFileSync('./' + args[1]);

// Concatenate the contents of the two files into a single string
const combinedContent = contentA + contentB;

// Write the concatenated string to a new file specified in the command line arguments
file.writeFileSync('./' + args[2], combinedContent);
