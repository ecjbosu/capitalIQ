#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 12:22:56 2021

@author: byersjw
"""#
#
#
from capiq.capiq_client import CapIQClient
ciq_client = CapIQClient("joe.w.byers@okstate.edu", "SSOK2018a")
return_value = ciq_client.gdsg(["IBM"], ["IQ_CLOSEPRICE"], ["close_price"], properties=[{}])

#  File "/home/byersjw/work/repo/presentations/Classes/Shared/CapitalIQ/capitalIQ.py", line 12, in <module>
#     return_value = ciq_client.gdsg(["TRIP"], ["IQ_CLOSEPRICE"], ["close_price"], properties=[{}])

#   File "/usr/local/lib/python3.9/site-packages/capiq/capiq_client.py", line 99, in gdsg
#     return self.make_request(identifiers, group_mnemonics, return_keys, properties, "GDSG", False)

#   File "/usr/local/lib/python3.9/site-packages/capiq/capiq_client.py", line 157, in make_request
#     if len(response.json()['GDSSDKResponse']) == 1 and \

#   File "/usr/lib/python3.9/site-packages/requests/models.py", line 898, in json
#     return complexjson.loads(self.text, **kwargs)

#   File "/usr/lib64/python3.9/json/__init__.py", line 346, in loads
#     return _default_decoder.decode(s)

#   File "/usr/lib64/python3.9/json/decoder.py", line 337, in decode
#     obj, end = self.raw_decode(s, idx=_w(s, 0).end())

#   File "/usr/lib64/python3.9/json/decoder.py", line 355, in raw_decode
#     raise JSONDecodeError("Expecting value", s, err.value) from None

# JSONDecodeError: Expecting value

# <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
# <html><head>
# <title>401 Unauthorized</title>
# </head><body>
# <h1>Unauthorized</h1>
# <p>This server could not verify that you
# are authorized to access the document
# requested.  Either you supplied the wrong
# credentials (e.g., bad password), or your
# browser doesn't understand how to supply
# the credentials required.</p>
# </body></html>
