# Kenyan Weather App

![Kenyan Weather App](https://aibunny.s3.ap-southeast-1.amazonaws.com/media/uploads/2023/10/29/celery.png)

## Overview

The Kenyan Weather App is a powerful Django-based web application that provides real-time weather data for various locations in Kenya. With the integration of Celery, this app ensures up-to-the-minute weather forecasts without causing delays in its response time.

## Features

- Real-time weather data retrieval
- User-friendly interface for inputting locations
- Efficient task management with Celery and a message broker
- Historical weather data records
- Responsive and seamless user experience

## Technologies Used

- Django: A high-level Python web framework
- Celery: An asynchronous task queue/job queue based on distributed message passing
- Redis: A popular message broker for Celery
- OpenWeatherMap API: For fetching weather data
- HTML/CSS: For front-end design
- Python: For back-end logic

## Getting Started

1. Clone this repository: `git clone https://github.com/aibunny/kenyan-weather-app.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Set up Celery and configure your message broker (e.g., Redis).
4. Run the development server: `python manage.py runserver`
5. Access the Kenyan Weather App in your web browser at `http://localhost:8000/weather`

## Contribution

I welcome contributions and suggestions to make the Kenyan Weather App even better. If you have ideas, bug reports, or feature requests, feel free to open an issue or submit a pull request.

## Author

- aibunny
- Blog: [Medium Blog](https://aibunny.medium.com/django-and-celery-supercharging-your-web-app-with-asynchronous-tasks-7ad989848d08)
- Personal Blog: [Your Personal Blog](https://www.theaibunny.com/django-and-celery)

