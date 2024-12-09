import { navigateTo } from '../router.js';


export function sendCodeOauth(appContainer) {
    //('from sendCodeOauth');
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get('code');
    //('Code:', code);
    
    fetch(`${window.self.origin}/backend/login/42/callback/?code=${code}`, {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => {
        //('Response:', response);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json(); // Parse the JSON response
    })
    .then(data => {
        if (data.message === '2fa required.') {
            // Redirect to a local 2FA input page with the token
            const token = data.redirect; 
            // Assuming you have the token from previous response
            navigateTo(`${token}`, appContainer); // Include the token in the URL
        } else {
            alert('You are logged in successfully!');
            localStorage.setItem('me', JSON.stringify(data.user));
            navigateTo('/home', appContainer); // Redirect to home
        }
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('An error occurred. Please try again.');
    });
}





export function render_42_login(appContainer) {
    window.location.href = window.self.origin + '/backend/' +'login/42/'
}
