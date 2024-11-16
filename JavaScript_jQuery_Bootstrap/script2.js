//EX2
 // Function to find the largest of five numbers
 function findLargestNumber() {
    // Array to store the numbers
    let numbers = [];

    // Loop to get 5 numbers from the user
    for (let i = 1; i <= 5; i++) {
        let num = parseFloat(prompt(`Enter number ${i}:`));

        // Validate input
        if (isNaN(num)) {
            alert("Please enter a valid number.");
            return; // Exit the function if input is invalid
        }
        numbers.push(num);
    }

    // Find the largest number
    let largest = Math.max(...numbers);

    // Display the result
    alert(`The largest number is: ${largest}`);
}

// Call the function
findLargestNumber();
