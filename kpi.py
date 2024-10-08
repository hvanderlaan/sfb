#!/usr/bin/env python3

''' sfb.py: main python3 script for storm forcasts. '''

###############################################################################
# File     : kpi.py                                                           #
# Purpose  : Get and message the KP-Index for aurora's in Europe              #
#                                                                             #
# Author   : Harald van der Laan                                              #
# Date     : 2024/09/18                                                       #
# Version  : v0.0.1                                                           #
###############################################################################
# Requirements:                                                               #
#  - Python3                                                                  #
#  - Telegram bot from @BotFather                                             #
###############################################################################
# Changelog:                                                                  #
#  - v0.0.1    : initial version                                              #
###############################################################################

import configparser
from api import kpindex
from api import telegram


def main():
    ''' main function '''
    # configuration file actions
    config = configparser.ConfigParser()
    config.read('sfb.cfg')
    chat_id = config['telegram']['chatid']
    token = config['telegram']['token']
    noaaurl = config['noaa']['url']
    icon = u'\U0001F30C'

    # weeronline forecast
    kpi = kpindex.get_kp_index(noaaurl)
    if kpi >= 7:
        telegram.send_telegram(token, chat_id, icon + ' *KP-Index:* ' + str(kpi) + '\n\nEr is een grote kans op Noorderlicht')
    if kpi < 7 and kpi >= 5:
        telegram.send_telegram(token, chat_id, icon + ' *KP-Index:* ' + str(kpi) + '\n\nEr is een matige kans op Noorderlicht')
    if kpi < 5 and kpi >= 3:
        telegram.send_telegram(token, chat_id, icon + '*KP-Index:* ' + str(kpi) + '\n\nEr is een kleine kans op Noorderlicht')




if __name__ == "__main__":
    main()
