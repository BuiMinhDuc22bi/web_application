//EX3
function checkOddEven() {
    
    // Get the output div
    const outputDiv = document.getElementById("output");
    outputDiv.innerHTML = ""; // Clear previous output

    // Loop from 1 to 15
    for (let i = 1; i <= 15; i++) {
        // Check if the number is odd or even
        if (i % 2 === 0) {
            outputDiv.innerHTML += `<p>${i} is even</p>`;
        } else {
            outputDiv.innerHTML += `<p>${i} is odd</p>`;
        }
    }
}
// Call the function
checkOddEven();
