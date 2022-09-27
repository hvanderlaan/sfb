###############################################################################
# File     : api/telegram.py                                                  #
# Purpose  : Send a telegram message to a telegram bot with storm forcasts    #
#            warnings of the European continent.                              #
#                                                                             #
# Author   : Harald van der Laan                                              #
# Date     : 2022/09/15                                                       #
# Version  : v0.0.1                                                           #
###############################################################################
# Requirements:                                                               #
#  - Python3                                                                  #
#  - Telegram bot from @BotFather                                             #
###############################################################################
# Changelog:                                                                  #
#  - v0.0.1    : initial version                                              #
###############################################################################

import httpx


def send_telegram(token, chatid, data):
    """ send notification to telegram

    token is telegram bot tocken
    chatid is id to send message to
    data is the message content """

    url = 'https://api.telegram.org/bot' + token
    url += '/sendMessage?chat_id=' + chatid
    url += '&parse_mode=Markdown&text=' + data
    response = httpx.get(url)

    return response.json()


def send_telegram_photo(token, chatid, img_url):
    """ send image to telegram

    token is telegram bot tocken
    chatid is id to send message to"""

    url = 'https://api.telegram.org/bot' + token
    url += '/sendPhoto?chat_id=' + chatid
    url += '&parse_mode=Markdown&photo=' + img_url
    response = httpx.get(url)

    return response.json()
