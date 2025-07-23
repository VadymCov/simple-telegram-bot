# Telegram Bot with Inline buttons

Simple Telegram bot on aiogram 3.x with basic functionality of inline buttons.

## Features

- Command `/start` with a welcome message
- Three interactive inline buttons
- Asynchronous callback processing

## Installation

1. Clone the repository:
```bash
git clone <your-repo>
cd <project-folder>
```

2. Install dependencies:
```bash
pip install aiogram
```

3. Create a `config.py` file and add the bot token:
```python
YOUR_TOKEN = "your_token_from_BotFather"
```

## Setup

1. Create a bot in [@BotFather](https://t.me/BotFather)
2. Get the token and add it to `config.py`
3. Make sure `config.py` is added to `.gitignore`

## Launch

```bash
python start.py
```

## Project structure

```
├── start.py # Main bot file
├── config.py # Configuration (token)
├── .gitignore # Ignored files
└── README.md # Documentation
```

## Usage

After launching the bot:
1. Find the bot in Telegram
2. Send the command `/start`
3. Click on the inline buttons "one", "two", "three"

## Requirements

- Python 3.7+
- aiogram 3.x

## Security

⚠️ **Important**: Never commit the `config.py` file with the token to a public repository!

## License

This project is distributed under the MIT license.