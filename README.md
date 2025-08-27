![Static Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white)

# Telegram Chat User Scraper

This Python script uses the Pyrogram library to scrape user information from a Telegram group, supergroup, or channel and save it to a JSON file

## Features

- **Scrapes User Data:** Extracts user ID, first name, last name, username, and premium status from Telegram chat members
- **Filters Bots:** Excludes bots from the scraped user list
- **Saves to JSON:** Stores the collected user data in a neatly formatted JSON file
- **Error Handling:** Includes basic error handling to catch and print potential exceptions
- **Clear User Class:** Uses a `User` class for object-oriented data handling
- **Uses `getattr` for optional fields:** Safely handles cases where `first_name`, `last_name`, or `username` may be missing for a user

## Prerequisites

-   Python 3.7 or higher
-   Pyrogram library (`pip install pyrogram`)

## Installation

1.  **Clone the repository:**
```bash
git clone [repository_url]
cd [project_directory]
```

2. Install the required dependencies:
```bash
pip install pyrogram
```

## Setup

1. Get API Credentials:

  - Go to my.telegram.org (https://my.telegram.org/) and log in with your Telegram account
  - Create a new app and obtain your API_ID and API_HASH

2. Configure the Script:

  - Open the script.py file (or whatever the name of your main file is).
  - Replace the placeholder values with your actual credentials and settings:
```python
    API_ID = 123456789 # Your API ID
    API_HASH = "YOURAPIHASH" # Your API HASH
    CHAT_TO_PARSE = -100123456789 # The chat ID of the group/channel
    PATH_TO_SAVE = "users.json" # The filename to save users to. Must end in .json
```
- Important Notes:
    - Store API_ID and API_HASH securely. Consider using environment variables
    - CHAT_TO_PARSE must be the numeric ID of the group, supergroup, or channel. It's usually a negative number for groups and channels and starts with -100. You need admin rights to scrape members in channels
    - PATH_TO_SAVE specifies the name of the JSON file where the user data will be stored. Ensure the script has write access to the directory where you're saving the file

## Usage

1. Run the script:
```bash
python members_parsing.py
```
2. Authorize your Account:

  - The first time you run the script, it will prompt you to enter your phone number and verification code to authorize your Telegram account. Follow the instructions in the console

3. The User Data:

  - The script will scrape the user data and save it to the users.json file

## Data Format

The users.json file will contain a JSON array of user objects. Each object will have the following structure:


```json
[
  {
    "user_id": 123456789,
    "first_name": "John",
    "last_name": "Doe",
    "username": "@johndoe",
    "is_premium": true
  },
  {
    "user_id": 987654321,
    "first_name": "Jane",
    "last_name": "Smith",
    "username": "None",
    "is_premium": false
  }
]
```

## Disclaimer

This script is provided for educational purposes only. The author is not responsible for any misuse of this script. Use at your own risk

## License

This project is licensed under the MIT License

## Support

![Static Badge](https://img.shields.io/badge/TON-0098EA?style=for-the-badge&logo=TON&logoColor=white)

`UQB-7m2USzQ451d9orgD4iECLD0FL_BV-zzk3i--bdRl51ho`


![Static Badge](https://img.shields.io/badge/TRC20-50AF95?style=for-the-badge&logo=tether&logoColor=white)

`TUbvCEDE5wpVRsbLmuU8JfkWY4gNcBNbrx`
