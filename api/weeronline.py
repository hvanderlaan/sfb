''' api/estofex.py: api module to get estofex data'''

###############################################################################
# File     : api/weeronline.py                                                   #
# Purpose  : Send a telegram message to a telegram bot with storm forcasts    #
#            warnings of the European continent.                              #
#                                                                             #
# Author   : Harald van der Laan                                              #
# Date     : 2022/09/30                                                       #
# Version  : v0.0.1                                                           #
###############################################################################
# Requirements:                                                               #
#  - Python3                                                                  #
#  - Telegram bot from @BotFather                                             #
###############################################################################
# Changelog:                                                                  #
#  - v0.0.1    : initial version                                              #
###############################################################################

import re
import bs4
import httpx


def get_weather_forecast(url):
    ''' get_weather_forecasr: getting the forecast for today '''
    with httpx.Client() as client:
        html = client.get(url)
    
    soup = bs4.BeautifulSoup(html.text, 'html.parser')
    forecast = soup.h3.div.p

    forecast = re.sub('<[^>]+>', '', str(forecast))

    return forecast
