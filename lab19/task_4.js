// ...existing code...
function printStudents(students) {
    if (!Array.isArray(students)) throw new TypeError("Expected an array of names");
    students.forEach(name => console.log(name));
}

module.exports = { printStudents };

if (require.main === module) {
    const readline = require('readline');
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

    rl.question('Enter student names (comma-separated): ', (answer) => {
        const students = answer.split(',').map(s => s.trim()).filter(Boolean);
        if (students.length === 0) {
            console.log('No names entered.');
        } else {
            printStudents(students);
        }
        rl.close();
    });
}
// ...existing code...