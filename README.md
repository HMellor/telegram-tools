# Telegram Tools
A wrapper around `telethon` for quick and simple implementations

## Installation
```bash
pip install git+https://github.com/HMellor/telegram-tools.git#egg=telegram-tools
# or
git clone https://github.com/HMellor/telegram-tools.git
pip install ./telegram_tools
```

## Setup
A `.cfg` file of the following format must be provided:
```
api_id=1234
api_hash=1234ABCD
token=1234:ABCD
chat_id=1234
```

## Usage
```python
import telegram_tools as tg

bot = tg.Bot("telegram.cfg")
bot.send_message("Hello World!")
```