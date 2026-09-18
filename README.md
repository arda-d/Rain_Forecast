# Rain Alert & Weather SMS Notifier

An automated Python application that fetches weather forecast data for a specified location using the OpenWeatherMap API and sends an SMS notification via the Twilio API if rain or severe weather is predicted in the upcoming hours.

## Overview

Checking the daily weather forecast before leaving home can be easy to forget. This project automates that routine by inspecting the weather condition codes for the next 12 hours. If any forecast window indicates rain, drizzle, or snow, it immediately triggers an SMS notification to your mobile phone so you never forget your umbrella.

## Key Features

- **Automated Weather Inspection**: Fetches 3-hour interval weather forecast data from the OpenWeatherMap API.
- **Condition Code Analysis**: Evaluates OpenWeatherMap condition IDs to accurately detect precipitation (rain, drizzle, thunderstorm, snow).
- **Instant SMS Alerts**: Integrates with Twilio REST API to dispatch real-time text messages.
- **Environment Variable Security**: Utilizes `.env` files to keep sensitive API keys, account tokens, and personal phone numbers secure and separate from the source code.

## Tech Stack

- **Python 3.x**
- **Requests**: For handling HTTP GET requests to the OpenWeatherMap API.
- **Twilio SDK**: For interacting with Twilio's messaging service.
- **python-dotenv**: For loading environment variables from a local `.env` file.

## Project Structure

```text
.
├── main.py           # Main application script
├── .env.example      # Example environment configuration template
├── .gitignore        # Specifies files for Git to ignore
└── README.md         # Project documentation
