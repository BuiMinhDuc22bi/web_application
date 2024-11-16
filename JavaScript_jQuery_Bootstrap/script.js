document.addEventListener("DOMContentLoaded", function () {
    
    //for seperate the id of the homework 
    const tempInput = document.getElementById("tempInput");
    const conversionType = document.getElementById("conversionType");
    const convertBtn = document.getElementById("convertBtn");
    const resultDiv = document.getElementById("ex1_result");

    convertBtn.addEventListener("click", function () {
        const temp = parseFloat(tempInput.value);
        if (isNaN(temp)) {
            resultDiv.textContent = "Please enter a valid temperature.";
            resultDiv.style.color = "red";
            return;
        }

        let result;
        if (conversionType.value === "toCelsius") {
            result = ((temp - 32) * 5) / 9;
            resultDiv.textContent = `Converted Temperature: ${result.toFixed(2)} °C`;
        } else if (conversionType.value === "toFahrenheit") {
            result = (temp * 9) / 5 + 32;
            resultDiv.textContent = `Converted Temperature: ${result.toFixed(2)} °F`;
        }
        resultDiv.style.color = "black";
    });
});

    

