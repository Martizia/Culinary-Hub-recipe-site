fetch('http://api.weatherapi.com/v1/current.json?key=1501cfd6fa0241e0aca160204242304&q=Kyiv&aqi=no')
    .then(response => response.json())
    .then(data => {
        const weatherDiv = document.getElementById('weather');
        weatherDiv.innerHTML = `
            <h2>Weather in ${data.location.name}</h2>
            <p>Temperature: ${data.current.temp_c}°C</p>
            <p>Weather: ${data.current.condition.text}</p>
        `;
    })
    .catch(error => console.error('Error:', error));