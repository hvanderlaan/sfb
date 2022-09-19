# Storm chasers Forecast Bot

Storm chasers Forecast Bot uses [Estofex](https://www.estofex.org) notifications when ther is a Level 1, 2 or 3 warning of storms in Europe. The bot will send a picture and a description of the warning level in Europe.

## Requirements

    - Python3
        - argeparse
        - configparser
        - bs4
        - httpx
    - Telegram bot

## Installation

### Creating a Telegram bot

Open telegram chat application on your phone, desktop or browser and send `/newbot` to `@BotFather` and follow the instructions. when you are done creating the bot you will see the bot in Telegram. Click on your bot and start it.

If you are using the bot only for your self you're done. If you need to use the bot in a group, please craete a new group and add the bot to the group.

Send a message to the bot or the group and open a browser to get the `chat_id` this is needed for the Telegram configuration file. Please go to `https://api.telegram.org/bot<token>/getUpdates` `<token>` is provided by `@BotFather` in the last message. The page will show you some json string and search for `"chat_id"` This is `positive number` if you are using the bot directly and a `negative number` when the bot is in a group.

### Getting the brains of the bot

```
git clone https://www.github.com/hvanderlaan/sfb.git
cd sfb
pip install -r requirements.txt
cp sfb.cfg.sample sfb.cfg
vi sfb.cfg
    - edit the chat_id and token

./sfb.py
```

And wait for the telegram message in the bot or the group. To automate the messages you could place the `forecast.py` script in cron.

```
vi /etc/cron.d/estofex
0 9 * * * cd /<path/to>/; python3 sfb.py >/dev/null 2>&1
```

## Todo

- [X] Add comments and headers to python files if needed.
- [X] Change image url to get better image.
- [X] Change use of forecast.txt to memory only.
- [X] Add Dutch weather forecasts
- [ ] Add argument for output only and not sending to telegram.