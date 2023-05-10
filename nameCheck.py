# Script to secure my namesake (@cletus) on Twitter
# This shit cost me $80... better get it.

bearertoke = "ENTER_YOURS"
user_id = "ENTER_DESIRED"

import requests
import json
import time
import sys
import winsound
import usernameSelenium

run = True

while run:
    url = f'https://api.twitter.com/2/users/by?usernames={user_id}&user.fields=created_at'
    headers = {
        'Authorization': f'Bearer {bearertoke}'
    }

    responseReal = requests.get(url, headers=headers)
    user_data = json.loads(responseReal.text)

    if 'errors' in user_data:
        print("BAD RESPONSE GO GET EM TIGER")
        frequency = 1000
        duration = 5000
        winsound.Beep(frequency, duration)
        usernameSelenium.send_text()
        run = False
        break

    else:
        print(user_data)

        for remaining in range(60, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
