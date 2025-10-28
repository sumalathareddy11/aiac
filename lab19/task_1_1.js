// ...new file...
function printNumbers() {
    // Print the first 10 natural numbers (1 through 10).
    for (let i = 1; i <= 10; i++) {
        console.log(i);
    }
}

module.exports = { printNumbers };

// If executed directly with Node, run the function
if (require.main === module) {
    printNumbers();
}
