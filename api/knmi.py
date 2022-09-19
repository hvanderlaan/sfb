###############################################################################
## File     : api/knmi.py                                                    ##
## Purpose  : Send a telegram message to a telegram bot with storm forcasts  ##
##            warnings of the European continent.                            ##
##                                                                           ##
## Author   : Harald van der Laan                                            ##
## Date     : 2022/09/15                                                     ##
## Version  : v0.0.1                                                         ##
###############################################################################
## Requirements:                                                             ##
##  - Python3                                                                ##
##  - Telegram bot from @BotFather                                           ##
###############################################################################
## Changelog:                                                                ##
##  - v0.0.1    : initial version                                            ##
###############################################################################

from nis import match
import re
import json
import bs4
import httpx

def get_warning(url):
    with httpx.Client() as client:
        html = client.get(url)
    
    soup = bs4.BeautifulSoup(html.text, 'html.parser')

    knmi_image = soup.figure.img['src']
    knmi_warning = soup.h2.text
    knmi_text = soup.p.text

    if not re.match('Er zijn geen waarschuwingen', str(knmi_warning)):
        result = '{'
        result += f'"warning": "*{knmi_warning}*",'
        result += f'"text": "{knmi_text}",'
        result += f'"image": "{knmi_image}"'
        result += '}'
    else:
        result = '{"warning": "None"}'

    return json.loads(result)