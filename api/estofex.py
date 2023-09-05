''' api/estofex.py: api module to get estofex data'''

###############################################################################
# File     : api/estofex.py                                                   #
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

import re
import json
import bs4
import httpx


def get_warning():
    """ get_warning: Function for getting the estofex warnings """
    baseurl = 'https://www.estofex.org'
    url = f'{baseurl}/cgi-bin/polygon/showforecast.cgi?listvalid=yes'

    with httpx.Client() as client:
        html = client.get(url)

    soup = bs4.BeautifulSoup(html.text, 'html.parser')

    try:
        level = soup.tr.findNextSiblings()[1].img.findNext()

        if re.match('.*1.png', str(level)):
            forecastlevel = 1
        elif re.match('.*2.png', str(level)):
            forecastlevel = 2
        elif re.match('.*3.png', str(level)):
            forecastlevel = 3
        else:
            forecastlevel = None

        forecastlink = soup.a['href']
        #forecastimage = soup.img['src']
        forecastimage = '/forecasts/tempmap/.png'

        result = '{'
        result += f'"level": "{forecastlevel}",'
        result += f'"link": "{forecastlink}",'
        result += f'"image": "{forecastimage}"'
        result += '}'
    except AttributeError:
        result = '{"level": "None"}'

    return json.loads(result)


def get_forecast(url):
    ''' get_forecast: getting the estofex forecast data

    url = estofex url '''
    with httpx.Client() as client:
        html = client.get(url)

    soup = bs4.BeautifulSoup(html.text, 'html.parser')
    forecast = re.sub('<br/>', '\n', str(soup.p.findNextSiblings()[1]))
    forecast = re.sub('<[^>]+>', '', str(forecast))

    result = ''
    for line in forecast.splitlines():
        if re.match('A level', str(line)):
            result += '*' + line + '*' + '\n\n'

    return result
