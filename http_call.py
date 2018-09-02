#!/usr/bin/env python
import time
import requests

URL = 'https://webhook.site/72d88dec-2e2a-41a9-96e2-433ca9514684'


for call in range(0,3):
    req = requests.get(URL)
    print(req.headers.get('Date'))