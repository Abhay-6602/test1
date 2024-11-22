document.getElementById('loginForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent the form from submitting

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('error-message');

    // Mock validation (replace with server-side authentication in a real application)
    if (username === 'admin' && password === 'password') {
        errorMessage.textContent = '';
        alert('Login successful!');
        // Redirect or perform further actions here
    } else {
        errorMessage.textContent = 'Invalid username or password.';
    }
});
