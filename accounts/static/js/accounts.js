
document.getElementById("student-registration-form").addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent page reload

    let formData = {
        name: document.getElementById("name").value,
        father_name: document.getElementById("father_name").value,
        class_name: document.getElementById("class").value,
        roll_number: document.getElementById("roll_number").value,
        section: document.getElementById("section").value,
        school: document.getElementById("school").value,
        phone_number: document.getElementById("phone_number").value
    };

    try {
        let response = await fetch("/register/student/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken()  // For Django CSRF protection
            },
            body: JSON.stringify(formData)
        });

        let result = await response.json();

        if (response.ok) {
            document.getElementById("response-message").innerText = "Student registered successfully!";
            document.getElementById("response-message").style.color = "green";
            document.getElementById("student-registration-form").reset();  // Clear form
        } else {
            document.getElementById("response-message").innerText = result.error || "Registration failed!";
            document.getElementById("response-message").style.color = "red";
        }
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("response-message").innerText = "An error occurred!";
        document.getElementById("response-message").style.color = "red";
    }
});

// Function to get CSRF token from cookies
function getCSRFToken() {
    let cookieValue = null;
    let cookies = document.cookie.split(";");
    for (let cookie of cookies) {
        let [key, value] = cookie.trim().split("=");
        if (key === "csrftoken") {
            cookieValue = value;
            break;
        }
    }
    return cookieValue;
}

