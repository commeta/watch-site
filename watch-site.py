#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  watch-site.py
#  
#  Copyright 2020 Evgenii Morozov <dcs-spb@ya.ru>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  Insert your token, and channel id - from telegram API
#  And change site domain for watch, example site.com

import socks
import socket
import requests

def send_telegram(text: str):
    token = "your token!!!"
    url = "https://api.telegram.org/bot"
    channel_id = "channel id!!!"
    url += token
    method = url + "/sendMessage"

    socks.set_default_proxy(socks.SOCKS5, "localhost", 9100)
    socket.socket = socks.socksocket

    # Magic!
    def getaddrinfo(*args):
         return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]
    socket.getaddrinfo = getaddrinfo

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")


from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
req = Request("https://site.com")
try:
    response = urlopen(req)
except HTTPError as e:
    send_telegram('The server couldn\'t fulfill the request. site.com')
except URLError as e:
    send_telegram('We failed to reach a server. site.com')
