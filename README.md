# CropSense
  This is a Crop Management System built using Django and MySQL. It helps to store the crop details and recommends crops based on the weather conditions of the current location or the seaeched location.

## About CropSense
  The Crop Management System, built with Django, tracks various crops and their details such as name, season, harvest time, price, and stock quantity. 
  It includes ideal growing conditions for each crop, like humidity, rainfall, and temperature ranges. 
  Users can view and add crops, and get smart recommendations for the best crops to grow based on current weather conditions using a weather API. 
  The system also provides real-time and forecasted weather information to assist with planting and harvesting activities.

## How to run on your machine

- Clone the repository <br>
  ```
  git clone https://github.com/rahulks01/CropSense.git
  ```

- Start up a virtual environment <br>
  ```
  python -m venv venv
  ```

- Activate the virtual environment <br>
  ```
  On Windows: venv\Scripts\activate
  ```
  ```
  On macOS and Linux: source venv/bin/activate
  ```
- Navigate to the project directory <br>
  ```
  cd CropSense
  ```
  
- Install the required packages <br>
  ```
  pip install -r requirements.txt
  ```

- Change the database credentials <br>
  Change the database credentials of your own database (MySQL) in the following file
  ```
  webapp/mydb.py
  ```
- Create the database <br>
  ```
  python mydb.py
  ```
  
- Load crops data <br>
  ```
  python manage.py load_crops.py
  ```

- Set up your OpenWeatherMap API key <br>
  Follow this <a href="https://openweathermap.org/">link</a> and set up your OpenWeatherMap API key.

- Add your OpenWeatherMap API key <br>
  Add your API key to the following files <br>
  ```
  webapp/static/script.js
  ```
  ```
  webapp/static/recommend.js
  ```
  ```
  webapp/weather_service.py
  ```

- Initialize the weather service <br>
  ```
  python manage.py fetch_weather.py
  ```
  
- Create a superuser for logging in <br>
  ```
  python manage.py createsuperuser
  ```
- Run the server <br>
  ```
  python manage.py makemigrations
  ```
  ```
  python manage.py migrate
  ```
  ```
  python manage.py runserver
  ```
  Open your web browser and go to `http://127.0.0.1:8000/`
