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
from api import estofex
from api import knmi
from api import weeronline
from api import telegram


def main():
    ''' main function '''
    # configuration file actions
    config = configparser.ConfigParser()
    config.read('sfb.cfg')
    chat_id = config['telegram']['chatid']
    token = config['telegram']['token']
    estofexurl = config['estofex']['baseurl']
    knmiurl = config['knmi']['url']
    weeronlineurl = config['weeronline']['url']

    # getting estofex forecast
    warnings = estofex.get_warning()

    if warnings['level'] != 'None':
        url = estofexurl + warnings['link']
        estofex_forecast = estofex.get_forecast(url)
        estofex_img_url = estofexurl + warnings['image']

        # send forecast to telegram bot / group
        telegram.send_telegram_photo(token, chat_id, estofex_img_url)
        telegram.send_telegram(token, chat_id, estofex_forecast)

    # knmi forecast
    knmi_warnings = knmi.get_warning(knmiurl)

    if knmi_warnings['warning'] != 'None':
        knmi_img_url = knmi_warnings['image']
        knmi_forecast = knmi_warnings['warning']
        knmi_forecast += '\n\n'
        knmi_forecast += knmi_warnings['text']

        telegram.send_telegram_photo(token, chat_id, knmi_img_url)
        telegram.send_telegram(token, chat_id, knmi_forecast)
    
    # weeronline forecast
    weeronline_forecast = weeronline.get_weather_forecast(weeronlineurl)
    telegram.send_telegram(token, chat_id, '*Weeronline:*\n\n' + weeronline_forecast)
        

if __name__ == "__main__":
    main()
