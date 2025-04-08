async function submitForm() {
const form = document.getElementById('adoptionForm');
const formData = new FormData(form);  // Collect form data
const jsonData = {};  // Object to hold JSON

// Convert FormData to JSON
formData.forEach((value, key) => {
    jsonData[key] = value;
});

try {
    const response = await fetch('/submit-application', {  // Your server endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    });

    console.log("Fetch call completed. Response:", response);  // Add this line

    if (response.ok) {
        const responseData = await response.json();  // Parse the JSON response

        console.log('Hey Mike, the application submitted successfully!');
        //alert(responseData.message);  // Display the message from the server
        alert(responseData.message || "Submission successful (no message from server)");

    } else {
        console.error('Submission failed:', response.status);
        alert('Submission failed'); // Simple error message
    }
} catch (error) {
    console.error('Network error:', error);
    alert('Network error occurred');
}

}

document.addEventListener('DOMContentLoaded', function() {
    const agreementCheckbox = document.getElementById('agreement');
    const submitButton = document.getElementById('submitButton');
    const requiredFields = document.querySelectorAll('[required]'); // Get all required elements

    function validateForm() {
        let allFilled = true; // Assume all are filled initially

        for (let i = 0; i < requiredFields.length; i++) {
            const field = requiredFields[i];
            if (field.type === 'checkbox') {
                if (!field.checked) {
                    allFilled = false;
                    break;
                }
            } else {
                if (!field.value.trim()) { // Check if value is empty or whitespace
                    allFilled = false;
                    break;
                }
            }
        }
        submitButton.disabled = !allFilled; // Disable if not all filled
    }

    // Run validation on page load
    validateForm();

    // Add event listeners to required fields
    requiredFields.forEach(field => {
        field.addEventListener('input', validateForm); // For text inputs
        field.addEventListener('change', validateForm); // For checkboxes, select etc.
    });
});



//
// Explanation of Changes:

// const requiredFields = document.querySelectorAll('[required]');: This line uses document.querySelectorAll('[required]') to get a list of all elements in the document that have the required attribute. 
// This includes text inputs, checkboxes, select elements, etc.
// function validateForm() { ... }: This function is responsible for checking if all the required fields have a value.
// let allFilled = true;: This variable is used to keep track of whether all required fields are filled. 
// It's initialized to true (assuming all are filled) and will be set to false if any required field is found to be empty.

// The for loop iterates through all the requiredFields.
// For each field, it checks if its value is empty (using !field.value.trim()). The trim() method removes any leading or trailing whitespace from the value, so that a field containing only spaces is considered empty.

// If a required field is found to be empty, allFilled is set to false, and the loop breaks (using break;).
// submitButton.disabled = !allFilled;: After the loop finishes, the disabled property of the submit button is set to the opposite of allFilled. If allFilled is true (meaning all required fields have a value), the button is enabled ( disabled = false ). 
// If allFilled is false (meaning at least one required field is empty), the button is disabled ( disabled = true ).
// validateForm();: This line calls the validateForm function once when the page loads. This ensures that the button is initially disabled if any required fields are empty.

// Event Listeners:
// The forEach loop attaches event listeners to all the requiredFields.

// field.addEventListener('input', validateForm);: This adds an event listener to the input event. The input event is fired whenever the value of an input element is changed. 
// This is used for text inputs, textareas, select elements, etc.

// field.addEventListener('change', validateForm);: This adds an event listener to the change event. The change event is fired when the value of an input element has been committed by the user. 
// This is used for checkboxes, radio buttons, and select elements.

// By listening to both the input and change events, you ensure that the validateForm function is called whenever the user changes the value of any required field. 
// This keeps the submit button's state up-to-date in real-time.
// With this code in place, the "Submit Application" button will be disabled when the page loads and will only become enabled when all the required fields have a value. 
// The button will also be automatically disabled if the user clears any of the required fields.
  