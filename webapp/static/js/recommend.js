// static/js/recommend.js
const apiKey = 'YOUR_API_KEY_HERE'; // Replace with your API key

function getCurrentLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(async function(position) {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            try {
                const locationName = await getLocationName(lat, lon);
                if (locationName) {
                    window.location.href = `/recommend/${encodeURIComponent(locationName)}/`;
                } else {
                    alert('Unable to retrieve location name.');
                }
            } catch (error) {
                alert('Error: ' + error.message);
            }
        }, function(error) {
            alert('Error getting location: ' + error.message);
        });
    } else {
        alert('Geolocation is not supported by this browser.');
    }
}

async function getLocationName(lat, lon) {
    const response = await fetch(`https://api.openweathermap.org/geo/1.0/reverse?lat=${lat}&lon=${lon}&limit=1&appid=${apiKey}`);
    if (!response.ok) {
        throw new Error('Failed to fetch location name');
    }
    const data = await response.json();
    if (data.length > 0) {
        return data[0].name;
    }
    return null;
}

document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    const location = document.getElementById('location').value.trim();
    if (location) {
        window.location.href = `/recommend/${encodeURIComponent(location)}/`;
    } else {
        alert('Please enter a location');
    }
});
