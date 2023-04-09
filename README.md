# WeatherApplication

This is a Flask-based web application that fetches weather data from the OpenWeatherMap API and displays it on a webpage. It also uses the IPInfo API to automatically fetch the user's location and display the weather data for that location.

1)Features
Fetches weather data for a specified city or the user's location
Displays the temperature, weather description, and icon for the location
Automatically detects the user's location using the IPInfo API
Supports both Celsius and Fahrenheit units
Prerequisites
Python 3.6 or higher
Flask 2.0.1 or higher
Requests 2.26.0 or higher

2)Getting Started
Clone the repository or download the code as a ZIP file and extract it to a directory of your choice.

Install the required Python libraries by running the following command in a terminal or command prompt:

Copy code
pip install -r requirements.txt
Sign up for a free API key from OpenWeatherMap and IPInfo.

Replace the placeholders for API_KEY_OPENWEATHERMAP and API_KEY_IPINFO in the app.py file with your own API keys.

Start the Flask server by running the following command in a terminal or command prompt:

Copy code
python app.py
Open a web browser and go to http://localhost:7000/ to access the application.

3)Usage
Enter a city name in the search bar and press Enter or click the search button to fetch the weather data for that location.
If the search bar is left blank, the application will automatically fetch the weather data for the user's location.
Click the unit toggle button to switch between Celsius and Fahrenheit units.

4)Credits
This application was developed by Pramit.
The weather data is provided by OpenWeatherMap.
The user location data is provided by IPInfo.
