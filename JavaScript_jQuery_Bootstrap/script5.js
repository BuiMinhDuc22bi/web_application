document.addEventListener("DOMContentLoaded", function () {
    const multiplyBtn = document.getElementById("multiplyBtn");
    const divideBtn = document.getElementById("divideBtn");
    const resultDiv = document.getElementById("ex5_result");

    multiplyBtn.addEventListener("click", function () {
        const num1 = parseFloat(document.getElementById("num1").value);
        const num2 = parseFloat(document.getElementById("num2").value);

        if (isNaN(num1) || isNaN(num2)) {
            resultDiv.textContent = "Please enter valid numbers.";
            resultDiv.style.color = "red";
            return;
        }

        const result = num1 * num2;
        resultDiv.textContent = `The Result is: ${result}`;
        resultDiv.style.color = "black";
    });

    divideBtn.addEventListener("click", function () {
        const num1 = parseFloat(document.getElementById("num1").value);
        const num2 = parseFloat(document.getElementById("num2").value);

        if (isNaN(num1) || isNaN(num2)) {
            resultDiv.textContent = "Please enter valid numbers.";
            resultDiv.style.color = "red";
            return;
        }

        if (num2 === 0) {
            resultDiv.textContent = "Division by zero is not allowed.";
            resultDiv.style.color = "red";
            return;
        }

        const result = num1 / num2;
        resultDiv.textContent = `The Result is: ${result.toFixed(2)}`;
        resultDiv.style.color = "black";
    });
});