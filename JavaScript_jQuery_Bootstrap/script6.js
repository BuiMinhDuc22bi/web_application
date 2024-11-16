document.addEventListener("DOMContentLoaded", function () {
    // Select all h1 elements inside a div
    const h1InsideDiv = document.querySelectorAll('div > h1');
    
    // Apply background color to each h1 element found
    h1InsideDiv.forEach(function (h1) {
        h1.style.backgroundColor = "#f0f0f0"; // Apply a background color
    });
});