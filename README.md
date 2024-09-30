
---

# Doctor Availability Notifier on Helsi.me

This project helps users get real-time updates about available doctor appointments on the website Helsi.me. It works by parsing the selected doctor's page and sending a message to a Telegram chat with the available appointment slots.

## Features

- Parses the page of a chosen doctor on Helsi.me.
- Checks for available appointment slots.
- Sends notifications to a specified Telegram chat if slots become available.
- Continually refreshes the page and updates based on new availability.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Docker
- Telegram Bot Token
- Configuration file with necessary settings

## Installation

### 1. Local Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/doctor-availability-notifier.git
cd doctor-availability-notifier
```

2. Install the required libraries using pip:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should include:

```
telegram
configparser
asyncio
selenium
```

3. Create a `config.ini` file in the root of the project with the following content:

```ini
[Settings]
bot_token = YOUR_TELEGRAM_BOT_TOKEN
chat_id = YOUR_CHAT_ID
```

Replace `YOUR_TELEGRAM_BOT_TOKEN` and `YOUR_CHAT_ID` with your actual bot token and chat ID from Telegram.

4. Update the `target_page` variable in the `main.py` file with the URL of the doctor's page you want to monitor on Helsi.me.

```python
target_page = "https://helsi.me/doctor/ds_000"
```

### 2. Docker Installation

To run the project using Docker, follow these steps:

1. Build the Docker image:

```bash
docker build -t helsi-notifier .
```

2. Run the Docker container:

```bash
docker run -d helsi-notifier
```

The Dockerfile takes care of installing the necessary dependencies, including Google Chrome, which is required for running Selenium with Chrome WebDriver.

#### Dockerfile Details:

- **Base Image**: `python:3.12-slim` for a lightweight Python environment.
- **Working Directory**: The app files are copied to `/app`.
- **Chrome Installation**: The Dockerfile installs Google Chrome and sets up the environment for Selenium to work with it.

If you want to adjust the `config.ini` or any other files, make sure to rebuild the Docker image after changes.

```bash
docker build -t helsi-notifier .
```

## Usage

1. Once the script is running, it will begin monitoring the doctor’s page and send a Telegram message whenever appointment slots become available.

2. The script will log activities to the console, helping you track when the page is being parsed and when messages are sent.

## Logging

Logs are set up to help track the behavior of the bot and the page parsing process. Logging output can be viewed in the console.

## Customization

- **Exception Days**: You can exclude specific days from being checked by adding them to the `exception_days` list in the `main.py` file.
  
```python
exception_days = ["01 січ", "01 вер", "01 жовт"]
```

- **Time Interval**: The script checks for availability every 60 seconds, but you can adjust this interval by modifying the `time.sleep(60)` line in the `main()` function.

## Project Structure

```
doctor-availability-notifier/
│
├── functionality/
│   ├── driver.py        # Script to handle the web driver and page interaction.
│   ├── doctor_info.py   # Script to obtain necessary doctor information.
│   ├── message.py       # Script to customise the message to Telegram.
│   ├── parsing_helsi.py # Script to parse the Helsi.me doctor page.
│
├── config.ini           # Configuration file for bot token and chat ID.
├── main.py              # Main script for running the notification system.
└── README.md            # This file.
```

## Contributions

Feel free to fork the project, submit issues, and contribute!

---

