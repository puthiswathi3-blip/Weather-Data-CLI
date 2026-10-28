##### **Weather Data CLI 🌦️**

###### 

###### **Description**

The Weather Data CLI is a Python command-line application that retrieves current weather information for a user-provided city using the OpenWeather API. It displays useful weather details in a clear and formatted output.



###### **Objectives**

\- Learn how to integrate a weather API with Python.

\- Understand API requests and JSON data processing.

\- Practice functions and exception handling.

\- Store API credentials securely using environment variables.



###### **Technologies Used**

\- Programming Language: Python

\- Library: Requests

\- API: OpenWeather API



###### **Features**

\- Accepts city names from the user.

\- Displays temperature in Celsius.

\- Shows weather conditions, feels-like temperature, humidity, and wind speed.

\- Handles invalid city names and network errors.

\- Keeps API credentials outside the source code.

\- Allows users to check multiple cities until they choose to exit.



###### **Project Structure**



Weather-Data-CLI/

│

├── weather\_cli.py

└── README.md



###### **Installation and Setup**



1\. Install the required library



pip install requests



2\. Get an API key



Create an account at \[OpenWeather](https://openweathermap.org/api) and obtain an API key.



3\. Set the API key



For Windows Command Prompt:



cmd

set OPENWEATHER\_API\_KEY=your\_api\_key\_here



For Windows PowerShell:



powershell

$env:OPENWEATHER\_API\_KEY="your\_api\_key\_here"





Replace `your\_api\_key\_here` with your actual API key.



4\. Run the program



python weather\_cli.py



###### **Sample Output**

Welcome to the Weather Data CLI!



Enter city name (or type 'exit' to quit): Hyderabad



===================================

&#x20;        WEATHER REPORT

===================================

City        : Hyderabad, IN

Condition   : Clear Sky

Temperature : 29.5 °C

Feels Like  : 31.2 °C

Humidity    : 45%

Wind Speed  : 3.5 m/s

===================================

```



Note: The displayed weather values are examples. Actual results depend on current weather conditions.



###### **Error Handling**

\- Displays an error when the city name is invalid.

\- Handles connection errors and request timeouts.

\- Reports missing API credentials.

\- Handles unexpected or incorrectly formatted API responses.



###### **Learning Outcomes**

This project helped me understand how to connect Python applications to external APIs, process JSON responses, use environment variables, and handle errors in a command-line application.



###### **Conclusion**

The Weather Data CLI is a practical Python project that combines API integration, data processing, functions, and error handling to retrieve and display current weather information.





