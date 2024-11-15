const task11_right = document.getElementById("task11_right");

// Function to load category images
function loadCategory(category) {
    const images = {
        image_1: ["beaver.jpg"],
        image_2: ["cat_beam.jpg"],
        image_3: ["cheems.jpg"]
    };

    task11_right.innerHTML = ""; // Clear previous content

    if (images[category]) {
        images[category].forEach((img) => {
            const thumbnail = document.createElement("img");
            thumbnail.src = `images/${img}`;
            thumbnail.alt = img;
            thumbnail.addEventListener("click", () => {
                window.open(`images/${img}`, "_blank");
            });
            task11_right.appendChild(thumbnail);
        });
    } else {
        task11_right.innerHTML = "<p>No images available for this category.</p>";
    }
}

// Event Listeners for categories
document.getElementById("image_1").addEventListener("click", () => loadCategory("image_1"));
document.getElementById("image_2").addEventListener("click", () => loadCategory("image_2"));
document.getElementById("image_3").addEventListener("click", () => loadCategory("image_3"));
