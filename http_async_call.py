#!/usr/bin/env python

from requests_futures.sessions import FuturesSession

URL = 'https://webhook.site/72d88dec-2e2a-41a9-96e2-433ca9514684'
session = FuturesSession()

req1 = session.get(URL)
req2 = session.get(URL)
req3 = session.get(URL)

response1 = req1.result()
print(response1.headers.get('Date'))
response2 = req2.result()
print(response2.headers.get('Date'))
response3 = req3.result()
print(response3.headers.get('Date'))