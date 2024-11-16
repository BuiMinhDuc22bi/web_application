function checkPasswords() {
    // Get the input values
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm-password").value;
    const message = document.getElementById("ex4_message");

    // Clear previous messages
    message.textContent = "";

    // Check if passwords match
    if (password === confirmPassword) {
        message.textContent = "Passwords match!";
        message.className = "success";
    } else {
        message.textContent = "Passwords do not match. Please try again.";
        message.className = "error";
    }
}