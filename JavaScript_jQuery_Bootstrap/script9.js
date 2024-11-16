$(document).ready(function() {
    // Variable to store the time of the last click
    let lastClickTime = null;

    // Attach a click event to the paragraph
    $('p').click(function() {
        const currentClickTime = new Date().getTime(); // Get current timestamp in milliseconds

        if (lastClickTime !== null) {
            // Calculate the difference between current and last click times
            const timeDifference = currentClickTime - lastClickTime;
            
            // Log the time difference to the #log div
            $('#log').text(`Time between clicks: ${timeDifference} milliseconds`);
        }

        // Update the last click time to the current one
        lastClickTime = currentClickTime;
    });
});