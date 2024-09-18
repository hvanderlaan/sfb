#!/usr/bin/env python3

''' sfb.py: main python3 script for storm forcasts. '''

###############################################################################
# File     : sfb.py                                                           #
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

    # weeronline forecast
    kpi = kpindex.get_kp_index(noaaurl)
    if kpi >= 4 and kpi < 5:
        telegram.send_telegram(token, chat_id, '*KP-Index:* ' + str(kpi) + '\n\nEr is een kleine op kans Noorderlicht')
    elif kpi >= 5 and kpi < 7:
        telegram.send_telegram(token, chat_id, '*KP-Index:* ' + str(kpi) + '\n\nEr is een matige kans op Noorderlicht')
    elif kpi >= 7:
        telegram.send_telegram(token, chat_id, '*KP-Index:* ' + str(kpi) + '\n\nEr is een grote kans op Noorderlicht')



if __name__ == "__main__":
    main()
