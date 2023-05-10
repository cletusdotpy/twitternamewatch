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
# Run indefinitely until condiiton to send text
while run:
    # Don't think this actually needs the fields specified, but regardless this users endpoint gets 500requests/24hrs.
    url = f'https://api.twitter.com/2/users/by?usernames={user_id}&user.fields=created_at'
    headers = {
        'Authorization': f'Bearer {bearertoke}'
    }

    # Capture response and create plaintext var
    responseReal = requests.get(url, headers=headers)
    user_data = json.loads(responseReal.text)

    # 'errors' exists when requested user is not found. Possibly prone to false alarms, but we can't all be perfect
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
        # Print plaintext because why not, then countdown from 173 (this can run 24/7).
        # This timer can be decreased, but you will eventually hit a rate cap
        for remaining in range(173, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
