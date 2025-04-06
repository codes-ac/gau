document.getElementById("student-registration-form").addEventListener("submit", async function (event) {
    event.preventDefault();

    let formData = {
        name: document.getElementById("name").value,
        father_name: document.getElementById("father_name").value,
        class_number: document.getElementById("student_class").value,
        roll_number: document.getElementById("roll_number").value,
        email: document.getElementById("email").value,
        school: document.getElementById("school").value,
        phone_number: document.getElementById("phone_number").value,
        gender: document.getElementById("gender").value
    };

    const errorDiv = document.getElementById("form-error");
    errorDiv.innerHTML = ""; 

    try {
        const response = await fetch("/register/student/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken()
            },
            body: JSON.stringify(formData)
        });

        const responseText = await response.text(); // read raw text
        console.log("Raw Response Text:", responseText);

        let result;
        try {
            result = JSON.parse(responseText);
        } catch (jsonError) {
            console.error("Error parsing JSON:", jsonError);
            errorDiv.innerHTML = `<div class='error-text'>Unexpected server response.</div>`;
            return;
        }

        console.log("Parsed Response Body:", result);

        if (response.ok) {
            const userId = result.student_id;
            window.location.href = `/student/${userId}/profile/`;
        } else {
            // Show errors properly
            for (const key in result) {
                const errorMessages = Array.isArray(result[key]) ? result[key] : [result[key]];
                errorMessages.forEach((msg) => {
                    const errorText = document.createElement("div");
                    errorText.className = "error-text";
                    errorText.innerText = `${key}: ${msg}`;
                    errorDiv.appendChild(errorText);
                });
            }
        }
    } catch (error) {
        console.error("Fetch error:", error);
        errorDiv.innerHTML = "<div class='error-text'>An unexpected error occurred. Please try again.</div>";
    }
});

// CSRF helper
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
