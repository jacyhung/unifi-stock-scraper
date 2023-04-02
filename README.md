# Unifi Stock Scraper
This is a simple script that scrapes the stock of a Unifi store and sends a Discord notification via a webohok URL to the user if the stock is available.

## Requirements
- Python 3.6+
- Discord webhook URL
- BeautifulSoup4
- DiscordWebhook

## Usage
1. Clone the repository
2. Install the requirements
   1. ```python
      pip install -r requirements.txt
      ```
3. Run the script
   1. ```python
      python3 main.py
      ```
4. Sit back and wait. The script will run every minute and send a notification if the stock is available.