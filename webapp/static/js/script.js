const API_KEY = "YOUR_API_KEY_HERE"; //Enter your API Key here

const cityInput = document.querySelector(".city-input");
const searchButton = document.querySelector(".search-btn");
const locationButton = document.querySelector(".location-btn");
const currentWeatherDiv = document.querySelector(".current-weather");
const forecastContainer = document.querySelector(".forecast-container");

const createWeatherCard = (cityName, weatherItem, index) => {
  if (index === 0) {
    return `<div class="weather-icon">
              <img src="https://openweathermap.org/img/wn/${weatherItem.weather[0].icon}@4x.png" alt="Weather Icon">
            </div>
            <div class="weather-details">
              <h2>${cityName}</h2>
              <h3>Temperature: ${(weatherItem.main.temp - 273.15).toFixed(2)}°C</h3>
              <p>${weatherItem.weather[0].description}</p>
              <p>Humidity: ${weatherItem.main.humidity}%</p>
              <p>Wind Speed: ${weatherItem.wind.speed} m/s</p>
            </div>`;
  } else {
    return `<div class="forecast-card">
              <h3>${weatherItem.dt_txt.split(" ")[0]}</h3>
              <img src="https://openweathermap.org/img/wn/${weatherItem.weather[0].icon}@4x.png" alt="Weather Icon">
              <p>Temp: ${(weatherItem.main.temp - 273.15).toFixed(2)}°C</p>
              <p>Wind: ${weatherItem.wind.speed} m/s</p>
              <p>Humidity: ${weatherItem.main.humidity}%</p>
            </div>`;
  }
};

const getWeatherDetails = (cityName, latitude, longitude) => {
  const WEATHER_API_URL = `https://api.openweathermap.org/data/2.5/forecast?lat=${latitude}&lon=${longitude}&appid=${API_KEY}`;

  fetch(WEATHER_API_URL)
    .then(response => response.json())
    .then(data => {
      const uniqueForecastDays = [];
      const fiveDaysForecast = data.list.filter(forecast => {
        const forecastDate = new Date(forecast.dt_txt).getDate();
        if (!uniqueForecastDays.includes(forecastDate)) {
          return uniqueForecastDays.push(forecastDate);
        }
      });

      cityInput.value = "";
      currentWeatherDiv.innerHTML = "";
      forecastContainer.innerHTML = "";

      fiveDaysForecast.forEach((weatherItem, index) => {
        const html = createWeatherCard(cityName, weatherItem, index);
        if (index === 0) {
          currentWeatherDiv.insertAdjacentHTML("beforeend", html);
        } else {
          forecastContainer.insertAdjacentHTML("beforeend", html);
        }
      });
    })
    .catch(() => {
      alert("An error occurred while fetching the weather forecast!");
    });
};

const getCityCoordinates = () => {
  const cityName = cityInput.value.trim();
  if (cityName === "") return;
  const API_URL = `https://api.openweathermap.org/geo/1.0/direct?q=${cityName}&limit=1&appid=${API_KEY}`;

  fetch(API_URL)
    .then(response => response.json())
    .then(data => {
      if (!data.length) return alert(`No coordinates found for ${cityName}`);
      const { lat, lon, name } = data[0];
      getWeatherDetails(name, lat, lon);
    })
    .catch(() => {
      alert("An error occurred while fetching the coordinates!");
    });
};

const getUserCoordinates = () => {
  navigator.geolocation.getCurrentPosition(
    position => {
      const { latitude, longitude } = position.coords;
      const API_URL = `https://api.openweathermap.org/geo/1.0/reverse?lat=${latitude}&lon=${longitude}&limit=1&appid=${API_KEY}`;
      fetch(API_URL)
        .then(response => response.json())
        .then(data => {
          const { name } = data[0];
          getWeatherDetails(name, latitude, longitude);
        })
        .catch(() => {
          alert("An error occurred while fetching the city name!");
        });
    },
    error => {
      if (error.code === error.PERMISSION_DENIED) {
        alert("Geolocation request denied. Please reset location permission to grant access again.");
      } else {
        alert("Geolocation request error. Please reset location permission.");
      }
    }
  );
};

locationButton.addEventListener("click", getUserCoordinates);
searchButton.addEventListener("click", getCityCoordinates);
cityInput.addEventListener("keyup", e => e.key === "Enter" && getCityCoordinates());
