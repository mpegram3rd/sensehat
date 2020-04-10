#!/usr/bin/python

import requests

resp = requests.get('https://jsonplaceholder.typicode.com/posts/1')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
body = resp.json()["body"]
title = resp.json()["title"]
print('{} \n{}'.format(body,title))


