document.getElementById('adoptionForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevents the default form submission behavior

    const formData = new FormData(this);
    const jsonData = Object.fromEntries(formData);

    // Convert the data to JSON and display it
    const jsonOutput = JSON.stringify(jsonData, null, 4); // Pretty-print JSON with indentation

    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML = '<pre>' + jsonOutput + '</pre>'; // Display JSON in a preformatted block
});
